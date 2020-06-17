from dataclasses import dataclass
from typing import List


@dataclass
class DomainDto:
    domain_id: int
    domain_name: str
    description: str

@dataclass
class UserDto:
    user_id: int
    name: str

@dataclass
class DomainStatDto:
    domain_id: int
    followers_count: int
    posts_count: int
    bookmarked_count: int

@dataclass
class DomainJoinRequestDto:
    request_id: int
    user_id: int

@dataclass
class DomainDetailsDto:
    domain: DomainDto
    domain_stats: DomainStatDto
    domain_experts: List[UserDto]
    user_id: int
    is_user_domain_expert: bool
    requested_users_dto: List[UserDto]
    