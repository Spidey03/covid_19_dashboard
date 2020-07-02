from unittest.mock import create_autospec

from gyaan.interactors.storages.post_storage_interface \
    import PostStorageInterface
from gyaan.interactors.presenters.post_presenter_interface \
    import PostPresenterInterface
from gyaan.interactors.get_post_interactor \
    import GetPostInteractor
from gyaan.interactors.get_post_interactor import GetPostInteractor

from gyaan.interactors.storages.dtos_v2 import (
    UserDto, PostDto, DomainDto, CommentDto, ReactionDto, TagDto,
    PostDetailsDto, PostCompleteDetailsPresenterDto, PresenterCommentDto,
    PresenterReplyDto, DomainPostsDetailsDto, PresenterDomainPostsDto,
    PostDetailsWithMetricsDto
)


def test_get_post_interactor_with_valid_post_id():
    # Arrange
    domain_id=1
    user_id=1
    posts_dto = [PostDto(
        user_id=1,
        post_id=1,
        domain_id=1,
        title="first_post",
        description="first_post",
        posted_at="datetime"
    )]
    domains_dto =  [DomainDto(
        domain_id=1,
        name="django",
        description="django",
        picture="django.com",
        experts=None,
        members=None
    )]
    users_dto = [UserDto(user_id=1, name="user1", profile_pic="user1.com"),
                 UserDto(user_id=2, name="user2", profile_pic="user2.com"),
                 UserDto(user_id=3, name="user3", profile_pic="user3.com")]

    comments_dto = [CommentDto(comment_id=1,content="comment1",user_id=2,
                    is_answer=True,post_id=1,commented_at="datetime",
                    parent_comment=None, approved_by_id=1),
                    CommentDto(comment_id=2,content="comment2",user_id=3,
                    is_answer=False,post_id=1,commented_at="datetime",
                    parent_comment=1, approved_by_id=None)]

    reactions_dto = [ReactionDto(reaction_id=1, post_id=1, comment_id=None,
                     user_id=2)]

    tags_dto = [TagDto(tag_id=1, name="tag1", post_id=1, domain_id=1)]

    domain_posts_dto = DomainPostsDetailsDto(posts_dto=posts_dto,
                                      domains_dto=domains_dto,
                                      users_dto=users_dto,
                                      comments_dto=comments_dto,
                                      reactions_dto=reactions_dto,
                                      tags_dto=tags_dto
                                      )

    expected_output = PresenterDomainPostsDto(
        domain_posts_details_dto=domain_posts_dto,
        posts_details_with_metrics_dto=[PostDetailsWithMetricsDto(
            post_id=1,
            is_user_reacted=False,
            post_reactions_count=1,
            approved_answer_dto=CommentDto(comment_id=1,content="comment1",user_id=2,
                    is_answer=True,post_id=1,commented_at="datetime",
                    parent_comment=None, approved_by_id=1),
            comments_count=1,
            parent_comments_with_replies_dto=[
                PresenterCommentDto(
                    comment_dto=comments_dto[0],
                    replies_dto=[PresenterReplyDto(
                                reply_dto=comments_dto[1],
                                reactions_count=0
                    )],
                    replies_count=1,
                    reactions_count=0
            )]
        )]
    )

    post_storage = create_autospec(PostStorageInterface)
    post_presenter = create_autospec(PostPresenterInterface)
    interactor = GetPostInteractor(
        post_storage=post_storage,
        post_presenter=post_presenter
    )

    post_storage.get_domain_posts_details_dto.return_value = domain_posts_dto
    post_presenter.get_domain_posts_response.return_value = expected_output

    # Act
    actual_output = interactor.get_domain_posts(
        user_id=user_id, domain_id=domain_id)

    # Assert
    assert actual_output == expected_output

    post_storage.get_domain_posts_details_dto.assert_called_once_with(
        domain_id=domain_id
    )
    post_presenter.get_domain_posts_response.assert_called_once_with(
        presenter_domain_posts_dto=expected_output
    )
