from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_report_of_a_state_for_a_date_interactor\
    import GetReportOFStateForDate
from covid_dashboard.storages.state_storage_implementation\
    import StateStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.exceptions.exceptions import InvalidDate
from covid_dashboard.constants.exception_messages import INVALID_DATE


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = StateStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetReportOFStateForDate(
        storage=storage, presenter=presenter)

    request_data = kwargs['request_data']
    query = kwargs['request_query_params']
    date = query['date']
    try:
        response = interactor.get_report_of_state_for_date(
            date=date
        )
    except InvalidDate:
        raise NotFound(*INVALID_DATE)
    data = json.dumps(response)
    return HttpResponse(data, status=200)

    # try:
    #     from covid_dashboard.views.get_report_of_a_state_for_a_date.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.get_report_of_a_state_for_a_date.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.get_report_of_a_state_for_a_date.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="get_report_of_a_state_for_a_date",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]