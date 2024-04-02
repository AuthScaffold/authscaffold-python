

from abc import ABC, abstractmethod
from typing import Optional

from AuthScaffold.Interfaces.ServerInterface.ISessionContext import ISessionContext
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class IChannelRouter(ABC):
    @abstractmethod
    def route_message(self, message : Packet, context : ISessionContext) -> Optional[Packet]:
        """
        Routes a message to the appropriate session.

        Args:
            message (IMessage): The message to route.
        """
        pass
