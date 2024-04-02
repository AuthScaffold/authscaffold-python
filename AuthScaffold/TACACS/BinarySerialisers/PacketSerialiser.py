from AuthScaffold.TACACS.BinarySerialisers.Constants import TACACS_HEADER_LENGTH
from AuthScaffold.TACACS.BinarySerialisers.HeaderSerialiser import HeaderSerialiser
from AuthScaffold.TACACS.BinarySerialisers.Packet import Packet


class PacketSerialiser:
    def __init__(self) -> None:
        pass

    @staticmethod
    def deserialise(byte_data : bytes) -> Packet:
        if len(byte_data) < TACACS_HEADER_LENGTH:
            raise ValueError('Data is too short to be a valid TACACS packet')

        header = HeaderSerialiser.deserialise(byte_data[:TACACS_HEADER_LENGTH])

        if header.length != (len(byte_data) + TACACS_HEADER_LENGTH):
            raise ValueError('Header length does not match packet length')

        body = byte_data[TACACS_HEADER_LENGTH:]

        return Packet(header, body)

    @staticmethod
    def serialise(packet : Packet) -> bytes:
        header_bytes = HeaderSerialiser.serialise(packet.header)
        return header_bytes + packet.body
