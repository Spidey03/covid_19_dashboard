import pytest
from mock import create_autospec
from unittest.mock import patch
from gyaan.interactors.get_domain_posts_interactor \
    import GetDomainPostsInteractor
from gyaan.interactors.get_posts_interactor \
    import GetPostsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import DomainDetailsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden


class TestGetDomainPosts():

    def test_when_domain_not_exists_raise_exception_domain_not_exist(self):
        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = 0, 5

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.check_domain_is_valid.side_effect = DomainNotExists
        presenter.raise_domain_does_not_exists.side_effect = NotFound
        interactor = GetDomainPostsInteractor(storage=storage)

        # Act
        with pytest.raises(NotFound):
            interactor.get_domain_posts_wrapper(user_id=user_id,
                domain_id=domain_id, offset=offset, limit=limit,
                presenter=presenter)

        # Assert
        storage.check_domain_is_valid.assert_called_once_with(domain_id=domain_id)

    def test_when_user_is_not_follower_of_domain_raise_exception_user_is_not_follower(self):
        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = 0, 5

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.check_domain_is_valid.return_value = None
        storage.check_user_is_follower_of_domain.return_value = False
        presenter.raise_user_not_follower.side_effect = Forbidden
        interactor = GetDomainPostsInteractor(storage=storage)

        # Act
        with pytest.raises(Forbidden):
            interactor.get_domain_posts_wrapper(user_id=user_id,
                domain_id=domain_id, offset=offset, limit=limit,
                presenter=presenter)

        # Assert
        storage.check_domain_is_valid.assert_called_once_with(domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id=user_id, domain_id=domain_id)

    def test_when_invalid_offset_value_given_raise_exception_invalid_value_for_offset(self):
        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = -1, 5

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.check_domain_is_valid.return_value = None
        storage.check_user_is_follower_of_domain.return_value = True
        presenter.raise_invalid_value_for_offset.side_effect = BadRequest
        interactor = GetDomainPostsInteractor(storage=storage)

        # Act
        with pytest.raises(BadRequest):
            interactor.get_domain_posts_wrapper(user_id=user_id,
                domain_id=domain_id, offset=offset, limit=limit,
                presenter=presenter)

        # Assert
        storage.check_domain_is_valid.assert_called_once_with(domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id=user_id, domain_id=domain_id)

    def test_when_invalid_limit_value_given_raise_exception_invalid_value_for_offset(self):
        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = 5, 2

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.check_domain_is_valid.return_value = None
        storage.check_user_is_follower_of_domain.return_value = True
        presenter.raise_invalid_value_for_limit.side_effect = BadRequest
        interactor = GetDomainPostsInteractor(storage=storage)

        # Act
        with pytest.raises(BadRequest):
            interactor.get_domain_posts_wrapper(user_id=user_id,
                domain_id=domain_id, offset=offset, limit=limit,
                presenter=presenter)

        # Assert
        storage.check_domain_is_valid.assert_called_once_with(domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id=user_id, domain_id=domain_id)

    @patch.object(GetPostsInteractor, 'get_posts')
    def test_when_valid_details_given(self, response_get_posts, post_complete_details):
        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = 0, 5
        expected_output = response_get_posts

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        storage.check_domain_is_valid.return_value = None
        storage.check_user_is_follower_of_domain.return_value = True
        GetPostsInteractor.get_posts.return_value = post_complete_details
        presenter.response_get_posts.return_value = expected_output
        interactor = GetDomainPostsInteractor(storage=storage)

        # Act
        output = interactor.get_domain_posts_wrapper(user_id=user_id,
            domain_id=domain_id, offset=offset, limit=limit,
            presenter=presenter)

        # Assert
        storage.check_domain_is_valid.assert_called_once_with(domain_id=domain_id)
        storage.check_user_is_follower_of_domain.assert_called_once_with(
            user_id=user_id, domain_id=domain_id)
        presenter.response_get_posts.assert_called_once_with(post_complete_details)
        assert output == expected_output
