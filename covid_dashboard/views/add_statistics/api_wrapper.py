from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.add_new_statistics_interactor\
    import AddNewStatistics
from covid_dashboard.storages.mandal_storage_implementation\
    import MandalStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from common.oauth2_storage import OAuth2SQLStorage
from covid_dashboard.exceptions.exceptions\
    import (InvalidDetailsForTotalConfirmed,
            InvalidDetailsForTotalDeaths,
            InvalidDetailsForTotalRecovered,
            InvalidMandalId, InvalidStatsDetails,
            DetailsAlreadyExist
           )
from covid_dashboard.constants.exception_messages\
    import (INVALID_TOTAL_CONFIRMED, INVALID_TOTAL_DEATHS,
            INVALID_TOTAL_RECOVERED, DETAILS_ALREADY_EXIST)


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    request_data = kwargs['request_data']
    mandal_id = request_data['mandal_id']
    date = request_data['date']
    total_confirmed = request_data['total_confirmed']
    total_deaths = request_data['total_deaths']
    total_recovered = request_data['total_recovered']

    storage = MandalStorageImplementation()
    presenter = PresenterImplementation()
    
    interactor = AddNewStatistics(storage=storage, presenter=presenter)
    try:
        interactor.add_new_statistics(mandal_id=mandal_id,
            date=date, total_confirmed=total_confirmed,
            total_deaths=total_deaths,
            total_recovered=total_recovered)
    except InvalidDetailsForTotalConfirmed:
        raise BadRequest(*INVALID_TOTAL_CONFIRMED)
    except InvalidDetailsForTotalDeaths:
        raise BadRequest(*INVALID_TOTAL_DEATHS)
    except InvalidDetailsForTotalRecovered:
        raise BadRequest(*INVALID_TOTAL_RECOVERED)
    except DetailsAlreadyExist:
        raise BadRequest(*DETAILS_ALREADY_EXIST)

    return HttpResponse(status=200)

    # try:
    #     from covid_dashboard.views.add_statistics.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.add_statistics.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.add_statistics.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="add_statistics",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]