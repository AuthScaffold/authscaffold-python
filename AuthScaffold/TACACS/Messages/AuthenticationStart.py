
from AuthScaffold.TACACS.Messages.Enumerations import TacacsAuthenticationAction, TacacsAuthenticationService, TacacsAuthenticationType


class AuthenticationBody:
    """
    Represents the body of an authentication message.

    Attributes:
        _action (TacacsAuthenticationAction): The authentication action.
        _priv_lvl (int): The privilege level.
        _authen_type (TacacsAuthenticationType): The authentication type.
        _authen_service (TacacsAuthenticationService): The authentication service.
        _user (str): The username.
        _port (str): The port.
        _rem_addr (str): The remote address.
        _data (str): Additional data.
    """

    def __init__(self,
                 action: TacacsAuthenticationAction,
                 priv_lvl: int,
                 authen_type: TacacsAuthenticationType,
                 authen_service: TacacsAuthenticationService,
                 user: str,
                 port: str,
                 rem_addr: str,
                 data: str):
        """
        Initializes a new instance of the AuthenticationBody class.

        Args:
            action (TacacsAuthenticationAction): The authentication action.
            priv_lvl (int): The privilege level.
            authen_type (TacacsAuthenticationType): The authentication type.
            authen_service (TacacsAuthenticationService): The authentication service.
            user (str): The username.
            port (str): The port.
            rem_addr (str): The remote address.
            data (str): Additional data.
        """
        self._action = action
        self._priv_lvl = priv_lvl
        self._authen_type = authen_type
        self._authen_service = authen_service
        self._user = user
        self._port = port
        self._rem_addr = rem_addr
        self._data = data

    @property
    def action(self) -> TacacsAuthenticationAction:
        """
        Gets or sets the authentication action.

        Returns:
            TacacsAuthenticationAction: The authentication action.
        """
        return self._action

    @action.setter
    def action(self, value : TacacsAuthenticationAction):
        """
        Sets the authentication action.

        Args:
            value (TacacsAuthenticationAction): The authentication action.

        Returns:
            None
        """
        self._action = value

    @property
    def priv_lvl(self) -> int:
        """
        Gets or sets the privilege level.

        Returns:
            int: The privilege level.
        """
        return self._priv_lvl

    @priv_lvl.setter
    def priv_lvl(self, value : int):
        """
        Sets the privilege level.

        Args:
            value (int): The privilege level.

        Returns:
            None
        """
        self._priv_lvl = value

    @property
    def authen_type(self) -> TacacsAuthenticationType:
        """
        Gets or sets the authentication type.

        Returns:
            TacacsAuthenticationType: The authentication type.
        """
        return self._authen_type

    @authen_type.setter
    def authen_type(self, value : TacacsAuthenticationType):
        """
        Sets the authentication type.

        Args:
            value (TacacsAuthenticationType): The authentication type.

        Returns:
            None
        """
        self._authen_type = value

    @property
    def authen_service(self) -> TacacsAuthenticationService:
        """
        Gets or sets the authentication service.

        Returns:
            TacacsAuthenticationService: The authentication service.
        """
        return self._authen_service

    @authen_service.setter
    def authen_service(self, value : TacacsAuthenticationService):
        """
        Sets the authentication service.

        Args:
            value (TacacsAuthenticationService): The authentication service.

        Returns:
            None
        """
        self._authen_service = value

    @property
    def user(self) -> str:
        """
        Gets or sets the username.

        Returns:
            str: The username.
        """
        return self._user

    @user.setter
    def user(self, value : str):
        """
        Sets the username.

        Args:
            value (str): The username.

        Returns:
            None
        """
        self._user = value

    @property
    def port(self) -> str:
        """
        Gets or sets the port.

        Returns:
            str: The port.
        """
        return self._port

    @port.setter
    def port(self, value : str):
        """
        Sets the port.

        Args:
            value (str): The port.

        Returns:
            None
        """
        self._port = value

    @property
    def rem_addr(self) -> str:
        """
        Gets or sets the remote address.

        Returns:
            str: The remote address.
        """
        return self._rem_addr

    @rem_addr.setter
    def rem_addr(self, value : str):
        """
        Sets the remote address.

        Args:
            value (str): The remote address.

        Returns:
            None
        """
        self._rem_addr = value

    @property
    def data(self) -> str:
        """
        Gets or sets the additional data.

        Returns:
            str: The additional data.
        """
        return self._data

    @data.setter
    def data(self, value : str):
        """
        Sets the additional data.

        Args:
            value (str): The additional data.

        Returns:
            None
        """
        self._data = value
