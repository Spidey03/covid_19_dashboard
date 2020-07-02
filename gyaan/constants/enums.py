import enum

from ib_common.constants import BaseEnumClass


class CodeLanguage(BaseEnumClass, enum.Enum):
    python = "PYTHON"
    c_language = "C"
    c_plus_plus = "CPP"
    python36 = "PYTHON36"
    python37 = "PYTHON37"
    python38 = "PYTHON38"
    python38_datascience = "PYTHON38_DATASCIENCE"
    python38_aiml = "PYTHON38_AIML"

class Role(BaseEnumClass, enum.Enum):
    DEVELOPER = "DEVELOPER"
    DESIGNER = "DESIGNER"


class JoinStatus(BaseEnumClass, enum.Enum):
    REQUESTED = "REQUESTED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"


class PostStatus(BaseEnumClass, enum.Enum):
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"


class ReactionEntityType(BaseEnumClass, enum.Enum):
    Post = "post"
    Comment = "comment"
    Domain = "domain"
    Reply = "reply"

class RequestStatus(BaseEnumClass, enum.Enum):
    ACCEPTED = "accepted"
    REJECTED = "rejected"