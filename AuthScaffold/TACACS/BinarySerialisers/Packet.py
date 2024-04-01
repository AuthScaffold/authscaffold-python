from AuthScaffold.TACACS.Messages.Header import Header

class Packet:
    """Represents a TACACS packet."""

    def __init__(self, header : Header, body : bytes):
        """
        Initializes a new instance of the Packet class.

        Args:
            header (Header): The header of the TACACS packet.
            body (bytes): The body of the TACACS packet.
        """
        self._header = header
        self._body = body

    @property
    def header(self) -> Header:
        """
        Gets the header of the TACACS packet.

        Returns:
            Header: The header of the TACACS packet.
        """
        return self._header

    @property
    def body(self) -> bytes:
        """
        Gets the body of the TACACS packet.

        Returns:
            bytes: The body of the TACACS packet.
        """
        return self._body
