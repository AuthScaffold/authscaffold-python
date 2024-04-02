

import asyncio
from typing import Optional

from AuthScaffold.Interfaces.ServerInterface.IChannelRouter import IChannelRouter
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IManagedConnection import IManagedConnection
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet
from AuthScaffold.TACACS.BinarySerialisers.PacketSerialiser import PacketSerialiser
from AuthScaffold.TACACS.Messages.Enumerations import TacacsFlags
from AuthScaffold.TacacsServer.ConnectionManager import ConnectionManager
from AuthScaffold.TacacsServer.ManagedConnection import ManagedConnection
import AuthScaffold.TACACS.BinarySerialisers.Constants as TacacsConstants
from AuthScaffold.TACACS.BinarySerialisers.HeaderSerialiser import HeaderSerialiser
from AuthScaffold.TacacsServer.NoopMessageDecoder import NoopMessageDecoder
from AuthScaffold.TacacsServer.SessionManager import SessionManager
from contextlib import contextmanager

connection_manager = ConnectionManager()
header_serialiser = HeaderSerialiser()
decoder = NoopMessageDecoder()
message_router : IChannelRouter = IChannelRouter()

@contextmanager
def connection_onclosed_handler(context : Optional[IConnectionContext]):
    if context is None:
        return

    try:
        yield context
    finally:
        connection_manager.OnConnectionClosed(context)

@contextmanager
def connection_close_on_exit(connection : IManagedConnection):
    try:
        yield connection
    finally:
        connection.close()

async def handle_client(reader : asyncio.StreamReader, writer : asyncio.StreamWriter):
    with connection_close_on_exit(ManagedConnection(reader, writer)) as connection:
        with connection_onclosed_handler(connection_manager.OnConnectionStarted(connection)) as connection_context:
            session_manager = SessionManager()

            while True:
                # Wait up to 2 minutes for a packet
                data = await connection.receive(TacacsConstants.TACACS_HEADER_LENGTH, 120)
                if len(data) != TacacsConstants.TACACS_HEADER_LENGTH:
                    break

                header = header_serialiser.deserialise(data)

                # Recover or create a new session context
                session = session_manager.get_session(header)
                session = session or session_manager.start_session(header, connection_context)
                if session is None:
                    break

                # Wait up to 15 seconds for the body
                body = await connection.receive(header.length, 15)
                if len(body) != header.length:
                    break

                # Try decoding the packet
                packet_encoded = Packet(header, body)
                packet_decoded = decoder.decode_message(packet_encoded, connection_context)
                if packet_decoded is None:
                    break

                #question: Is a device expecting in-order request-response?

                # Process the packet
                response_packet = message_router.route_message(packet_decoded, session)

                # If a response was generated, send it
                if response_packet is not None:
                    response_packet_encoded = decoder.encode_message(response_packet, connection_context)
                    if response_packet_encoded is not None:
                        response_packet_encoded.header.flags = response_packet_encoded.header.flags | TacacsFlags.TAC_PLUS_SINGLE_CONNECT_FLAG
                        response_bytes = PacketSerialiser.serialise(response_packet_encoded)
                        await connection.send(response_bytes)

                # Handle session completion
                if session.is_session_complete():
                    session_manager.end_session(session)

                    # If not in multi-session mode, close the connection
                    if not session_manager.is_multi_session():
                        break




async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
