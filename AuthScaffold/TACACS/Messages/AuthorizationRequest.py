from typing import List
from AuthScaffold.TACACS.Messages.Enumerations import TacacsAuthenticationMethod, TacacsAuthenticationService, TacacsAuthenticationType


class AuthorizationRequest:
    """
    Represents an authorization request message in the TACACS+ protocol.

    Attributes:
        authen_method (TacacsAuthenticationMethod): The authentication method used for the authorization request.
        priv_lvl (int): The privilege level for the authorization request.
        authen_type (TacacsAuthenticationType): The authentication type for the authorization request.
        authen_service (TacacsAuthenticationService): The authentication service for the authorization request.
        user (str): The user for the authorization request.
        port (str): The port for the authorization request.
        rem_addr (str): The remote address for the authorization request.
        arguments (List[str]): The arguments for the authorization request.
    """

    def __init__(self,
                 authen_method: TacacsAuthenticationMethod,
                 priv_lvl: int,
                 authen_type: TacacsAuthenticationType,
                 authen_service: TacacsAuthenticationService,
                 user: str,
                 port: str,
                 rem_addr: str,
                 arguments: List[str]):
        """
        Initializes an AuthorizationRequest object.

        Args:
            authen_method (TacacsAuthenticationMethod): The authentication method used.
            priv_lvl (int): The privilege level.
            authen_type (TacacsAuthenticationType): The authentication type.
            authen_service (TacacsAuthenticationService): The authentication service.
            user (str): The user name.
            port (str): The port.
            rem_addr (str): The remote address.
            arguments (List[str]): The list of arguments.
        """
        self._authen_method = authen_method
        self._priv_lvl = priv_lvl
        self._authen_type = authen_type
        self._authen_service = authen_service
        self._user = user
        self._port = port
        self._rem_addr = rem_addr
        self._arguments = arguments

    @property
    def authen_method(self) -> TacacsAuthenticationMethod:
        """
        Gets the authentication method used for the authorization request.
        """
        return self._authen_method

    @authen_method.setter
    def authen_method(self, value : TacacsAuthenticationMethod):
        """
        Sets the authentication method used for the authorization request.
        """
        self._authen_method = value

    @property
    def priv_lvl(self) -> int:
        """
        Gets the privilege level for the authorization request.
        """
        return self._priv_lvl

    @priv_lvl.setter
    def priv_lvl(self, value : int):
        """
        Sets the privilege level for the authorization request.
        """
        self._priv_lvl = value

    @property
    def authen_type(self) -> TacacsAuthenticationType:
        """
        Gets the authentication type for the authorization request.
        """
        return self._authen_type

    @authen_type.setter
    def authen_type(self, value : TacacsAuthenticationType):
        """
        Sets the authentication type for the authorization request.
        """
        self._authen_type = value

    @property
    def authen_service(self) -> TacacsAuthenticationService:
        """
        Gets the authentication service for the authorization request.
        """
        return self._authen_service

    @authen_service.setter
    def authen_service(self, value : TacacsAuthenticationService):
        """
        Sets the authentication service for the authorization request.
        """
        self._authen_service = value

    @property
    def user(self) -> str:
        """
        Gets the user for the authorization request.
        """
        return self._user

    @user.setter
    def user(self, value : str):
        """
        Sets the user for the authorization request.
        """
        self._user = value

    @property
    def port(self) -> str:
        """
        Gets the port for the authorization request.
        """
        return self._port

    @port.setter
    def port(self, value : str):
        """
        Sets the port for the authorization request.
        """
        self._port = value

    @property
    def rem_addr(self) -> str:
        """
        Gets the remote address for the authorization request.
        """
        return self._rem_addr

    @rem_addr.setter
    def rem_addr(self, value : str):
        """
        Sets the remote address for the authorization request.
        """
        self._rem_addr = value

    @property
    def arguments(self) -> List[str]:
        """
        Gets the arguments for the authorization request.
        """
        return self._arguments

    @arguments.setter
    def arguments(self, value : List[str]):
        """
        Sets the arguments for the authorization request.
        """
        self._arguments = value
