import datetime
from typing import List
from dataclasses import dataclass


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


@dataclass
class TagDto:
    tag_id: int
    name: str


@dataclass
class PostTagDto:
    post_id: int
    tag_id: int

@dataclass
class PostTagDetailsDto:
    tags: List[TagDto]
    post_tags: List[PostTagDto]

@dataclass
class PostDto:
    post_id: int
    title: str
    content: str
    posted_by: int
    posted_at: datetime.datetime

@dataclass
class PostCommentsCount:
    post_id: int
    comments_count: int

@dataclass
class PostReactionsCount:
    post_id: int
    reactions_count: int

@dataclass
class CommentRepliesCount:
    comment_id: int
    replies_count: int

@dataclass
class CommentReactionsCount:
    comment_id: int
    reactions_count: int

@dataclass
class CommentDto:
    comment_id: int
    post_id: int
    content: str
    commented_by: int
    commented_at: datetime.datetime

@dataclass
class CompletePostDetailsDto:
    post_dtos: List[PostDto]
    post_reaction_counts: List[PostReactionsCount]
    comment_counts: List[PostCommentsCount]
    comment_reaction_counts: List[CommentReactionsCount]
    reply_counts: List[CommentRepliesCount]
    comment_dtos: List[CommentDto]
    post_tag_details: List[PostTagDetailsDto]
    users_dtos: List[UserDto]

@dataclass
class DomainDetailsWithPostsDto:
    domain_details: DomainDetailsDto
    domain_posts: CompletePostDetailsDto