from dataclasses import dataclass
import datetime

from typing import List, Optional

from gyaan.constants.enums import JoinStatus, PostStatus

@dataclass()
class UserDto:
    user_id: int
    name: str
    profile_pic: str


@dataclass
class DomainDto:
    domain_id: int
    name: str
    description: str
    picture: str
    experts: Optional[List[UserDto]]
    members: Optional[List[UserDto]]

@dataclass()
class ReactionDto:
    reaction_id: int
    post_id: Optional[int]
    comment_id: Optional[int]
    user_id: int

@dataclass()
class CommentDto:
    comment_id: int
    content: str
    user_id: int
    is_answer: bool
    approved_by_id: Optional[int]
    post_id: Optional[int]
    commented_at: datetime
    parent_comment: Optional[int]

@dataclass()
class PostDto:
    user_id: int
    post_id: int
    domain_id: int
    title: str
    description: str
    posted_at: datetime

@dataclass()
class TagDto:
    tag_id: int
    name: str
    post_id: Optional[int]
    domain_id: Optional[int]


# get post dtos from storage

@dataclass
class PostDetailsDto:
    post_dto: PostDto
    domain_dto: DomainDto
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]
    tags_dto: Optional[List[TagDto]]


# get post dtos to presenter

@dataclass()
class PresenterReplyDto:
    reply_dto: CommentDto
    reactions_count: int
    is_user_reacted: bool


@dataclass
class PresenterCommentDto:
    comment_dto: CommentDto
    replies_count: Optional[int]
    reactions_count: int
    replies_dto: List[PresenterReplyDto]
    is_user_reacted: bool


@dataclass
class PostCompleteDetailsPresenterDto:
    post_details_dto: PostDetailsDto
    is_user_reacted: bool
    comments_count: int
    post_reactions_count: int
    approved_answer_dto: Optional[CommentDto]
    comments_details_dto: List[PresenterCommentDto]


# get domain posts dtos from storage

@dataclass
class DomainPostsDetailsDto:
    posts_dto: List[PostDto]
    domains_dto: List[DomainDto]
    users_dto: List[UserDto]
    comments_dto: List[CommentDto]
    reactions_dto: List[ReactionDto]
    tags_dto: Optional[List[TagDto]]

@dataclass
class PostDetailsWithMetricsDto:
    post_id: int
    is_user_reacted: bool
    post_reactions_count: int
    comments_count: int
    approved_answer_dto: Optional[CommentDto]
    parent_comments_with_replies_dto: Optional[List[PresenterCommentDto]]

@dataclass
class PresenterDomainPostsDto:
    domain_posts_details_dto: DomainPostsDetailsDto
    posts_details_with_metrics_dto: List[PostDetailsWithMetricsDto]
