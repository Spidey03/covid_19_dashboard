from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.storages.user_storage_implementation \
    import UserStorageImplementation
from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation
from covid_dashboard.interactors.log_in_interactor \
    import LogInInteractor
from common.oauth2_storage import OAuth2SQLStorage


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = UserStorageImplementation()
    presenter = PresenterImplementation()
    oauth_storage = OAuth2SQLStorage()
    interactor = LogInInteractor(storage=storage, oauth_storage=oauth_storage)

    request_data = kwargs['request_data']
    username = request_data['username']
    password = request_data['password']

    access_token = \
        interactor.login_wrapper(username=username, password=password,
            presenter=presenter)

    data = json.dumps(access_token)
    return HttpResponse(data, status=200)
    # try:
    #     from covid_dashboard.views.log_in.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.log_in.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.log_in.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="log_in",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]