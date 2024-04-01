from AuthScaffold.TACACS.Messages.Enumerations import TacacsFlags, TacacsMajorVersion, TacacsMinorVersion, TacacsType


class Header:
    """Represents the header of a TACACS message."""

    def __init__(self,
                    major_version : TacacsMajorVersion,
                    minor_version : TacacsMinorVersion,
                    type : TacacsType,
                    seq_no : int,
                    flags : TacacsFlags,
                    session_id : int,
                    length : int):
        """
        Initializes a new instance of the Header class.

        Args:
            major_version (TacacsMajorVersion): The major version of the TACACS protocol.
            minor_version (TacacsMinorVersion): The minor version of the TACACS protocol.
            type (TacacsType): The type of the TACACS message.
            seq_no (int): The sequence number of the TACACS message.
            flags (TacacsFlags): The flags of the TACACS message.
            session_id (int): The session ID of the TACACS message.
            length (int): The length of the TACACS message.
        """
        self._major_version = major_version
        self._minor_version = minor_version
        self._type = type
        self._seq_no = seq_no
        self._flags = flags
        self._session_id = session_id
        self._length = length

    @property
    def major_version(self) -> TacacsMajorVersion:
        """
        Gets the major version of the TACACS protocol.

        Returns:
            TacacsMajorVersion: The major version of the TACACS protocol.
        """
        return self._major_version

    @major_version.setter
    def major_version(self, value : TacacsMajorVersion):
        """
        Sets the major version of the TACACS protocol.

        Args:
            value (TacacsMajorVersion): The major version of the TACACS protocol.
        """
        self._major_version = value

    @property
    def minor_version(self) -> TacacsMinorVersion:
        """
        Gets the minor version of the TACACS protocol.

        Returns:
            TacacsMinorVersion: The minor version of the TACACS protocol.
        """
        return self._minor_version

    @minor_version.setter
    def minor_version(self, value : TacacsMinorVersion):
        """
        Sets the minor version of the TACACS protocol.

        Args:
            value (TacacsMinorVersion): The minor version of the TACACS protocol.
        """
        self._minor_version = value

    @property
    def type(self) -> TacacsType:
        """
        Gets the type of the TACACS message.

        Returns:
            TacacsType: The type of the TACACS message.
        """
        return self._type

    @type.setter
    def type(self, value : TacacsType):
        """
        Sets the type of the TACACS message.

        Args:
            value (TacacsType): The type of the TACACS message.
        """
        self._type = value

    @property
    def seq_no(self):
        """
        Gets the sequence number of the TACACS message.

        Returns:
            int: The sequence number of the TACACS message.
        """
        return self._seq_no

    @seq_no.setter
    def seq_no(self, value : int):
        """
        Sets the sequence number of the TACACS message.

        Args:
            value (int): The sequence number of the TACACS message.
        """
        self._seq_no = value

    @property
    def flags(self):
        """
        Gets the flags of the TACACS message.

        Returns:
            TacacsFlags: The flags of the TACACS message.
        """
        return self._flags

    @flags.setter
    def flags(self, value : TacacsFlags):
        """
        Sets the flags of the TACACS message.

        Args:
            value (TacacsFlags): The flags of the TACACS message.
        """
        self._flags = value

    @property
    def session_id(self):
        """
        Gets the session ID of the TACACS message.

        Returns:
            int: The session ID of the TACACS message.
        """
        return self._session_id

    @session_id.setter
    def session_id(self, value : int):
        """
        Sets the session ID of the TACACS message.

        Args:
            value (int): The session ID of the TACACS message.
        """
        self._session_id = value

    @property
    def length(self):
        """
        Gets the length of the TACACS message.

        Returns:
            int: The length of the TACACS message.
        """
        return self._length

    @length.setter
    def length(self, value : int):
        """
        Sets the length of the TACACS message.

        Args:
            value (int): The length of the TACACS message.
        """
        self._length = value
