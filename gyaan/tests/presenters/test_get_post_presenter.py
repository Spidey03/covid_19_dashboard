import pytest

from gyaan.presenters.post_presenter_implementation \
    import PostPresenterImplementation
from gyaan.interactors.storages.dtos_v2 import *

def test_get_post_presenter_wtih_valid_details(get_post_response_dict):
    # Arrange
    post_dto = PostDto(user_id=1,
        post_id=1, domain_id=1, title='Django post',
        description='updated',
        posted_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 249700)
    )

    domain_dto =  DomainDto(domain_id=1, name='Django', description='django',
        picture='dkfajh', experts=None, members=None)

    users_dto = [UserDto(user_id=1, name='', profile_pic=None),
                 UserDto(user_id=1, name='', profile_pic=None),
                 UserDto(user_id=2, name='user1', profile_pic='user1@abc.com')]

    comments_dto = [
        CommentDto(comment_id=1, content='comment to post1', user_id=1,
        is_answer=True, approved_by_id=1, post_id=1,
        commented_at=datetime.datetime(2020, 6, 4, 10, 29, 0, 111781),
        parent_comment=None),
        CommentDto(comment_id=2, content='reply to comment1', user_id=2,
        is_answer=False, approved_by_id=None, post_id=1,
        commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 265862),
        parent_comment=1)
    ]

    approved_answer_dto=CommentDto(comment_id=1, content='comment to post1',
        user_id=1, is_answer=True, approved_by_id=1, post_id=1,
        commented_at=datetime.datetime(2020, 6, 4, 10, 29, 0, 111781),
        parent_comment=None)

    reactions_dto = [ReactionDto(reaction_id=2, post_id=1, comment_id=None,
                     user_id=1)]

    tags_dto = []
    post_details_dto = PostDetailsDto(post_dto=post_dto,
                                      domain_dto=domain_dto,
                                      users_dto=users_dto,
                                      comments_dto=comments_dto,
                                      reactions_dto=reactions_dto,
                                      tags_dto=tags_dto
                                      )

    comments_details_dto=[
        PresenterCommentDto(comment_dto=CommentDto(comment_id=1,
            content='comment to post1', user_id=1, is_answer=True,
            approved_by_id=1, post_id=1,
            commented_at=datetime.datetime(2020, 6, 4, 10, 29, 0, 111781),
            parent_comment=None), replies_count=1, reactions_count=0,
            replies_dto=[PresenterReplyDto(reply_dto=CommentDto(comment_id=2,
                content='reply to comment1', user_id=2, is_answer=False,
                approved_by_id=None, post_id=1,
                commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 265862),
                parent_comment=1), reactions_count=0)])]


    post_complete_details_dto = PostCompleteDetailsPresenterDto(
        post_details_dto=post_details_dto,
        is_user_reacted=True,
        comments_count=1,
        post_reactions_count=1,
        approved_answer_dto=approved_answer_dto,
        comments_details_dto=comments_details_dto
        )

    expected_output = get_post_response_dict

    presenter = PostPresenterImplementation()

    # Act
    actual_output = presenter.get_post_response(post_complete_details_dto)

    # Assert
    assert actual_output == expected_output



def test_get_post_reponse_dict_with_no_approved_answer(
        get_post_response_dict_when_no_answer):
    # Arrange
    post_dto=PostDto(user_id=1, post_id=2, domain_id=2, title='ORM post',
        description='first',
        posted_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 252871)
    )

    domain_dto=DomainDto(domain_id=2, name='ORM', description='ORM',
        picture='dkfajh', experts=None, members=None)

    users_dto=[UserDto(user_id=1, name='', profile_pic=None),
               UserDto(user_id=2, name='user1', profile_pic='user1@abc.com')]

    comments_dto=[CommentDto(
        comment_id=3, content='comment to post2', user_id=2, is_answer=False,
        approved_by_id=None, post_id=2,
        commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 269175),
        parent_comment=None)
    ]

    approved_answer_dto = None

    reactions_dto = []

    tags_dto = []

    post_details_dto = PostDetailsDto(post_dto=post_dto,
                                      domain_dto=domain_dto,
                                      users_dto=users_dto,
                                      comments_dto=comments_dto,
                                      reactions_dto=reactions_dto,
                                      tags_dto=tags_dto
                                      )

    comments_details_dto=[
        PresenterCommentDto(comment_dto=CommentDto(
            comment_id=3, content='comment to post2', user_id=2,
            is_answer=False, approved_by_id=None, post_id=2,
            commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 269175),
            parent_comment=None), replies_count=0, reactions_count=0,
            replies_dto=[]
        )
    ]


    post_complete_details_dto = PostCompleteDetailsPresenterDto(
        post_details_dto=post_details_dto,
        is_user_reacted=False,
        comments_count=1,
        post_reactions_count=0,
        approved_answer_dto=approved_answer_dto,
        comments_details_dto=comments_details_dto
        )

    expected_output = get_post_response_dict_when_no_answer

    presenter = PostPresenterImplementation()

    # Act
    actual_output = presenter.get_post_response(post_complete_details_dto)

    # Assert
    assert actual_output == expected_output


def test_get_post_with_no_answer_no_comments_no_reactions(
        get_post_response_dict_when_no_answer_commetns_reactions):
    # Arrange
    post_dto = PostDto(user_id=3, post_id=4,
        domain_id=3, title='SQL post', description='first',
        posted_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 258924)
    )
    domain_dto=DomainDto(domain_id=3, name='Flask', description='Flask',
                         picture='dkfajh', experts=None, members=None)
    users_dto=[UserDto(user_id=3, name='user2', profile_pic='user2@abc.com')]

    approved_answer_dto = None

    comments_dto = []

    reactions_dto = []

    tags_dto = []

    post_details_dto = PostDetailsDto(post_dto=post_dto,
                                      domain_dto=domain_dto,
                                      users_dto=users_dto,
                                      comments_dto=comments_dto,
                                      reactions_dto=reactions_dto,
                                      tags_dto=tags_dto
                                      )

    post_complete_details_dto = PostCompleteDetailsPresenterDto(
        post_details_dto=post_details_dto,
        is_user_reacted=False,
        comments_count=0,
        post_reactions_count=0,
        approved_answer_dto=approved_answer_dto,
        comments_details_dto=[]
        )

    expected_output = get_post_response_dict_when_no_answer_commetns_reactions

    presenter = PostPresenterImplementation()

    # Act
    actual_output = presenter.get_post_response(post_complete_details_dto)

    # Assert
    assert actual_output == expected_output
