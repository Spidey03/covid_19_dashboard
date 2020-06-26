from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.storages.state_storage_implementation \
    import StateStorageImplementation
from covid_dashboard.presenters.presenter_implementation \
    import PresenterImplementation
from covid_dashboard.interactors.state_get_day_wise_report_interactor \
    import StateGetDaywiseReportInteractor


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    state_id = 1

    storage = StateStorageImplementation()
    presenter = PresenterImplementation()
    interactor = StateGetDaywiseReportInteractor(
        storage=storage)

    state_day_wise_report = interactor.state_get_day_wise_report_wrapper(
        state_id=state_id, presenter=presenter)

    data = json.dumps(state_day_wise_report)
    return HttpResponse(data, status=200)
    # try:
    #     from covid_dashboard.views.state_get_day_wise_report.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.state_get_day_wise_report.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.state_get_day_wise_report.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="state_get_day_wise_report",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]