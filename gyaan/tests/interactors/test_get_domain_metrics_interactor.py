from unittest.mock import create_autospec

from gyaan.interactors.storages.domain_storage_interface \
    import DomainStorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.get_domain_metrics_interactor \
    import GetDomainMetricsInteractor
from gyaan.interactors.storages.dtos import (
    DomainDetailsDto, DomainExpertsDetailsDto, UserDto,
    DomainExpertDetailsPresenterDto, PendingPostMetrics,
    UserDomainPostDto, DomainJoinRequestWithCountDto
)


def test_domain_metrics_when_user_is_not_expert():
    # Arrange
    user_id = 1
    domain_id = 1
    domain_details_dto = DomainDetailsDto(
        domain_id=domain_id,
        name="Django",
        description="DjangoWithPython",
        picture="django.com",
        no_of_followers=10,
        total_posts=10,
        likes=10
    )

    domain_expert_details_dto = DomainExpertsDetailsDto(
        total_experts=1,
        domain_experts=[UserDto(
            user_id=2,
            name="user2",
            profile_pic="user2.com"
            )
        ]
    )

    is_user_following_this_domain = False
    post_review_requests_dto = None
    domain_join_request_details_dtos = None

    expected_output = DomainExpertDetailsPresenterDto(
                    domain_details_dto=domain_details_dto,
                    domain_expert_details_dto=domain_expert_details_dto,
                    is_following=is_user_following_this_domain,
                    post_review_requests_dto=None,
                    domain_join_request_details_dtos= \
                        None
                )

    domain_storage = create_autospec(DomainStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetDomainMetricsInteractor(
        domain_storage=domain_storage,
        presenter=presenter
    )

    # domain_storage.get_domain_details_dto.return_value = domain_details_dto
    # domain_storage.get_domain_expert_details_dto.return_value = \
    #     domain_expert_details_dto

    domain_storage.get_domain_details_dto_with_experts_dtos.return_value = \
        domain_details_dto, domain_expert_details_dto
    domain_storage.get_user_status_for_this_domain.return_value = \
        is_user_following_this_domain
    presenter.get_domain_metrics_response.return_value = \
        expected_output

    # Act
    actual_output = interactor.get_domain_metrics(
        domain_id=domain_id, user_id=user_id
    )

    # Assert
    assert actual_output == expected_output

    domain_storage.get_domain_details_dto_with_experts_dtos \
        .assert_called_once_with(
            domain_id=domain_id)
    domain_storage.get_user_status_for_this_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    presenter.get_domain_metrics_response.assert_called_once_with(
        domain_expert_details_presenter_dto=expected_output)

def test_domain_metrics_when_user_is_expert():
    # Arrange
    user_id = 1
    domain_id = 1
    domain_details_dto = DomainDetailsDto(
        domain_id=domain_id,
        name="Django",
        description="DjangoWithPython",
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
    # post_review_requests_dto = PendingPostMetrics(
    #     pending_posts_count=10,
    #     pending_posts_in_each_domain_dtos=[
    #         UserDomainPostDto(
    #             domain_id=1,
    #             name="Django",
    #             picture="django.com",
    #             posts_count=10
    #         )
    #     ]
    # )

    post_review_requests_dto = [
            UserDomainPostDto(
                domain_id=1,
                name="Django",
                picture="django.com",
                posts_count=10
            )
        ]

    domain_join_request_details_dtos = [UserDto(
        user_id=2,
        name="user2",
        profile_pic="user2.com"
        )
    ]


    expected_output = DomainExpertDetailsPresenterDto(
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

    domain_storage = create_autospec(DomainStorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetDomainMetricsInteractor(
        domain_storage=domain_storage,
        presenter=presenter
    )

    # domain_storage.get_domain_details_dto.return_value = domain_details_dto
    # domain_storage.get_domain_expert_details_dto.return_value = \
    #     domain_expert_details_dto

    domain_storage.get_domain_details_dto_with_experts_dtos.return_value = \
        domain_details_dto, domain_expert_details_dto
    domain_storage.get_user_status_for_this_domain.return_value = \
        is_user_following_this_domain
    domain_storage.get_post_review_requests_by_domain.return_value = \
        post_review_requests_dto
    domain_storage.get_domain_join_request_dtos.return_value = \
        domain_join_request_details_dtos
    presenter.get_domain_metrics_response.return_value = \
        expected_output

    # Act
    actual_output = interactor.get_domain_metrics(
        domain_id=domain_id, user_id=user_id
    )

    # Assert
    assert actual_output == expected_output

    domain_storage.get_domain_details_dto_with_experts_dtos \
        .assert_called_once_with(
            domain_id=domain_id)
    domain_storage.get_user_status_for_this_domain.assert_called_once_with(
        user_id=user_id, domain_id=domain_id)
    domain_storage.get_post_review_requests_by_domain.assert_called_once_with(
        user_id=user_id)
    domain_storage.get_domain_join_request_dtos.assert_called_once_with(
        domain_id=domain_id)

    presenter.get_domain_metrics_response.assert_called_once_with(
        domain_expert_details_presenter_dto=expected_output)
