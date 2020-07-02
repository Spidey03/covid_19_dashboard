import pytest

from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion
from gyaan.interactors.storages.dtos import (
    GetPostDto, UserDto, DomainDto, PostsCompleteDto, GetPostCompleteDetailsDto
)


def test_get_posts_response(comment_dtos, get_posts_reponse_v2, answer_dto):
    # Arrange
    user_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    domain_dto = DomainDto(
        domain_id=1,
        name="Django",
        picture="django.com",
        members_dtos=None,
        request_dtos=None
    )
    post_dto = GetPostDto(
        post_id=1,
        posted_by=user_dto,
        title="First Post",
        description="project Gyaan",
        posted_at="datetime",
        tags=["Gyaan", "Stack"],
        comments_count=10,
        reactions_count=10,
        domain=domain_dto
    )
    reaction_status = True

    all_posts_complete_dto = PostsCompleteDto(
        posts_dtos=[
            GetPostCompleteDetailsDto(
            post_dto=post_dto,
            comment_dtos=comment_dtos,
            answer_dto=answer_dto,
            is_reacted=reaction_status
            )
        ]
    )

    expected_output = get_posts_reponse_v2
    presenter = PresenterImplementaion()

    # Act
    actual_output = presenter.get_posts_response(all_posts_complete_dto)

    # Assert
    assert actual_output == expected_output


def test_get_posts_response_with_no_answer(comment_dtos,
        get_posts_response_with_no_answer_v2):
    # Arrange
    user_dto = UserDto(
        user_id=1,
        name="mahesh",
        profile_pic="mahesh.com"
    )
    domain_dto = DomainDto(
        domain_id=1,
        name="Django",
        picture="django.com",
        members_dtos=None,
        request_dtos=None
    )
    post_dto = GetPostDto(
        post_id=1,
        posted_by=user_dto,
        title="First Post",
        description="project Gyaan",
        posted_at="datetime",
        tags=["Gyaan", "Stack"],
        comments_count=10,
        reactions_count=10,
        domain=domain_dto
    )
    reaction_status = True
    answer_dto = None

    all_posts_complete_dto = PostsCompleteDto(
        posts_dtos=[
            GetPostCompleteDetailsDto(
            post_dto=post_dto,
            comment_dtos=comment_dtos,
            answer_dto=answer_dto,
            is_reacted=reaction_status
            )
        ]
    )

    expected_output = get_posts_response_with_no_answer_v2
    presenter = PresenterImplementaion()

    # Act
    actual_output = presenter.get_posts_response(all_posts_complete_dto)

    # Assert
    assert actual_output == expected_output