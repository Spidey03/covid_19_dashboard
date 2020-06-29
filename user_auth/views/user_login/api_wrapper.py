from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from user_auth.interactors.login_interactor\
    import LoginUserInteractor
from user_auth.storages.user_storage_implementation\
    import UserStorageImplementation
from user_auth.presenters.presenter_implementation\
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from user_auth.constants.exception_messages import INVALID_USERNAME, INVALID_PASSWORD


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    
    interactor = LoginUserInteractor(storage=storage,
        presenter=presenter, oauth_storage=oauth_storage)
    
    try:
        access_token_response = interactor.login_user(
            username=username, password=password)
    except InvalidUserName:
        raise NotFound(*INVALID_USERNAME)
    except InvalidPassword:
        raise NotFound(*INVALID_PASSWORD)
    data = json.dumps(access_token_response)
    return HttpResponse(data, 200)
    