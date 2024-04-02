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

    @property
    @abstractmethod
    def session_id(self) -> int:
        """
        Gets the session ID.

        Returns:
            int: The session ID.
        """
        pass

    @abstractmethod
    def close_session(self):
        """
        Closes the session.
        """
        pass

    @abstractmethod
    def is_session_complete(self) -> bool:
        """
        Indicates if the session is complete.

        Returns:
            bool: True if the session is complete, False otherwise.
        """
        pass





