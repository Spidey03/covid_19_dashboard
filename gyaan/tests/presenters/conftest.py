import pytest

from gyaan.interactors.storages.dtos import (
    UserDto, CommentDto, AnswerDto, DomainDto
)

def get_user_dto():
    user_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    return user_dto

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
def comment_dtos():
    comment_dtos = [CommentDto(
        comment_id=1,
        post_id=1,
        commented_by=get_user_dto(),
        content="solution",
        commented_at="datetime",
        parent_comment=None,
        reactions_count=10,
        replies_count=10,
        reply_dtos=[]
    )]
    return comment_dtos

@pytest.fixture()
def answer_dto():
    answer_dto = AnswerDto(
        comment_id=1,
        post_id=1,
        commented_by=get_user_dto(),
        content="solution",
        commented_at="datetime",
        parent_comment=None,
        reactions_count=10,
        replies_count=10,
        approved_by=get_user_dto(),
        reply_dtos=[]
    )
    return answer_dto

@pytest.fixture()
def get_posts_response():
    get_posts_response = [{
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
        "comments_count": 10,
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
            "content": "solution",
            "commented_by": {
                "user_id": 1,
                "name": "mahesh",
                "profile_pic": "mahesh.com"
            },
            "reactions_count": 10,
            "replies_count": 10,
            "replyies": [],
            "approved_by": {
                "user_id": 1,
                "name": "mahesh",
                "profile_pic": "mahesh.com"
            }
        },
        "latest_comments": [
            {
                "comment_id": 1,
                "commented_at": "datetime",
                "content": "solution",
                "commented_by": {
                    "user_id": 1,
                    "name": "mahesh",
                    "profile_pic": "mahesh.com"
                },
                "reactions_count": 10,
                "replies_count": 10,
                "reply_dtos": []
            }
        ]
    }]

    return get_posts_response


@pytest.fixture()
def get_posts_reponse_v2():
    get_posts_reponse_v2 = [{'post_id': 1,
  'posted_by': {'user_id': 1, 'name': 'mahesh', 'profile_pic': 'mahesh.com'},
  'title': 'First Post',
  'description': 'project Gyaan',
  'posted_at': 'datetime',
  'tags': ['Gyaan', 'Stack'],
  'comments_count': 10,
  'reactions_count': 10,
  'domain': {'domain_id': 1, 'name': 'Django', 'picture': 'django.com'},
  'is_reacted': True,
  'latest_comments': [{'comment_id': 1,
    'content': 'solution',
    'commented_at': 'datetime',
    'commented_by': {'user_id': 1,
     'name': 'mahesh',
     'profile_pic': 'mahesh.com'},
    'reactions_count': 10,
    'replies_count': 10,
    'replies': []}],
  'approved_answer': {'comment_id': 1,
   'content': 'solution',
   'commented_at': 'datetime',
   'commented_by': {'user_id': 1,
    'name': 'mahesh',
    'profile_pic': 'mahesh.com'},
   'reactions_count': 10,
   'replies_count': 10,
   'replies': [],
   'approved_by': {'user_id': 1,
    'name': 'mahesh',
    'profile_pic': 'mahesh.com'}}}]
    return get_posts_reponse_v2


@pytest.fixture()
def get_posts_response_with_no_answer():
    get_posts_response_with_no_answer = [{
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
        "comments_count": 10,
        "reactions_count": 10,
        "domain": {
            "domain_id": 1,
            "name": "Django",
            "picture": "django.com"
        },
        "is_reacted": True,
        "approved_answer": None,
        "latest_comments": [
            {
                "comment_id": 1,
                "commented_at": "datetime",
                "content": "solution",
                "commented_by": {
                    "user_id": 1,
                    "name": "mahesh",
                    "profile_pic": "mahesh.com"
                },
                "reactions_count": 10,
                "replies_count": 10
            }
        ]
    }]

    return get_posts_response_with_no_answer

@pytest.fixture
def get_posts_response_with_no_answer_v2():
    get_posts_response_with_no_answer_v2 = [{'post_id': 1,
  'posted_by': {'user_id': 1, 'name': 'mahesh', 'profile_pic': 'mahesh.com'},
  'title': 'First Post',
  'description': 'project Gyaan',
  'posted_at': 'datetime',
  'tags': ['Gyaan', 'Stack'],
  'comments_count': 10,
  'reactions_count': 10,
  'domain': {'domain_id': 1, 'name': 'Django', 'picture': 'django.com'},
  'is_reacted': True,
  'latest_comments': [{'comment_id': 1,
    'content': 'solution',
    'commented_at': 'datetime',
    'commented_by': {'user_id': 1,
     'name': 'mahesh',
     'profile_pic': 'mahesh.com'},
    'reactions_count': 10,
    'replies_count': 10,
    'replies': []}],
  'approved_answer': None}]
    return get_posts_response_with_no_answer_v2


@pytest.fixture
def get_user_metrics_response():
    get_user_metrics_response = {
        "user": {
            "user_id": 1,
            "name": "mahesh",
            "profile_pic": "mahesh.com"
        },
        "following_domains": [
            {
                "domain_id": 1,
                "name": "Django",
                "picture": "django.com"
            }
        ],
        "suggested_domains": [
            {
                "domain_id": 1,
                "name": "Django",
                "picture": "django.com",
                "follow_request": True
            }
        ],
        "user_post_metrics": {
            "total_posts": 10,
            "posts_in_each_domain": [
                {
                    "domain_id": 1,
                    "name": "Django",
                    "picture": "django.com",
                    "posts_count": 10
                }
            ]
        },
        "pending_post_metrics": {
            "total_review_posts": 10,
            "pending_for_review": [
                {
                    "domain_id": 1,
                    "name": "Django",
                    "picture": "django.com",
                    "review_posts_count": 10
                }
            ]
        }
    }
    return get_user_metrics_response


@pytest.fixture
def get_domain_metrics_response():
    response = {
        "domain_id": 1,
        "name": "Django",
        "picture": "django.com",
        "description": "Django Framework",
        "experts": {
            "total_experts": 1,
            "domain_experts": [
                {
                    "user_id": 1,
                    "name": "user1",
                    "profile_pic": "user1.com"
                }
            ]
        },
        "no_of_followers": 10,
        "total_posts": 10,
        "likes": 10,
        "is_following": True,
        "domain_expert_metrics": {
            "post_review_requests": {
                "total_posts": 10,
                "pending_for_review": [
                    {
                        "domain_id": 1,
                        "name": "Django",
                        "picture": "django.com",
                        "review_posts_count": 10
                    }
                ]
            },
            "user_requests": {
                "total_requests": 1,
                "requests": [
                    {
                        "user_id": 1,
                        "name": "user1",
                        "profile_pic": "user1.com"
                    }
                ]
            }
        }
    }
    return response


@pytest.fixture
def get_domain_metrics_response_when_user_is_not_expert():
    response = {
        "domain_id": 1,
        "name": "Django",
        "picture": "django.com",
        "description": "Django Framework",
        "experts": {
            "total_experts": 1,
            "domain_experts": [
                {
                    "user_id": 1,
                    "name": "user1",
                    "profile_pic": "user1.com"
                }
            ]
        },
        "no_of_followers": 10,
        "total_posts": 10,
        "likes": 10,
        "is_following": True,
        "domain_expert_metrics": None
    }
    return response


@pytest.fixture
def get_post_response_dict():
    get_post_presenter = {'post_id': 1,
 'posted_by': {'user_id': 1, 'name': '', 'profile_pic': None},
 'title': 'Django post',
 'description': 'updated',
 'posted_at': '2020-06-02 21:05:18.249700',
 'tags': [],
 'comments_count': 1,
 'reactions_count': 1,
 'domain': {'domain_id': 1, 'name': 'Django', 'picture': 'dkfajh'},
 'is_reacted': True,
 'approved_answer': {'comment_id': 1,
  'content': 'comment to post1',
  'commented_at': '2020-06-04 10:29:00.111781',
  'comemnted_by': {'user_id': 1, 'name': '', 'profile_pic': None},
  'reactions_count': 0,
  'replies_count': 1,
  'replies': [{'comemnt_id': 2,
    'content': 'reply to comment1',
    'commented_at': '2020-06-02 21:05:18.265862',
    'commented_by': {'user_id': 2,
     'name': 'user1',
     'profile_pic': 'user1@abc.com'},
    'reactions_count': 0}],
  'approved_by': {'user_id': 1, 'name': '', 'profile_pic': None}},
 'latest_comments': [{'comment_id': 1,
   'content': 'comment to post1',
   'commented_at': '2020-06-04 10:29:00.111781',
   'comemnted_by': {'user_id': 1, 'name': '', 'profile_pic': None},
   'reactions_count': 0,
   'replies_count': 1,
   'replies': [{'comemnt_id': 2,
     'content': 'reply to comment1',
     'commented_at': '2020-06-02 21:05:18.265862',
     'commented_by': {'user_id': 2,
      'name': 'user1',
      'profile_pic': 'user1@abc.com'},
     'reactions_count': 0}]}]}

    return get_post_presenter

@pytest.fixture
def get_post_response_dict_when_no_answer():
    post_response_dict_when_no_answer = {'post_id': 2,
 'posted_by': {'user_id': 1, 'name': '', 'profile_pic': None},
 'title': 'ORM post',
 'description': 'first',
 'posted_at': '2020-06-02 21:05:18.252871',
 'tags': [],
 'comments_count': 1,
 'reactions_count': 0,
 'domain': {'domain_id': 2, 'name': 'ORM', 'picture': 'dkfajh'},
 'is_reacted': False,
 'approved_answer': None,
 'latest_comments': [{'comment_id': 3,
   'content': 'comment to post2',
   'commented_at': '2020-06-02 21:05:18.269175',
   'comemnted_by': {'user_id': 2,
    'name': 'user1',
    'profile_pic': 'user1@abc.com'},
   'reactions_count': 0,
   'replies_count': 0,
   'replies': []}]}

    return post_response_dict_when_no_answer

@pytest.fixture
def get_post_response_dict_when_no_answer_commetns_reactions():
    post_id_4 = {'post_id': 4,
 'posted_by': {'user_id': 3, 'name': 'user2', 'profile_pic': 'user2@abc.com'},
 'title': 'SQL post',
 'description': 'first',
 'posted_at': '2020-06-02 21:05:18.258924',
 'tags': [],
 'comments_count': 0,
 'reactions_count': 0,
 'domain': {'domain_id': 3, 'name': 'Flask', 'picture': 'dkfajh'},
 'is_reacted': False,
 'approved_answer': None,
 'latest_comments': []}

    return post_id_4