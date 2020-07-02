import pytest

from gyaan.interactors.storages.dtos import (
    UserDto, CommentDto, DomainDto
)

def get_user_dto():
    user_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    return user_dto


@pytest.fixture()
def comment_dtos():
    comment_dtos = [CommentDto(
        comment_id=1,
        post_id=1,
        content="solution",
        commented_at="datetime",
        parent_comment=None,
        replies_count=10,
        reactions_count=10,
        commented_by=get_user_dto,
        reply_dtos=[]
        )]
    return comment_dtos

@pytest.fixture()
def user_dto():
    user_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    return user_dto

@pytest.fixture()
def domain_dto():
    domain_dto = DomainDto(
        domain_id=1,
        name="Django",
        picture="django.com",
        members_dtos=None,
        request_dtos=None
    )
    return domain_dto




@pytest.fixture()
def get_post_response():
    get_post_response = {
        "post_id": 1,
        "posted_by": {
            "user_id": 1,
            "name": "mahesh",
            "profile_pic": "mahesh.com"
        },
        "title": "First Post",
        "description": "project Gyaan",
        "posted_at": "datetime",
        "tags": ["Gyaan", "Stack"],
        "comments_count": 4,
        "reactions_count": 10,
        "domain": {
            "domain_id": 1,
            "name": "Django",
            "picture": "django.com"
        },
        "is_reacted": True,
        "approved_answer": {
            "comment_id": 1,
            "commented_at": "datetime",
            "commented_by": {
                "user_id": 2,
                "name": "naveen",
                "profile_pic": "naveen.com"
            },
            "reactions_count": 3,
            "replies_count": 2,
            "approved_by": {
                "user_id": 3,
                "name": "ravi",
                "profile_pic": "ravi.com"
            }
        },
        "latest_comments": [
            {
                "comment_id": 2,
                "commented_at": "datetime",
                "content": "solution",
                "commented_by": {
                    "user_id": 3,
                    "name": "ravi",
                    "profile_pic": "ravi.com"
                },
                "reactions_count": 1,
                "replies_count": 0
            }
        ]
    }

    return get_post_response

# gyaan/v2
from gyaan.interactors.storages.dtos_v3 import *

@pytest.fixture
def user_dtos():
    user_dtos = [
        UserDetailsDTO(user_id=1, name="User1",
                       profile_pic_url="user1.com"),
        UserDetailsDTO(user_id=2, name="User2",
                       profile_pic_url="user2.com"),
        UserDetailsDTO(user_id=3, name="User3",
                       profile_pic_url="user3.com")
    ]
    return user_dtos

@pytest.fixture
def post_dtos():
    post_dtos = [
        PostDTO(
            post_id=1,
            posted_at="datetime",
            posted_by_id=1,
            title="Django Post",
            content="django"
        ),
        PostDTO(
            post_id=2,
            posted_at="datetime",
            posted_by_id=1,
            title="Django Post",
            content="django"
        ),
        PostDTO(
            post_id=3,
            posted_at="datetime",
            posted_by_id=2,
            title="Django Post",
            content="django"
        ),
        PostDTO(
            post_id=4,
            posted_at="datetime",
            posted_by_id=2,
            title="Django Post",
            content="django"
        )
    ]
    return post_dtos

@pytest.fixture
def comment_dtos_v2():
    comment_dtos = [
        CommentDTO(
            comment_id=1,
            commented_at="datetime",
            commented_by_id=2,
            content="comment"
        ),
        CommentDTO(
            comment_id=2,
            commented_at="datetime",
            commented_by_id=1,
            content="comment"
        ),
        CommentDTO(
            comment_id=3,
            commented_at="datetime",
            commented_by_id=2,
            content="comment"
        ),
        CommentDTO(
            comment_id=4,
            commented_at="datetime",
            commented_by_id=1,
            content="comment"
        )
    ]
    return comment_dtos

def tag_dtos():
    tag_dtos = [
        Tag(tag_id=1, name="django"),
        Tag(tag_id=2, name="django"),
        Tag(tag_id=3, name="django"),
        Tag(tag_id=4, name="django"),
    ]
    return post_tag_dtos


def post_tag_dtos():
    post_tag_dtos = [
        PostTag(post_id=1, tag_id=1),
        PostTag(post_id=2, tag_id=2),
        PostTag(post_id=3, tag_id=3),
        PostTag(post_id=4, tag_id=4),
    ]
    return post_tag_dtos

@pytest.fixture
def post_tag_details_dtos():
    post_tag_details_dtos =PostTagDetails(
        tags=tag_dtos(),
        post_tag_ids=post_tag_dtos()
    )

    return post_tag_details_dtos

@pytest.fixture
def post_reaction_counts():
    post_reaction_counts = [
        PostReactionsCount(post_id=1,reactions_count=2),
        PostReactionsCount(post_id=2,reactions_count=2),
        PostReactionsCount(post_id=3,reactions_count=0),
        PostReactionsCount(post_id=4,reactions_count=0),
    ]
    return post_reaction_counts

@pytest.fixture
def comment_reaction_counts():
    comment_reaction_counts = [
        CommentReactionsCount(comment_id=1,reactions_count=2),
        CommentReactionsCount(comment_id=2,reactions_count=2),
        CommentReactionsCount(comment_id=3,reactions_count=0),
        CommentReactionsCount(comment_id=4,reactions_count=0),
    ]
    return comment_reaction_counts

@pytest.fixture
def post_comment_counts():
    post_comment_counts = [
        PostCommentsCount(post_id=1,comments_count=2),
        PostCommentsCount(post_id=2,comments_count=2),
        PostCommentsCount(post_id=3,comments_count=0),
        PostCommentsCount(post_id=4,comments_count=0),
    ]
    return post_comment_counts

@pytest.fixture
def comment_replies_counts():
    comment_replies_counts = [
        CommentRepliesCount(comment_id=1,replies_count=2),
        CommentRepliesCount(comment_id=2,replies_count=2),
        CommentRepliesCount(comment_id=3,replies_count=0),
        CommentRepliesCount(comment_id=4,replies_count=0),
    ]
    return comment_replies_counts

@pytest.fixture
def domain_dtos():
    domain_dtos =[
        DomainDTO(
            domain_id=1,
            name="Domain1",
            description="domain1"
        ),
        DomainDTO(
            domain_id=2,
            name="Domain2",
            description="domain2"
        )
    ]
    return domain_dtos

@pytest.fixture
def domain_stats_dtos():
    domain_stats_dtos = [
        DomainStatsDTO(
            domain_id=1,
            followers_count=10,
            posts_count=10,
            bookmarked_count=10
        ),
        DomainStatsDTO(
            domain_id=2,
            followers_count=10,
            posts_count=10,
            bookmarked_count=10
        )
    ]
    return domain_stats_dtos

@pytest.fixture
def domain_join_requests_dtos():
    domain_join_requests_dtos = [
        DomainJoinRequestDTO(
            request_id=1,
            user_id=2
        )
    ]
    return domain_join_requests_dtos