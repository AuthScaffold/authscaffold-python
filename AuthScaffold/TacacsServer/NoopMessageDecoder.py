
from typing import Optional
from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.Interfaces.ServerInterface.IMessageDecoder import IMessageDecoder
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class NoopMessageDecoder(IMessageDecoder):
    def decode_message(self, message : Packet, context : IConnectionContext) -> Optional[Packet]:
        return message

    def encode_message(self, message : Packet, context : IConnectionContext) -> Optional[Packet]:
        return message
