
from abc import ABC, abstractmethod
from typing import Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext


class ISessionManager(ABC):
    @abstractmethod
    def is_multi_session(self) -> bool:
        """
        Indicates if the session manager supports multiple sessions.

        Returns:
            bool: True if multiple sessions are supported, False otherwise.
        """
        pass

    @abstractmethod
    def start_session(self, session_id : int, context : IConnectionContext) -> Optional[ISessionContext]:
        """
        Opens a session.

        If this is the first session the Session Manager
        should also negotiate single connection mode.

        Args:
            session_id (int): The session ID.
            context (IConnectionContext): The connection context.

        Returns:
            Optional[ISessionContext]: The session context. Null if the session ID is already in use.
        """
        pass

    @abstractmethod
    def get_session(self, session_id : int) -> Optional[ISessionContext]:
        """
        Gets a session by its ID.

        Args:
            session_id (int): The session ID.

        Returns:
            Optional[ISessionContext]: The session context if found, None otherwise.
        """
        pass

    @abstractmethod
    def end_session(self, session : ISessionContext):
        """
        Closes a session.

        Args:
            session (ISessionContext): The session to close.
        """
        pass
