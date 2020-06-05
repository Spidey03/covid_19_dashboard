from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_statistics_interactor\
    import GetStatistics
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.exceptions.exceptions\
    import (InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId, InvalidStatsDetails, StatNotFound
           )
from covid_dashboard.constants.exception_messages import (INVALID_MANDAL_ID)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs['request_data']
    mandal_id = request_data['mandal_id']
    
    storage = MandalStorageImplementation()
    presenter = PresenterImplementation()
    
    interactor = GetStatistics(storage=storage, presenter=presenter)
    try:
        response = interactor.get_statistics(mandal_id=mandal_id)
    except InvalidMandalId:
        raise NotFound(*INVALID_MANDAL_ID)
    data = json.dumps(response)
    return HttpResponse(data, status=200)
    
    # try:
    #     interactor.update_statistics(mandal_id=mandal_id,
    #         date=date, total_confirmed=total_confirmed,
    #         total_deaths=total_deaths,
    #         total_recovered=total_recovered)
    # except InvalidDetailsForTotalConfirmed:
    #     raise BadRequest(*INVALID_TOTAL_CONFIRMED)
    # except InvalidDetailsForTotalDeaths:
    #     raise BadRequest(*INVALID_TOTAL_DEATHS)
    # except InvalidDetailsForTotalRecovered:
    #     raise BadRequest(*INVALID_TOTAL_RECOVERED)
    # except StatNotFound:
    #     raise BadRequest(*DETAILS_NOT_FOUND)
    # return HttpResponse(status=200)
    # try:
    #     from covid_dashboard.views.get_reports_of_mandal.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.get_reports_of_mandal.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.get_reports_of_mandal.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="get_reports_of_mandal",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]