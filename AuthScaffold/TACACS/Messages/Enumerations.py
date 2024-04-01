from enum import Enum, Flag


class TacacsMajorVersion(Enum):
    """
    Enumeration class representing the major versions of the TACACS+ protocol.
    """
    TACACS_PLUS_MAJOR_1 = 0xc

class TacacsMinorVersion(Enum):
    """
    Enumeration class representing the minor versions of the TACACS+ protocol.
    """

    TACACS_PLUS_MINOR_VER_DEFAULT = 0x0
    TACACS_PLUS_MINOR_VER_ONE = 0x1

class TacacsType(Enum):
    """
    Enumeration class representing the types of TACACS+ messages.
    """

    TAC_PLUS_AUTHENTICATION = 0x1
    TAC_PLUS_AUTHORISATION = 0x2
    TAC_PLUS_ACCOUNTING = 0x3

class TacacsFlags(Flag):
    """
    Enumeration class representing the flags of TACACS+ messages.
    """

    TAC_PLUS_UNENCRYPTED_FLAG = 0x01
    TAC_PLUS_SINGLE_CONNECT_FLAG = 0x04


class TacacsAuthenticationAction(Enum):
    """
    Enumeration class representing the actions that can be taken in response to an authentication request.
    """

    TAC_PLUS_AUTHEN_LOGIN = 0x1
    TAC_PLUS_AUTHEN_CHPASS = 0x2
    TAC_PLUS_AUTHEN_SENDAUTH = 0x3

class TacacsAuthenticationType(Enum):
    """
    Enumeration class representing the types of authentication requests.
    """

    TAC_PLUS_AUTHEN_TYPE_NOT_SET = 0x00
    TAC_PLUS_AUTHEN_TYPE_ASCII = 0x1
    TAC_PLUS_AUTHEN_TYPE_PAP = 0x2
    TAC_PLUS_AUTHEN_TYPE_CHAP = 0x3
    TAC_PLUS_AUTHEN_TYPE_MSCHAP = 0x5
    TAC_PLUS_AUTHEN_TYPE_MSCHAPV2 = 0x6

class TacacsAuthenticationService(Enum):
    """
    Enumeration class representing the services that can be authenticated.
    """

    TAC_PLUS_AUTHEN_SVC_NONE = 0x0
    TAC_PLUS_AUTHEN_SVC_LOGIN = 0x1
    TAC_PLUS_AUTHEN_SVC_ENABLE = 0x2
    TAC_PLUS_AUTHEN_SVC_PPP = 0x3
    TAC_PLUS_AUTHEN_SVC_PT = 0x5
    TAC_PLUS_AUTHEN_SVC_RCMD = 0x6
    TAC_PLUS_AUTHEN_SVC_X25 = 0x7
    TAC_PLUS_AUTHEN_SVC_NASI = 0x8
    TAC_PLUS_AUTHEN_SVC_FWPROXY = 0x9

class TacacsAuthenticationStatus(Enum):
    """
    Enumeration class representing the status of an authentication request.
    """

    TAC_PLUS_AUTHEN_STATUS_PASS = 0x1
    TAC_PLUS_AUTHEN_STATUS_FAIL = 0x2
    TAC_PLUS_AUTHEN_STATUS_GETDATA = 0x3
    TAC_PLUS_AUTHEN_STATUS_GETUSER = 0x4
    TAC_PLUS_AUTHEN_STATUS_GETPASS = 0x5
    TAC_PLUS_AUTHEN_STATUS_RESTART = 0x6
    TAC_PLUS_AUTHEN_STATUS_ERROR = 0x7
    TAC_PLUS_AUTHEN_STATUS_FOLLOW = 0x21

class TacacsAuthenicationReplyFlags(Flag):
    """
    Enumeration class representing the flags of an authentication reply.
    """

    TAC_PLUS_AUTHEN_FLAG_NOECHO = 0x1


class TacacsAuthenticationContinueStatus(Enum):
    """
    Enumeration class representing the status of an authentication continue message.
    """

    TAC_PLUS_CONTINUE_FLAG_ABORT = 0x01

class TacacsAuthenticationMethod(Enum):
    """
    Enumeration class representing the authentication methods used in TACACS+.
    """
    TAC_PLUS_AUTHEN_METH_NOT_SET = 0x00
    TAC_PLUS_AUTHEN_METH_NONE = 0x01
    TAC_PLUS_AUTHEN_METH_KRB5 = 0x02
    TAC_PLUS_AUTHEN_METH_LINE = 0x03
    TAC_PLUS_AUTHEN_METH_ENABLE = 0x04
    TAC_PLUS_AUTHEN_METH_LOCAL = 0x05
    TAC_PLUS_AUTHEN_METH_TACACSPLUS = 0x06
    TAC_PLUS_AUTHEN_METH_GUEST = 0x08
    TAC_PLUS_AUTHEN_METH_RADIUS = 0x10
    TAC_PLUS_AUTHEN_METH_KRB4 = 0x11
    TAC_PLUS_AUTHEN_METH_RCMD = 0x20


class TacacsAuthorizationStatus(Enum):
    """
    Enumeration class representing the status of an authorization request.
    """
    TAC_PLUS_AUTHOR_STATUS_PASS_ADD = 0x01
    TAC_PLUS_AUTHOR_STATUS_PASS_REPL = 0x02
    TAC_PLUS_AUTHOR_STATUS_FAIL = 0x10
    TAC_PLUS_AUTHOR_STATUS_ERROR = 0x11
    TAC_PLUS_AUTHOR_STATUS_FOLLOW = 0x21


class TacacsAccountingFlags(Flag):
    """
    Enumeration class representing the flags of TACACS+ accounting messages.
    """
    TAC_PLUS_ACCT_FLAG_START = 0x02
    TAC_PLUS_ACCT_FLAG_STOP = 0x04
    TAC_PLUS_ACCT_FLAG_WATCHDOG = 0x08
