from unittest.mock import create_autospec

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.get_post_interactor import GetPostInteractor
from gyaan.interactors.storages.dtos_v2 import (
    UserDto, PostDto, DomainDto, CommentDto, ReactionDto, TagDto,
    PostDetailsDto, PostCompleteDetailsPresenterDto, PresenterCommentDto,
    PresenterReplyDto
)


def test_get_post_interactor_with_valid_post_id():
    # Arrange
    post_id=1
    user_id=1
    post_dto = PostDto(
        user_id=1,
        post_id=1,
        domain_id=1,
        title="first_post",
        description="first_post",
        posted_at="datetime"
    )
    domain_dto =  DomainDto(
        domain_id=1,
        name="django",
        description="django",
        picture="django.com",
        experts=None,
        members=None
    )
    users_dto = [UserDto(user_id=1, name="user1", profile_pic="user1.com"),
                 UserDto(user_id=2, name="user2", profile_pic="user2.com"),
                 UserDto(user_id=3, name="user3", profile_pic="user3.com")]

    comments_dto = [CommentDto(comment_id=1,content="comment1",user_id=2,
                    is_answer=True,post_id=1,commented_at="datetime",
                    approved_by_id = 1, parent_comment=None),
                    CommentDto(comment_id=2,content="comment2",user_id=3,
                    is_answer=False,post_id=1,commented_at="datetime",
                    approved_by_id = 1, parent_comment=1)]

    approved_answer_dto = CommentDto(comment_id=1,content="comment1",
                                     user_id=2, is_answer=True, post_id=1,
                                     commented_at="datetime",
                                     approved_by_id = 1, parent_comment=None)

    reactions_dto = [ReactionDto(reaction_id=1, post_id=1, comment_id=None,
                     user_id=2)]

    tags_dto = [TagDto(tag_id=1, name="tag1", post_id=1, domain_id=1)]

    post_details_dto = PostDetailsDto(post_dto=post_dto,
                                      domain_dto=domain_dto,
                                      users_dto=users_dto,
                                      comments_dto=comments_dto,
                                      reactions_dto=reactions_dto,
                                      tags_dto=tags_dto
                                      )

    expected_output = PostCompleteDetailsPresenterDto(
        post_details_dto=post_details_dto,
        is_user_reacted=False,
        comments_count=1,
        post_reactions_count=1,
        approved_answer_dto=approved_answer_dto,
        comments_details_dto=[PresenterCommentDto(
            comment_dto=comments_dto[0],
            replies_dto=[PresenterReplyDto(
                        reply_dto=comments_dto[1],
                        reactions_count=0
                        )],
            replies_count=1,
            reactions_count=0
            )]
        )

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetPostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )
    post_storage.get_post_details_dto.return_value = post_details_dto
    post_presenter.get_post_response.return_value = expected_output

    # Act
    actual_output = interactor.get_post(user_id=user_id, post_id=post_id)

    # Assert
    assert actual_output == expected_output

    post_storage.get_post_details_dto.assert_called_once_with(
        post_id=post_id
    )
    post_presenter.get_post_response.assert_called_once_with(
        post_complete_details_dto=expected_output
    )