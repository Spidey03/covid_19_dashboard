from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_district_report_of_specific_day_interactor\
    import GetDistrictReportOfSpecificDay
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.exceptions.exceptions import InvalidDistrictId, InvalidDate
from covid_dashboard.constants.exception_messages\
    import INVALID_DISTRICT_ID, INVALID_DATE


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = DistrictStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetDistrictReportOfSpecificDay(
        storage=storage, presenter=presenter)

    request_data = kwargs['request_data']
    district_id = kwargs['district_id']
    query = kwargs['request_query_params']
    date = query['date']

    try:
        response = interactor.get_district_report_of_specific_day(
            date=date, district_id=district_id
        )
    except InvalidDistrictId:
        raise NotFound(*INVALID_DISTRICT_ID)
    except InvalidDate:
        raise BadRequest(*INVALID_DATE)
    data = json.dumps(response)
    return HttpResponse(data, status=200)
    # try:
    #     from covid_dashboard.views.get_report_of_a_district.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.get_report_of_a_district.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.get_report_of_a_district.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="get_report_of_a_district",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]