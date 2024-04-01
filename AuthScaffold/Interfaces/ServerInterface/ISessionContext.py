from abc import ABC, abstractmethod

from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext

class ISessionContext(ABC):
    @property
    @abstractmethod
    def connection_context(self) -> IConnectionContext:
        """
        Gets the connection context.

        Returns:
            IConnectionContext: The connection context.
        """
        pass

    @abstractmethod
    def close_session(self):
        """
        Closes the session.
        """
        pass



