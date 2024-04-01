

from abc import ABC, abstractmethod


class IConnectionContext(ABC):
    """Connection context interface.

    A connection context details information about how the connection
    is made that can be passed down to sessions and other components
    to tie them to the connection.

    It is assumed that the implimentor might extend the connection
    context to include more information about the connection, the device
    that is connecting, etc.
    """

    @property
    @abstractmethod
    def connection_id(self) -> int:
        """
        Gets the connection ID.

        Returns:
            int: The connection ID.
        """
        pass

    @property
    @abstractmethod
    def connection_type(self) -> str:
        """
        Gets the connection type.

        Returns:
            str: The connection type.
        """
        pass

    @property
    @abstractmethod
    def client_address(self) -> str:
        """
        Gets the client address.

        Returns:
            str: The client address.
        """
        pass
