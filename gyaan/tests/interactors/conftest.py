import pytest
import datetime
from gyaan.interactors.storages.dtos import *

@pytest.fixture()
def domain_dto():
    domain_dto = DomainDto(
        domain_id=1,
        domain_name='CyberSecurity',
        description='CyberSecurity for white hat'
    )
    return domain_dto

@pytest.fixture()
def domain_stats():
    domain_stats = DomainStatDto(
        domain_id=1,
        followers_count=100,
        posts_count=50,
        bookmarked_count=25
    )
    return domain_stats

@pytest.fixture()
def experts():
    users = [
        UserDto(
            user_id=1,
            name="Naveen"
        ),
        UserDto(
            user_id=2,
            name="Codist"
        )
    ]
    return users

@pytest.fixture()
def domain_join_requests():
    domain_join_requests =  [
        DomainJoinRequestDto(
            request_id = 3,
            user_id = 1 
        )
    ]
    return domain_join_requests

@pytest.fixture()
def requested_users():
    requested_users = [
        UserDto(
            user_id=3,
            name="Gwen"
        )
    ]
    return requested_users

@pytest.fixture()
def response_get_domain_details():
    expected_output = {
            "domain_id":1,
            "domain_name":"CyberSecurity",
            "description":"CyberSecurity for white hat",
            "domain_stats":{
                "followers_count":100,
                "posts_count":50,
                "bookmarked_count":25
            },
            "domain_experts":[
                {
                    "user_id":1,
                    "name":"Naveen"
                },
                {
                    "user_id":2,
                    "name":"codist"
                }
            ],
            "requested_users":[
                {
                    "user_id":3,
                    "name":"Gwen"
                }
            ]
        }
    return expected_output


@pytest.fixture()
def posts():
    posts = [
        PostDto(
            post_id=1,
            title="Republic of Gamers",
            content="ROG usually called as Republic of Gamers",
            posted_by=1,
            posted_at=datetime.date(year=2020, month=7, day=16)
        ),
        PostDto(
            post_id=2,
            title="Spiderman PS4",
            content="The realistic graphics of Spiderman game will stun your head",
            posted_by=2,
            posted_at=datetime.date(year=2020, month=2, day=25)
        )
    ]
    return posts

@pytest.fixture()
def comments():
    comments = [
        CommentDto(
            comment_id=1,
            post_id=1,
            content="Awesome Specs",
            commented_by=2,
            commented_at=datetime.date(year=2020, month=7, day=16)
        ),
        CommentDto(
            comment_id=2,
            post_id=2,
            content="It looks very realistic",
            commented_by=1,
            commented_at=datetime.date(year=2020, month=2, day=25)
        )
    ]
    return comments

@pytest.fixture()
def post_reaction_counts():
    post_reaction_counts = [
        PostReactionsCount(
            post_id=1,
            reactions_count=10
        ),
        PostReactionsCount(
            post_id=2,
            reactions_count=5
        )
    ]
    return post_reaction_counts

@pytest.fixture()
def post_comment_counts():
    post_comment_counts = [
        PostCommentsCount(
            post_id=1,
            comments_count=1
        ),
        PostCommentsCount(
            post_id=2,
            comments_count=1
        )
    ]
    return post_comment_counts

@pytest.fixture()
def comment_reaction_counts():
    comment_reaction_counts = [
        CommentReactionsCount(
            comment_id=1,
            reactions_count=10
        ),
        CommentReactionsCount(
            comment_id=2,
            reactions_count=5
        )
    ]
    return comment_reaction_counts

@pytest.fixture()
def comment_replies_count():
    comment_replies_count = [
        CommentRepliesCount(
            comment_id=1,
            replies_count=10
        ),
        CommentRepliesCount(
            comment_id=2,
            replies_count=10
        )
    ]

@pytest.fixture()
def tags():
    tags = [
        TagDto(
            tag_id=1,
            name="Laptops"
        ),
        TagDto(
            tag_id=2,
            name="Games"
        )
    ]
    return tags

@pytest.fixture()
def post_tags():
    post_tags = [
        PostTagDto(
            post_id=1,
            tag_id=1
        ),
        PostTagDto(
            post_id=2,
            tag_id=2
        )
    ]
    return post_tags

@pytest.fixture()
def post_tag_details(tags, post_tags):
    post_tag_details = PostTagDetailsDto(
            tags=tags,
            post_tags=post_tags
        )
    return post_tag_details

@pytest.fixture()
def post_complete_details(posts, comments, post_reaction_counts,
        post_comment_counts,comment_reaction_counts,
        comment_replies_count, tags, post_tags, post_tag_details, experts):

    post_complete_details = CompletePostDetailsDto(
        post_dtos=posts,
        post_reaction_counts=post_reaction_counts,
        comment_counts=post_comment_counts,
        comment_reaction_counts=comment_reaction_counts,
        reply_counts=comment_replies_count,
        comment_dtos=comments,
        post_tag_details=post_tag_details,
        users_dtos=experts
    )
    return post_complete_details

@pytest.fixture()
def domain_details_dto():
    domain_details_dto = DomainDetailsDto(
            domain=domain_dto,
            domain_stats=domain_stats,
            domain_experts=experts,
            user_id=user_id,
            is_user_domain_expert=is_user_domain_expert,
            requested_users_dto=requested_users
        )
    return domain_details_dto

@pytest.fixture()
def response_get_posts():
    expected_output = {
        "posts":[
            {
                "post_id":1,
                "posted_by":"Naveen",
                "posted_at":datetime.date(year=2020, month=7, day=16),
                "title":"Republic of Gamers",
                "content":"ROG usually called as Republic of Gamers",
                "post_tags":[
                    {
                        "tag_id":1,
                        "name":"Laptops"
                    }
                ],
                "post_reactions_count":10,
                "post_comment_counts":1,
                "comments":[
                    {
                        "comment_id":1,
                        "comment_content":"Awesome Specs",
                        "commented_by":{
                            "user_id":2,
                            "name":"Codist"
                        },
                        "commented_at":datetime.date(year=2020, month=7, day=16),
                        "reaction_counts":10,
                        "replies_count":10
                    }
                ]
            },
            {
                "post_id":2,
                "posted_by":"Codist",
                "posted_at":datetime.date(year=2020, month=2, day=25),
                "title":"Spiderman PS4",
                "content":"The realistic graphics of Spiderman game will stun your head",
                "post_tags":[
                    {
                        "tag_id":2,
                        "name":"Games"
                    }
                ],
                "post_reactions_count":5,
                "post_comment_counts":1,
                "comments":[
                    {
                        "comment_id":2,
                        "comment_content":"It looks very realistic",
                        "commented_by":{
                            "user_id":1,
                            "name":"Naveen"
                        },
                        "commented_at":datetime.date(year=2020, month=2, day=25),
                        "reaction_counts":10,
                        "replies_count":10
                    }
                ]
            }
        ]
    }
    return expected_output

@pytest.fixture()
def response_get_domain_details_with_posts(response_get_posts,
        response_get_domain_details):
    expected_output = {
        "domain_details":response_get_domain_details,
        "domain_posts":response_get_posts
    }
    return expected_output