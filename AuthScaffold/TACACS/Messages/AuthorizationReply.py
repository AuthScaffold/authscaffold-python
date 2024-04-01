from AuthScaffold.TACACS.Messages.Enumerations import TacacsAuthorizationStatus
from typing import List


from typing import List

class AuthorizationReply:
    """
    Represents an authorization reply message in the TACACS+ protocol.

    Attributes:
        status (TacacsAuthorizationStatus): The status of the authorization reply.
        args (List[str]): The arguments of the authorization reply.
        server_msg (str): The server message of the authorization reply.
        data (str): The data of the authorization reply.
    """

    def __init__(self, status: TacacsAuthorizationStatus, args: List[str], server_msg: str, data: str):
        """
        Initializes a new instance of the AuthorizationReply class.

        Args:
            status (TacacsAuthorizationStatus): The status of the authorization reply.
            args (List[str]): The arguments of the authorization reply.
            server_msg (str): The server message of the authorization reply.
            data (str): The data of the authorization reply.
        """
        self._status = status
        self._args = args
        self._server_msg = server_msg
        self._data = data

    @property
    def status(self) -> TacacsAuthorizationStatus:
        """
        Get the status of the authorization reply.

        Returns:
            TacacsAuthorizationStatus: The status of the authorization reply.
        """
        return self._status

    @status.setter
    def status(self, value: TacacsAuthorizationStatus):
        """
        Set the status of the authorization reply.

        Args:
            value (TacacsAuthorizationStatus): The status to set.
        """
        self._status = value

    @property
    def args(self) -> List[str]:
        """
        Get the arguments of the authorization reply.

        Returns:
            List[str]: The arguments of the authorization reply.
        """
        return self._args

    @args.setter
    def args(self, value: List[str]):
        """
        Set the arguments of the authorization reply.

        Args:
            value (List[str]): The arguments to set.
        """
        self._args = value

    @property
    def server_msg(self) -> str:
        """
        Get the server message of the authorization reply.

        Returns:
            str: The server message of the authorization reply.
        """
        return self._server_msg

    @server_msg.setter
    def server_msg(self, value: str):
        """
        Set the server message of the authorization reply.

        Args:
            value (str): The server message to set.
        """
        self._server_msg = value

    @property
    def data(self) -> str:
        """
        Get the data of the authorization reply.

        Returns:
            str: The data of the authorization reply.
        """
        return self._data

    @data.setter
    def data(self, value: str):
        """
        Set the data of the authorization reply.

        Args:
            value (str): The data to set.
        """
        self._data = value
