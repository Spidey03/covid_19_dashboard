import pytest

from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion
from gyaan.interactors.storages.dtos import (
    DomainDto, UserRequestedDomainDto, UserDomainPostDto,
    UserDomainPostMetricsDto, SuggestedDomainDto, UserPostMetricsDto,
    PendingPostMetrics
)

def test_get_user_metrics_with_valid_details(
        user_dto, domain_dto,
        get_user_metrics_response):
    # Arrange
    following_domain_dtos = [domain_dto]
    approved_posts_in_each_domain_dtos = [UserDomainPostDto(
        domain_id=1,
        name="Django",
        picture="django.com",
        posts_count=10
    )]
    pending_posts_in_each_domain_dtos = approved_posts_in_each_domain_dtos

    user_domain_post_metrics_dto = UserDomainPostMetricsDto(
        user_dto=user_dto,
        following_domain_dtos=following_domain_dtos,
        suggested_domain_dtos=[SuggestedDomainDto(
            domain_dto=domain_dto,
            is_requested=True)
        ],
        user_post_metrics_dto=UserPostMetricsDto(
            total_posts=10,
            posts_in_each_domain_dtos=approved_posts_in_each_domain_dtos
        ),
        pending_post_metrics_dto = PendingPostMetrics(
            pending_posts_count=10,
            pending_posts_in_each_domain_dtos=pending_posts_in_each_domain_dtos
        )
        )

    expected_output = get_user_metrics_response
    presenter = PresenterImplementaion()

    # Act
    actual_output = presenter.get_user_metrics_response(
        user_domain_post_metrics_dto=user_domain_post_metrics_dto
    )

    # Assert
    assert actual_output == expected_output