from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_state_wise_cumulative_report_interactor\
    import GetStateWiseCumulativeReport
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.exceptions.exceptions import InvalidDate
from covid_dashboard.constants.exception_messages import INVALID_DATE

@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    # till_date = kwargs['till_date']
    query = kwargs['request_query_params']
    till_date = query['till_date']
    storage = StateStorageImplementation()
    presenter = PresenterImplementation()
    try:
        interactor = GetStateWiseCumulativeReport(storage=storage,
            presenter=presenter)
    except InvalidDate:
        raise BadRequest(*INVALID_DATE)
    
    daily_cumulative_report = interactor.get_state_wise_cumulative_report(
        till_date)
    data = json.dumps(daily_cumulative_report)
    return HttpResponse(data, status=200)
    
    
    # try:
    #     from covid_dashboard.views.get_state_wise_cumulative_report_of_cases.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.get_state_wise_cumulative_report_of_cases.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.get_state_wise_cumulative_report_of_cases.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="get_state_wise_cumulative_report_of_cases",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]