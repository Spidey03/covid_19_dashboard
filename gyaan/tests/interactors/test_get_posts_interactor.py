from unittest.mock import create_autospec

from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.get_posts_interactor import GetPostsInteractor
from gyaan.interactors.storages.dtos import (
    GetPostDto, UserDto, DomainDto, PostsCompleteDto, GetPostCompleteDetailsDto
)

def test_get_posts_interactor(get_post_response, comment_dtos):
    # Arrange
    user_id = 1
    limit = 1
    offset = 0
    post_id = 1
    posted_by_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    post_domain_dto = DomainDto(
        domain_id=1,
        name="Django",
        picture="django.com",
        members_dtos=[],
        request_dtos=[]
    )
    get_post_dto = GetPostDto(
        post_id=1,
        posted_by=posted_by_dto,
        title="First Post",
        description="project Gyaan",
        posted_at="datetime",
        tags=["Gyaan", "Stack"],
        comments_count=4,
        reactions_count=10,
        domain=post_domain_dto
    )
    answer_dto = comment_dtos[0]
    reaction_status = True
    all_posts_complete_dto = PostsCompleteDto(
        [
        GetPostCompleteDetailsDto(
            post_dto=get_post_dto,
            comment_dtos=comment_dtos,
            answer_dto=answer_dto,
            is_reacted=reaction_status
            )
        ]
    )

    # all_posts_complete_dto = [
    #     GetPostCompleteDetailsDto(
    #         post_dto=get_post_dto,
    #         comment_dtos=comment_dtos,
    #         answer_dto=answer_dto,
    #         is_reacted=reaction_status
    #         )
    #     ]

    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetPostsInteractor(
        storage=storage,
        presenter=presenter
    )
    storage.get_posts.return_value = [get_post_dto]
    storage.get_latest_comments.return_value = comment_dtos
    storage.get_answer_dto.return_value = answer_dto
    storage.get_reaction_status.return_value = True
    presenter.get_posts_response.return_value = all_posts_complete_dto


    # Act
    actual_output = interactor.get_posts(
        limit=limit, offset=offset, user_id=user_id)

    # Assert
    assert actual_output == all_posts_complete_dto

    #storage.get_posts.return_value.assert_called_once()
    storage.get_latest_comments.assert_called_once_with(post_id=post_id)
    storage.get_answer_dto.assert_called_once_with(post_id=post_id)
    storage.get_reaction_status.assert_called_once_with(user_id=user_id,
        post_id=post_id)
    presenter.get_posts_response.assert_called_once_with(
        all_posts_details_dto=all_posts_complete_dto)
