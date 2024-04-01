from abc import ABC, abstractmethod
from typing import Optional

from AuthScaffold.Interfaces.ServerInterface.IConnectionContext import IConnectionContext
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class IMessageDecoder(ABC):
    """
    This is an interface for message decoders. It provides a contract for encoding and decoding messages.

    The IMessageDecoder method is responsible for decoding and encoding a message in exactly
    the same way for a given IConnectionContext. Both `decode_message` and `encode_message`
    takes a `Packet` instance and returns a decoded (or encoded) `Packet` instance.

    Note:

    1. In some cases the decoding logic may be complex and may involve multiple sub-decoders.
    If the decoding logic is complex it is recommended to memoise the sucessful decoder for
    performance improvement.

    2. When no encode/decode logic is required, the `decode_message` and `encode_message` methods
    can be implemented to return the input message as is.

    """


    @abstractmethod
    def decode_message(self, message: Packet, context : IConnectionContext) -> Optional[Packet]:
        """
        Decodes a message.

        Args:
            message (bytes): The message to decode.

        Returns:
            Optional[Packet]: The decoded message. None if the message could not be encoded.
        """
        pass

    @abstractmethod
    def encode_message(self, message: Packet, context : IConnectionContext) -> Optional[Packet]:
        """
        Encodes a message.

        Args:
            message (Packet): The message to encode.

        Returns:
            Optional[Packet]: The encoded message. None if the message could not be encoded.
        """
        pass
