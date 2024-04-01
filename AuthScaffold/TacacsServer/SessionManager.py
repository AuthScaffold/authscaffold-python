
from typing import Dict, Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionManager import ISessionManager

class SessionManager(ISessionManager):
    def __init__(self) -> None:
        super().__init__()

        self._sessions : Dict[int, ISessionContext] = {}

    def is_multi_session(self) -> bool:
        return False

    def start_session(self, session_id : int, context : IConnectionContext) -> Optional[ISessionContext]:
        pass

    def get_session(self, session_id: int) -> Optional[ISessionContext]:
        pass

    def end_session(self, session : ISessionContext):
        pass
