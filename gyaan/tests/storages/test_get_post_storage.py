import datetime
import pytest

from gyaan.storages.post_storage_implementation \
    import PostStorageImplementation
from gyaan.interactors.storages.dtos_v2 import *

@pytest.mark.django_db
def test_get_post_with_valid_details(populate_database_v2):
    # Arrange
    post_id = 1

    post_dto = PostDto(
        user_id=1, post_id=1, domain_id=1,
        title='Django post', description='updated',
        posted_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 249700))

    domain_dto = DomainDto(domain_id=1, name='Django',
                           description='django', picture='dkfajh',
                           experts=None, members=None)

    users_dto = [UserDto(user_id=1, name='', profile_pic=None),
                 UserDto(user_id=1, name='', profile_pic=None),
                 UserDto(user_id=2, name='user1', profile_pic='user1@abc.com')
                 ]

    comments_dto = [
        CommentDto(
            comment_id=1, content='comment to post1', user_id=1,
            is_answer=True, approved_by_id=None, post_id=1,
            commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 262170),
            parent_comment=None),
        CommentDto(
            comment_id=2, content='reply to comment1', user_id=2,
            is_answer=False, approved_by_id=None, post_id=1,
            commented_at=datetime.datetime(2020, 6, 2, 21, 5, 18, 265862),
            parent_comment=1)]

    reactions_dto=[ReactionDto(
        reaction_id=2, post_id=1, comment_id=None, user_id=1)]
    tags_dto=[]

    expected_output = PostDetailsDto(
        post_dto=post_dto,
        domain_dto=domain_dto,
        users_dto=users_dto,
        comments_dto=comments_dto,
        reactions_dto=reactions_dto,
        tags_dto=tags_dto
    )

    post_storage = PostStorageImplementation()

    # Act
    actual_output = post_storage.get_post_details_dto(post_id=post_id)

    # Assert
    assert actual_output == expected_output


@pytest.mark.django_db
def test_get_post_details_with_no_comments_no_reactions(

    ):
    pass