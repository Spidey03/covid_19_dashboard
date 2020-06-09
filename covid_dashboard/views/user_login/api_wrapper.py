from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.login_interactor\
    import LoginUserInteractor
from covid_dashboard.storages.user_storage_implementation\
    import UserStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.exceptions.exceptions\
    import InvalidUserName, InvalidPassword
from covid_dashboard.constants.exception_messages import INVALID_USERNAME, INVALID_PASSWORD


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
    
    # try:
    #     from covid_dashboard.views.user_login.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.user_login.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.user_login.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="user_login",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]