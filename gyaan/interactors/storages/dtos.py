from dataclasses import dataclass
import datetime

from typing import List, Optional

from gyaan.constants.enums import JoinStatus, PostStatus

@dataclass
class UserDto:
    user_id: int
    name: str
    profile_pic: str

@dataclass
class MembersDto:
    user_id: int
    domain_id: int

@dataclass
class DomainRequestDto:
    user_id: int
    domain_id: int
    status: JoinStatus

# storage
@dataclass
class DomainDto:
    domain_id: int
    name: str
    picture: str
    members_dtos: Optional[List[MembersDto]]
    request_dtos: Optional[List[DomainRequestDto]]

# # storage
# @dataclass
# class DomainListDto:
#     domain_dtos: List[DomainDto]

@dataclass
class FollowingDomainDto:
    domain_id: int
    name: str
    profile_pic: str

# @dataclass
# class SuggestedDomainDto:
#     domain_id: int
#     name: str
#     profile_pic: str
#     follow_request: bool

# storage
@dataclass
class PostDto:
    post_id: int
    domain_id: Optional[int]
    domain: Optional[DomainDto]
    user_id: int
    title: str
    description: str
    status: PostStatus
    is_approved: bool
    approved_by: UserDto

# storage
@dataclass
class UserMetricsDto:
    user_dto: UserDto
    post_dtos: List[PostDto]
    domain_dtos: List[DomainDto]

@dataclass
class DomainPostDto:
    post_id: int
    domain_id: int
    name: str
    picture: str


# storage
@dataclass
class UserDomainPostDto:
    domain_id: int
    name: str
    picture: str
    posts_count: int

@dataclass
class UserPostMetricsDto:
    total_posts: int
    posts_in_each_domain_dtos: List[UserDomainPostDto]

@dataclass
class PendingPostMetrics:
    pending_posts_count: int
    pending_posts_in_each_domain_dtos: List[UserDomainPostDto]

@dataclass
class ReplyCommentDto:
    comment_id: int
    post_id: int
    commented_by: UserDto
    content: str
    commented_at: datetime
    reactions_count: int



@dataclass
class CommentDto:
    comment_id: int
    post_id: int
    commented_by: UserDto
    content: str
    commented_at: datetime
    parent_comment: Optional[int]
    reactions_count: int
    replies_count: int
    reply_dtos: List[ReplyCommentDto]

@dataclass
class AnswerDto:
    comment_id: int
    post_id: int
    commented_by: UserDto
    content: str
    commented_at: datetime
    parent_comment: Optional[int]
    reactions_count: int
    replies_count: int
    approved_by: Optional[UserDto]
    reply_dtos: List[ReplyCommentDto]


@dataclass
class GetPostCompleteDetailsDto:
    post_dto: PostDto
    comment_dtos: List[CommentDto]
    answer_dto: AnswerDto
    is_reacted: bool

@dataclass
class PostsCompleteDto:
    posts_dtos: List[GetPostCompleteDetailsDto]


@dataclass
class GetPostDto:
    post_id: int
    posted_by: UserDto
    title: str
    description: str
    posted_at: datetime
    tags: List[str]
    comments_count: int
    reactions_count: int
    domain : DomainDto

@dataclass
class UserRequestedDomainDto:
    user_id: int
    domain_id: int
    is_requested: bool

@dataclass
class SuggestedDomainDto:
    domain_dto: DomainDto
    is_requested: bool

@dataclass
class UserDomainPostMetricsDto:
    user_dto: UserDto
    following_domain_dtos: List[DomainDto]
    suggested_domain_dtos: List[SuggestedDomainDto]
    user_post_metrics_dto: List[UserPostMetricsDto]
    pending_post_metrics_dto: List[PendingPostMetrics]



# domain metrics dtos
@dataclass
class DomainDetailsDto:
    domain_id: int
    name: str
    description: str
    picture: str
    no_of_followers: int
    total_posts: int
    likes: int

@dataclass
class DomainExpertsDetailsDto:
    total_experts: int
    domain_experts: List[UserDto]


@dataclass
class DomainJoinRequestDto:
    domain_join_request_dto: List[UserDto]

@dataclass
class DomainJoinRequestWithCountDto:
    requests_count: int
    domain_join_request_dtos: List[UserDto]


@dataclass
class DomainExpertDetailsPresenterDto:
    domain_details_dto: DomainDetailsDto
    domain_expert_details_dto: List[DomainExpertsDetailsDto]
    is_following: bool
    post_review_requests_dto: Optional[PendingPostMetrics]
    domain_join_request_details_dtos: Optional[DomainJoinRequestWithCountDto]
