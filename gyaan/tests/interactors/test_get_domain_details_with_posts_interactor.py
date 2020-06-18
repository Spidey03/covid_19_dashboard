import pytest
from mock import create_autospec
from unittest.mock import patch
from gyaan.interactors.get_domain_details_interactor \
    import GetDomainDetailsInteractor
from gyaan.interactors.get_domain_posts_interactor \
    import GetDomainPostsInteractor
from gyaan.interactors.get_domain_details_with_posts_interactor \
    import GetDomainDetailsWithPostsInteractor
from gyaan.interactors.storages.storage_interface \
    import StorageInterface
from gyaan.interactors.presenters.presenter_interface \
    import PresenterInterface
from gyaan.interactors.storages.dtos import DomainDetailsWithPostsDto
from gyaan.exceptions.exceptions \
    import DomainNotExists, UserIsNotFollwerOfDomain
from django_swagger_utils.drf_server.exceptions \
    import NotFound, BadRequest, Forbidden


class TestGetDomainDetailsWithPosts:

    @patch.object(GetDomainPostsInteractor, 'get_domain_posts')
    @patch.object(GetDomainDetailsInteractor, 'get_domain_details')
    def test_with_valid_details(self, post_complete_details,
            domain_details_dto, response_get_domain_details_with_posts):

        # Arrange
        user_id, domain_id = 5, 3
        offset, limit = 0, 5
        expected_output = response_get_domain_details_with_posts

        domain_details_with_posts_dto = DomainDetailsWithPostsDto(
            domain_details=domain_details_dto,
            domain_posts=post_complete_details
        )

        storage = create_autospec(StorageInterface)
        presenter = create_autospec(PresenterInterface)

        GetDomainDetailsInteractor.get_domain_details.return_value = \
            domain_details_dto
        GetDomainPostsInteractor.get_domain_posts.return_value = \
            post_complete_details
        presenter.response_get_domain_details_with_posts.return_value = \
            expected_output
        interactor = GetDomainDetailsWithPostsInteractor(storage=storage)

        # Act
        output = interactor.get_domain_details_with_posts_wrapper(
            user_id=user_id, domain_id=domain_id,
            offset=offset, limit=limit, presenter=presenter)

        # Assert
        assert output == expected_output
