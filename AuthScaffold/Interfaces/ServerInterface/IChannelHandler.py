

from abc import ABC, abstractmethod

from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class IChannelHandler(ABC):
    @abstractmethod
    def can_handle_message(self, message : Packet) -> bool:
        """
        Determines whether the router can handle the message.

        Args:
            message (Packet): The message to handle.

        Returns:
            bool: True if the router can handle the message, otherwise False.
        """
        pass

    @abstractmethod
    def handle_message(self, message : Packet, context : ISessionContext) -> Packet:
        """
        Handles a message.

        Args:
            message (Packet): The message to handle.
            context (ISessionContext): The session context.

        Returns:
            Packet: The response message.
        """
        pass
