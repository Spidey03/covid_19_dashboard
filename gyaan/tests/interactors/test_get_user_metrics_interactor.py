from unittest.mock import create_autospec

from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.get_user_metrics_interactor import \
    GetUserMetricsInteractor
from gyaan.interactors.storages.dtos import (
    DomainDto, UserRequestedDomainDto, UserDomainPostDto,
    UserDomainPostMetricsDto, SuggestedDomainDto, UserPostMetricsDto,
    PendingPostMetrics
)

def test_get_user_metrics_with_valid_details(
        user_dto, domain_dto):
    # Arrange
    user_id = 1
    post_id = 1
    following_domain_dtos = [domain_dto]
    some_domain_dtos = [domain_dto]
    user_requested_domain_dtos = [UserRequestedDomainDto(
        user_id=1,
        domain_id=1,
        is_requested=True)]
    approved_posts_in_each_domain_dtos = [UserDomainPostDto(
        domain_id=1,
        name="Django",
        picture="django",
        posts_count=10
    )]
    pending_posts_in_each_domain_dtos = approved_posts_in_each_domain_dtos

    expected_output = UserDomainPostMetricsDto(
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
        ),
        )


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserMetricsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.get_user_dto.return_value = user_dto
    storage.get_following_domain_dtos.return_value = following_domain_dtos
    storage.get_some_domain_dtos.return_value = some_domain_dtos
    storage.get_user_requested_domain_dtos.return_value = \
        user_requested_domain_dtos
    storage.get_approved_posts_in_each_domain_dtos.return_value = \
        approved_posts_in_each_domain_dtos
    storage.get_pending_posts_in_each_domain_dtos.return_value = \
        pending_posts_in_each_domain_dtos
    presenter.get_user_metrics_response.return_value = expected_output

    # Act
    actual_output = interactor.get_user_metrcis(user_id=user_id)

    # Assert
    assert actual_output == expected_output

    storage.get_user_dto.assert_called_once_with(user_id=user_id)
    storage.get_following_domain_dtos.assert_called_once_with(user_id=user_id)
    storage.get_some_domain_dtos.assert_called_once()
    storage.get_user_requested_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_approved_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_pending_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    presenter.get_user_metrics_response.assert_called_once_with(
        user_domain_post_metrics_dto=expected_output)


def test_get_user_metrics_with_no_following_domains(
        user_dto, domain_dto):
    # Arrange
    user_id = 1
    post_id = 1
    following_domain_dtos = []
    some_domain_dtos = [domain_dto]
    user_requested_domain_dtos = [UserRequestedDomainDto(
        user_id=1,
        domain_id=1,
        is_requested=True)]
    approved_posts_in_each_domain_dtos = [UserDomainPostDto(
        domain_id=1,
        name="Django",
        picture="django",
        posts_count=10
    )]
    pending_posts_in_each_domain_dtos = approved_posts_in_each_domain_dtos

    expected_output = UserDomainPostMetricsDto(
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
        ),
        )


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserMetricsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.get_user_dto.return_value = user_dto
    storage.get_following_domain_dtos.return_value = following_domain_dtos
    storage.get_some_domain_dtos.return_value = some_domain_dtos
    storage.get_user_requested_domain_dtos.return_value = \
        user_requested_domain_dtos
    storage.get_approved_posts_in_each_domain_dtos.return_value = \
        approved_posts_in_each_domain_dtos
    storage.get_pending_posts_in_each_domain_dtos.return_value = \
        pending_posts_in_each_domain_dtos
    presenter.get_user_metrics_response.return_value = expected_output

    # Act
    actual_output = interactor.get_user_metrcis(user_id=user_id)

    # Assert
    assert actual_output == expected_output

    storage.get_user_dto.assert_called_once_with(user_id=user_id)
    storage.get_following_domain_dtos.assert_called_once_with(user_id=user_id)
    storage.get_some_domain_dtos.assert_called_once()
    storage.get_user_requested_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_approved_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_pending_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    presenter.get_user_metrics_response.assert_called_once_with(
        user_domain_post_metrics_dto=expected_output)

def test_get_user_metrics_with_no_posts_and_no_pending_posts(
        user_dto, domain_dto):

    # Arrange
    user_id = 1
    post_id = 1
    following_domain_dtos = [domain_dto]
    some_domain_dtos = [domain_dto]
    user_requested_domain_dtos = [UserRequestedDomainDto(
        user_id=1,
        domain_id=1,
        is_requested=True)]
    approved_posts_in_each_domain_dtos = []
    pending_posts_in_each_domain_dtos = approved_posts_in_each_domain_dtos

    expected_output = UserDomainPostMetricsDto(
        user_dto=user_dto,
        following_domain_dtos=following_domain_dtos,
        suggested_domain_dtos=[SuggestedDomainDto(
            domain_dto=domain_dto,
            is_requested=True)
        ],
        user_post_metrics_dto=UserPostMetricsDto(
            total_posts=0,
            posts_in_each_domain_dtos=approved_posts_in_each_domain_dtos
        ),
        pending_post_metrics_dto = PendingPostMetrics(
            pending_posts_count=0,
            pending_posts_in_each_domain_dtos=pending_posts_in_each_domain_dtos
        )
        )


    storage = create_autospec(StorageInterface)
    presenter = create_autospec(PresenterInterface)
    interactor = GetUserMetricsInteractor(
        storage=storage,
        presenter=presenter
    )

    storage.get_user_dto.return_value = user_dto
    storage.get_following_domain_dtos.return_value = following_domain_dtos
    storage.get_some_domain_dtos.return_value = some_domain_dtos
    storage.get_user_requested_domain_dtos.return_value = \
        user_requested_domain_dtos
    storage.get_approved_posts_in_each_domain_dtos.return_value = \
        approved_posts_in_each_domain_dtos
    storage.get_pending_posts_in_each_domain_dtos.return_value = \
        pending_posts_in_each_domain_dtos
    presenter.get_user_metrics_response.return_value = expected_output

    # Act
    actual_output = interactor.get_user_metrcis(user_id=user_id)

    # Assert
    assert actual_output == expected_output

    storage.get_user_dto.assert_called_once_with(user_id=user_id)
    storage.get_following_domain_dtos.assert_called_once_with(user_id=user_id)
    storage.get_some_domain_dtos.assert_called_once()
    storage.get_user_requested_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_approved_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    storage.get_pending_posts_in_each_domain_dtos.assert_called_once_with(
        user_id=user_id)
    presenter.get_user_metrics_response.assert_called_once_with(
        user_domain_post_metrics_dto=expected_output)
