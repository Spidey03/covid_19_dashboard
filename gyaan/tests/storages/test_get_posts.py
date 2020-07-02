import datetime
import pytest

from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.interactors.storages.dtos import (
    GetPostDto, UserDto, DomainDto, CommentDto, AnswerDto
)

@pytest.mark.django_db
def test_get_posts_with_valid_detials(
        create_users, populate_database):
    # Arrange
    user_id = 1
    post_id = 1
    limit = 2
    offset = 0
    expected_output = [GetPostDto(
        post_id=1,
        posted_by=UserDto(user_id=1, name='Mahesh',
                          profile_pic="mahesh@abc.com"),
        title='First post',
        description='first',
        posted_at=datetime.datetime(2020, 5, 29, 20, 59, 9),
        tags=[],
        comments_count=1,
        reactions_count=1,
        domain=DomainDto(
            domain_id=1, name='Django', picture='dkfajh',
            members_dtos=[], request_dtos=[]))]

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_posts(limit, offset)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_latest_comments_with_valid_detials(
        create_users, populate_database):
    # Arrange
    user_id = 1
    post_id = 1
    expected_output = [CommentDto(comment_id=1, post_id=1,
        commented_by=UserDto(user_id=1, name='Mahesh',
                             profile_pic="mahesh@abc.com"),
        content='first comment',
        commented_at=datetime.datetime(2020, 5, 29, 20, 59, 9),
        parent_comment=None, reactions_count=1, replies_count=0,
        reply_dtos=[])]

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_latest_comments(post_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_answer_dto_with_valid_detials(
        create_users, populate_database):
    # Arrange
    user_id = 1
    post_id = 1
    expected_output = AnswerDto(
        comment_id=1, post_id=1,
        commented_by=UserDto(
            user_id=1, name='Mahesh', profile_pic="mahesh@abc.com"),
        content='first comment',
        commented_at=datetime.datetime(2020, 5, 29, 20, 59, 9),
        parent_comment=None, reactions_count=1,
        replies_count=0, approved_by=None, reply_dtos=[])

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_answer_dto(post_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_reaction_status_of_user_to_post_with_valid_detials(
        create_users, populate_database):
    # Arrange
    user_id = 1
    post_id = 1
    expected_output = True

    storage = StorageImplementation()

    # Act
    actual_output = storage.get_reaction_status(user_id, post_id)

    # Assert
    assert actual_output == expected_output
