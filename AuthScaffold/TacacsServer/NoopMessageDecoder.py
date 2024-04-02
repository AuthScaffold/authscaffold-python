
from typing import Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IMessageDecoder import IMessageDecoder
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet
from AuthScaffold.TACACS.Messages.Enumerations import TacacsFlags


class NoopMessageDecoder(IMessageDecoder):
    def decode_message(self, message : Packet, context : IConnectionContext) -> Optional[Packet]:
        if (message.header.flags & TacacsFlags.TAC_PLUS_UNENCRYPTED_FLAG) == TacacsFlags.TAC_PLUS_UNENCRYPTED_FLAG:
            return message

        return None

    def encode_message(self, message : Packet, context : IConnectionContext) -> Optional[Packet]:
        return message
