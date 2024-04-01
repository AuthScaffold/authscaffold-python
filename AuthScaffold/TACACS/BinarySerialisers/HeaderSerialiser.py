import struct

from AuthScaffold.TACACS.Messages.Enumerations import TacacsFlags, TacacsMajorVersion, TacacsMinorVersion, TacacsType
from AuthScaffold.TACACS.Messages.Header import Header

class HeaderSerialiser:
    """

    1 2 3 4 5 6 7 8  1 2 3 4 5 6 7 8  1 2 3 4 5 6 7 8  1 2 3 4 5 6 7 8
    +----------------+----------------+----------------+----------------+
    |major  | minor  |                |                |                |
    |version| version|      type      |     seq_no     |   flags        |
    +----------------+----------------+----------------+----------------+
    |                                                                   |
    |                            session_id                             |
    +----------------+----------------+----------------+----------------+
    |                                                                   |
    |                              length                               |
    +----------------+----------------+----------------+----------------+


    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def deserialise(byte_data : bytes) -> Header:
        major_minor_version, typebyte, seq_no, flags, session_id, length = struct.unpack(
            '!BBBBII', byte_data)

        major_version = major_minor_version >> 4
        minor_version = major_minor_version & 0b00001111

        return Header(
            TacacsMajorVersion(major_version),
            TacacsMinorVersion(minor_version),
            TacacsType(typebyte),
            seq_no,
            TacacsFlags(flags),
            session_id,
            length
        )

    @staticmethod
    def serialise(header : Header) -> bytes:
        byte_data = struct.pack(
            '!BBBBII',
            (header.major_version.value << 4) | header.minor_version.value,
            header.type.value,
            header.seq_no,
            header.flags.value,
            header.session_id,
            header.length
        )

        return byte_data
