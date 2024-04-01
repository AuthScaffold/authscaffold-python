import asyncio
from typing import Tuple
from AuthScaffold.Interfaces.ServerInterface.ConnectionInformation import ConnectionInformation
from AuthScaffold.Interfaces.ServerInterface.IManagedConnection import IManagedConnection


class ManagedConnection(IManagedConnection):
    def __init__(self, reader : asyncio.StreamReader, writer : asyncio.StreamWriter) -> None:
        super().__init__()

        self._reader = reader
        self._writer = writer

        peer_information : Tuple[str, int] = writer.get_extra_info('peername')
        peer_ip = peer_information[0]
        peer_port = peer_information[1]

        self._client_connection = ConnectionInformation(peer_ip, peer_port)

    @property
    def client_information(self) -> ConnectionInformation:
        return self._client_connection

    async def send(self, data : bytes):
        self._writer.write(data)
        await self._writer.drain()

    async def receive(self, size : int, timeout_seconds : float) -> bytes:
        return await asyncio.wait_for(self._reader.read(size), timeout_seconds)

    def close(self):
        self._writer.close()
