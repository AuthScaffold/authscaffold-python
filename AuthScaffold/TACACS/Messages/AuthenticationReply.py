from AuthScaffold.TACACS.Messages.Enumerations import TacacsAuthenicationReplyFlags, TacacsAuthenticationStatus


class AuthenticationReply:
    """
    Represents a TACACS+ Authentication Reply message.

    Attributes:
        status (TacacsAuthenticationStatus): The authentication status.
        flags (TacacsAuthenicationReplyFlags): The authentication reply flags.
        server_msg (str): The server message.
        data (str): The data associated with the authentication reply.
    """

    def __init__(self,
                 status: TacacsAuthenticationStatus,
                 flags: TacacsAuthenicationReplyFlags,
                 server_msg: str,
                 data: str):
        """
        Initializes a new instance of the AuthenticationReply class.

        Args:
            status (TacacsAuthenticationStatus): The authentication status.
            flags (TacacsAuthenicationReplyFlags): The authentication reply flags.
            server_msg (str): The server message.
            data (str): The data associated with the authentication reply.
        """
        self._status = status
        self._flags = flags
        self._server_msg = server_msg
        self._data = data

    @property
    def status(self) -> TacacsAuthenticationStatus:
        """
        Get the authentication status.

        Returns:
            TacacsAuthenticationStatus: The authentication status.
        """
        return self._status

    @status.setter
    def status(self, value: TacacsAuthenticationStatus):
        """
        Set the authentication status.

        Args:
            value (TacacsAuthenticationStatus): The authentication status.
        """
        self._status = value

    @property
    def flags(self) -> TacacsAuthenicationReplyFlags:
        """
        Get the authentication reply flags.

        Returns:
            TacacsAuthenicationReplyFlags: The authentication reply flags.
        """
        return self._flags

    @flags.setter
    def flags(self, value: TacacsAuthenicationReplyFlags):
        """
        Set the authentication reply flags.

        Args:
            value (TacacsAuthenicationReplyFlags): The authentication reply flags.
        """
        self._flags = value

    @property
    def server_msg(self) -> str:
        """
        Get the server message.

        Returns:
            str: The server message.
        """
        return self._server_msg

    @server_msg.setter
    def server_msg(self, value: str):
        """
        Set the server message.

        Args:
            value (str): The server message.
        """
        self._server_msg = value

    @property
    def data(self) -> str:
        """
        Get the data associated with the authentication reply.

        Returns:
            str: The data associated with the authentication reply.
        """
        return self._data

    @data.setter
    def data(self, value: str):
        """
        Set the data associated with the authentication reply.

        Args:
            value (str): The data associated with the authentication reply.
        """
        self._data = value
