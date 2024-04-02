from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext


class SessionContext(ISessionContext):
    def __init__(self, session_id : int, connectionContext : IConnectionContext) -> None:
        super().__init__()

        self._connection_context = connectionContext
        self._is_session_closed = False
        self._session_id = session_id

    @property
    def session_id(self) -> int:
        return self._session_id

    @property
    def connection_context(self) -> IConnectionContext:
        return self._connection_context

    def close_session(self):
        self._is_session_closed = True

    def is_session_complete(self) -> bool:
        return self._is_session_closed
