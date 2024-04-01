

from abc import ABC, abstractmethod

from AuthScaffold.Interfaces.ServerInterface.ConnectionInformation import ConnectionInformation


class IManagedConnection(ABC):
    @property
    @abstractmethod
    def client_information(self) -> ConnectionInformation:
        """
        Gets the client information.

        Returns:
            ConnectionInformation: The client information.
        """
        pass

    @abstractmethod
    async def send(self, data : bytes):
        """
        Sends data to the client.

        Args:
            data (bytes): The data to send.
        """
        pass

    @abstractmethod
    async def receive(self, size : int, timeout_seconds : float) -> bytes:
        """
        Receives data from the client.

        Args:
            size (int): The number of bytes to receive.

        Returns:
            bytes: The received data.
        """
        pass

    @abstractmethod
    def close(self):
        """
        Closes the connection.
        """
        pass
