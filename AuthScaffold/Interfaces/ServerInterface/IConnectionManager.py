from abc import ABC, abstractmethod
from typing import Optional

from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IManagedConnection import IManagedConnection


class IConnectionManager(ABC):
    @abstractmethod
    def OnConnectionStarted(self, client : IManagedConnection) -> Optional[IConnectionContext]:
        """Callout when a connection is started.

        This method is called when a connection is started. The connection
        manager should create a connection context and return it. The
        connection context will be passed to the session manager to create
        a session context.

        The return type is set as optional, but the connection context
        should always be created. If the connection context cannot be
        created, the caller should assume the connection is not allowed.

        Args:
            client (IManagedConnection): The connection that was started.

        Returns:
            Optional[IConnectionContext]: _description_
        """
        pass

