import pytest

from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion
from gyaan.interactors.storages.dtos import (
    DomainJoinRequestWithCountDto, DomainExpertDetailsPresenterDto,UserDto,
    UserDomainPostDto, PendingPostMetrics, DomainExpertsDetailsDto,
    DomainDetailsDto
)

def test_get_domain_metrics_with_valid_details(
        get_domain_metrics_response):
    domain_id = 1
    domain_details_dto = DomainDetailsDto(
        domain_id=domain_id,
        name="Django",
        description="Django Framework",
        picture="django.com",
        no_of_followers=10,
        total_posts=10,
        likes=10
    )

    domain_expert_details_dto = DomainExpertsDetailsDto(
        total_experts=1,
        domain_experts=[UserDto(
            user_id=1,
            name="user1",
            profile_pic="user1.com"
            )
        ]
    )

    is_user_following_this_domain = True
    post_review_requests_dto = PendingPostMetrics(
        pending_posts_count=10,
        pending_posts_in_each_domain_dtos=[
            UserDomainPostDto(
                domain_id=1,
                name="Django",
                picture="django.com",
                posts_count=10
            )
        ]
    )

    domain_join_request_details_dtos = [UserDto(
        user_id=1,
        name="user1",
        profile_pic="user1.com"
        )
    ]


    domain_expert_details_presenter_dto = DomainExpertDetailsPresenterDto(
                    domain_details_dto=domain_details_dto,
                    domain_expert_details_dto=domain_expert_details_dto,
                    is_following=is_user_following_this_domain,
                    post_review_requests_dto=post_review_requests_dto,
                    domain_join_request_details_dtos= \
                        DomainJoinRequestWithCountDto(
                            requests_count=1,
                            domain_join_request_dtos= \
                            domain_join_request_details_dtos
                        )
                    )

    presenter = PresenterImplementaion()
    expected_output = get_domain_metrics_response

    # Act
    actual_output = presenter.get_domain_metrics_response(
        domain_expert_details_presenter_dto=domain_expert_details_presenter_dto)

    # Assert
    assert actual_output == expected_output


def test_get_domain_metrics_when_user_is_not_expert(
        get_domain_metrics_response_when_user_is_not_expert):
    # Arrange
    domain_id = 1
    domain_details_dto = DomainDetailsDto(
        domain_id=domain_id,
        name="Django",
        description="Django Framework",
        picture="django.com",
        no_of_followers=10,
        total_posts=10,
        likes=10
    )

    domain_expert_details_dto = DomainExpertsDetailsDto(
        total_experts=1,
        domain_experts=[UserDto(
            user_id=1,
            name="user1",
            profile_pic="user1.com"
            )
        ]
    )

    is_user_following_this_domain = True
    post_review_requests_dto = PendingPostMetrics(
        pending_posts_count=10,
        pending_posts_in_each_domain_dtos=[
            UserDomainPostDto(
                domain_id=1,
                name="Django",
                picture="django.com",
                posts_count=10
            )
        ]
    )

    domain_join_request_details_dtos = [UserDto(
        user_id=1,
        name="user1",
        profile_pic="user1.com"
        )
    ]


    domain_expert_details_presenter_dto = DomainExpertDetailsPresenterDto(
                    domain_details_dto=domain_details_dto,
                    domain_expert_details_dto=domain_expert_details_dto,
                    is_following=is_user_following_this_domain,
                    post_review_requests_dto=None,
                    domain_join_request_details_dtos= None
                    )

    presenter = PresenterImplementaion()
    expected_output = get_domain_metrics_response_when_user_is_not_expert

    # Act
    actual_output = presenter.get_domain_metrics_response(
        domain_expert_details_presenter_dto=domain_expert_details_presenter_dto)

    # Assert
    assert actual_output == expected_output