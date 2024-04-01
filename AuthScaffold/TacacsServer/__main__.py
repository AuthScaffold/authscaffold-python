

import asyncio
from typing import Optional

from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IManagedConnection import IManagedConnection
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet
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
                    return

                header = header_serialiser.deserialise(data)

                # Recover or create a new session context
                session = session_manager.get_session(header.session_id)
                session = session or session_manager.start_session(header.session_id, connection_context)
                if session is None:
                    return

                # Wait up to 15 seconds for the body
                body = await connection.receive(header.length, 15)
                if len(body) != header.length:
                    return

                # Try decoding the packet
                packet_encoded = Packet(header, body)
                packet_decoded = decoder.decode_message(packet_encoded, connection_context)
                if packet_decoded is None:
                    return








async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 8888)

    async with server:
        await server.serve_forever()

asyncio.run(main())
