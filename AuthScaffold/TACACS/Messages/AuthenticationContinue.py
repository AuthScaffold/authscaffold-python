from AuthScaffold.TACACS.Messages.Enumerations import TacacsAuthenticationContinueStatus


class AuthenticationContinue:
    """
    Represents a TACACS+ Authentication Continue message.

    Attributes:
        user_msg (str): The user message.
        data (str): The data associated with the message.
        flags (TacacsAuthenticationContinueStatus): The flags indicating the status of the authentication continue.
    """

    def __init__(self, user_msg: str, data: str, flags: TacacsAuthenticationContinueStatus):
        """
        Initializes a new instance of the AuthenticationContinue class.

        Args:
            user_msg (str): The user message.
            data (str): The data.
            flags (TacacsAuthenticationContinueStatus): The flags indicating the status of the authentication continue message.
        """
        self._user_msg = user_msg
        self._data = data
        self._flags = flags

    @property
    def user_msg(self) -> str:
        """
        Get the user message.

        Returns:
            str: The user message.
        """
        return self._user_msg

    @user_msg.setter
    def user_msg(self, value: str):
        """
        Set the user message.

        Args:
            value (str): The user message.
        """
        self._user_msg = value

    @property
    def data(self) -> str:
        """
        Get the data associated with the message.

        Returns:
            str: The data associated with the message.
        """
        return self._data

    @data.setter
    def data(self, value: str):
        """
        Set the data associated with the message.

        Args:
            value (str): The data associated with the message.
        """
        self._data = value

    @property
    def flags(self) -> TacacsAuthenticationContinueStatus:
        """
        Get the flags indicating the status of the authentication continue.

        Returns:
            TacacsAuthenticationContinueStatus: The flags indicating the status of the authentication continue.
        """
        return self._flags

    @flags.setter
    def flags(self, value: TacacsAuthenticationContinueStatus):
        """
        Set the flags indicating the status of the authentication continue.

        Args:
            value (TacacsAuthenticationContinueStatus): The flags indicating the status of the authentication continue.
        """
        self._flags = value
