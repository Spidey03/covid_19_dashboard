from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator

from raven.utils import json

from .validator_class import ValidatorClass

from gyaan.interactors.sign_in_interactor \
    import SignInInteractor
from gyaan.storages.storage_implementation \
    import StorageImplementation
from gyaan.presenters.presenter_implementation \
    import PresenterImplementaion
from common.oauth2_storage import OAuth2SQLStorage
from common.oauth_user_auth_tokens_service import OAuthUserAuthTokensService


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):

    # user = kwargs['user']
    # user_id = user.id
    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']
    print("password, username", password, username)

    storage = StorageImplementation()
    presenter = PresenterImplementaion()
    oauth2_storage = OAuth2SQLStorage()
    interactor = SignInInteractor(
        storage=storage,
        presenter=presenter,
        oauth2_storage=oauth2_storage
    )

    access_token_dict = interactor.sign_in(username=username,
                                           password=password)
    data = json.dumps(access_token_dict)
    response = HttpResponse(data, status=200)

    return response