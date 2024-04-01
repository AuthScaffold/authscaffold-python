from typing import List
from AuthScaffold.TACACS.Messages.Enumerations import TacacsAccountingFlags, TacacsAuthenticationMethod, TacacsAuthenticationService, TacacsAuthenticationType


class AccountingRequest:
    """
    Represents an accounting request packet in the TACACS+ protocol.

    Attributes:
        _flags (TacacsAccountingFlags): The flags field of the accounting request packet.
        _authen_method (TacacsAuthenticationMethod): The authentication method field of the accounting request packet.
        _priv_lvl (int): The privilege level field of the accounting request packet.
        _authen_type (TacacsAuthenticationType): The authentication type field of the accounting request packet.
        _authen_service (TacacsAuthenticationService): The authentication service field of the accounting request packet.
        _user (str): The user field of the accounting request packet.
        _port (str): The port field of the accounting request packet.
        _rem_address (str): The remote address field of the accounting request packet.
        _args (List[str]): The arguments field of the accounting request packet.
    """

    def __init__(self,
                 flags: TacacsAccountingFlags,
                 authen_method: TacacsAuthenticationMethod,
                 priv_lvl: int,
                 authen_type: TacacsAuthenticationType,
                 authen_service: TacacsAuthenticationService,
                 user: str,
                 port: str,
                 rem_add: str,
                 args: List[str]):
        """
        Constructor for the AccountingRequest class.

        Args:
            flags (TacacsAccountingFlags): The flags field of the accounting request packet.
            authen_method (TacacsAuthenticationMethod): The authentication method field of the accounting request packet.
            priv_lvl (int): The privilege level field of the accounting request packet.
            authen_type (TacacsAuthenticationType): The authentication type field of the accounting request packet.
            authen_service (TacacsAuthenticationService): The authentication service field of the accounting request packet.
            user (str): The user field of the accounting request packet.
            port (str): The port field of the accounting request packet.
            rem_add (str): The remote address field of the accounting request packet.
            args (List[str]): The arguments field of the accounting request packet.
        """
        self._flags = flags
        self._authen_method = authen_method
        self._priv_lvl = priv_lvl
        self._authen_type = authen_type
        self._authen_service = authen_service
        self._user = user
        self._port = port
        self._rem_address = rem_add
        self._args = args

    @property
    def flags(self) -> TacacsAccountingFlags:
        """
        Get the flags field of the accounting request packet.
        """
        return self._flags

    @flags.setter
    def flags(self, value : TacacsAccountingFlags):
        """
        Set the flags field of the accounting request packet.
        """
        self._flags = value

    @property
    def authen_method(self) -> TacacsAuthenticationMethod:
        """
        Get the authentication method field of the accounting request packet.
        """
        return self._authen_method

    @authen_method.setter
    def authen_method(self, value : TacacsAuthenticationMethod):
        """
        Set the authentication method field of the accounting request packet.
        """
        self._authen_method = value

    @property
    def priv_lvl(self) -> int:
        """
        Get the privilege level field of the accounting request packet.
        """
        return self._priv_lvl

    @priv_lvl.setter
    def priv_lvl(self, value : int):
        """
        Set the privilege level field of the accounting request packet.
        """
        self._priv_lvl = value

    @property
    def authen_type(self) -> TacacsAuthenticationType:
        """
        Get the authentication type field of the accounting request packet.
        """
        return self._authen_type

    @authen_type.setter
    def authen_type(self, value : TacacsAuthenticationType):
        """
        Set the authentication type field of the accounting request packet.
        """
        self._authen_type = value

    @property
    def authen_service(self) -> TacacsAuthenticationService:
        """
        Get the authentication service field of the accounting request packet.
        """
        return self._authen_service

    @authen_service.setter
    def authen_service(self, value : TacacsAuthenticationService):
        """
        Set the authentication service field of the accounting request packet.
        """
        self._authen_service = value

    @property
    def user(self) -> str:
        """
        Get the user field of the accounting request packet.
        """
        return self._user

    @user.setter
    def user(self, value : str):
        """
        Set the user field of the accounting request packet.
        """
        self._user = value

    @property
    def port(self) -> str:
        """
        Get the port field of the accounting request packet.
        """
        return self._port

    @port.setter
    def port(self, value : str):
        """
        Set the port field of the accounting request packet.
        """
        self._port = value

    @property
    def rem_add(self) -> str:
        """
        Get the remote address field of the accounting request packet.
        """
        return self._rem_address

    @rem_add.setter
    def rem_add(self, value : str):
        """
        Set the remote address field of the accounting request packet.
        """
        self._rem_address = value

    @property
    def args(self) -> List[str]:
        """
        Get the arguments field of the accounting request packet.
        """
        return self._args

    @args.setter
    def args(self, value : List[str]):
        """
        Set the arguments field of the accounting request packet.
        """
        self._args = value
