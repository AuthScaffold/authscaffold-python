

from typing import Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IConnectionManager import IConnectionManager
from AuthScaffold.Interfaces.ServerInterface.IManagedConnection import IManagedConnection
from AuthScaffold.Interfaces.ServerInterface.ISessionManager import ISessionManager
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class ConnectionManager(IConnectionManager):
    def __init__(self) -> None:
        super().__init__()

    def OnConnectionStarted(self, client : IManagedConnection) -> Optional[IConnectionContext]:
        return None

    def OnConnectionClosed(self, context : IConnectionContext):
        pass

