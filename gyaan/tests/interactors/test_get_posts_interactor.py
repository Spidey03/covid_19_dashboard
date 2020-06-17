import pytest
from mock import create_autospec
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
