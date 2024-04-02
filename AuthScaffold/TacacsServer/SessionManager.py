from typing import Dict, Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext
from AuthScaffold.Interfaces.ServerInterface.ISessionManager import ISessionManager
from AuthScaffold.TACACS.Messages.Enumerations import TacacsFlags
from AuthScaffold.TACACS.Messages.Header import Header
from AuthScaffold.TacacsServer.SessionContext import SessionContext



class SessionManager(ISessionManager):
    def __init__(self) -> None:
        super().__init__()

        self._sessions : Dict[int, ISessionContext] = {}

        self._multisession_negotiation_complete = False
        self._client_supports_multisession = False

    def is_multi_session(self) -> bool:
        return self._client_supports_multisession and self._multisession_negotiation_complete

    def start_session(self, header : Header, context : IConnectionContext) -> Optional[ISessionContext]:
        self.update_multisession_state(header)

        if self._sessions.get(header.session_id) is not None:
            return None

        session = SessionContext(header.session_id, context)
        self._sessions[header.session_id] = session

        return session

    def get_session(self, header: Header) -> Optional[ISessionContext]:
        session = self._sessions.get(header.session_id)
        if session is not None:
            self.update_multisession_state(header)
            self._multisession_negotiation_complete = True
            return session

    def end_session(self, session : ISessionContext):
        self._sessions.pop(session.session_id, None)

    def update_multisession_state(self, header: Header):
        if self._multisession_negotiation_complete:
            return

        clientSupportsMultisession = (header.flags & TacacsFlags.TAC_PLUS_SINGLE_CONNECT_FLAG) == TacacsFlags.TAC_PLUS_SINGLE_CONNECT_FLAG
        if clientSupportsMultisession:
            self._client_supports_multisession = clientSupportsMultisession
            self._multisession_negotiation_complete = True


