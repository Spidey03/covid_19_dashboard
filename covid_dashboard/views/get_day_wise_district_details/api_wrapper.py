from raven.utils import json
from django.http import HttpResponse
from django_swagger_utils.drf_server.exceptions import BadRequest, NotFound
from django_swagger_utils.drf_server.utils.decorator.interface_decorator \
    import validate_decorator
from .validator_class import ValidatorClass
from covid_dashboard.interactors.get_day_wise_district_details_interactor\
    import GetDayWiseDistrictDetails
from covid_dashboard.storages.district_storage_implementation\
    import DistrictStorageImplementation
from covid_dashboard.presenters.covid_presenter_implementation\
    import PresenterImplementation
from covid_dashboard.exceptions.exceptions import InvalidDistrictId
from covid_dashboard.constants.exception_messages import INVALID_DISTRICT_ID


@validate_decorator(validator_class=ValidatorClass)
def api_wrapper(*args, **kwargs):
    # ---------MOCK IMPLEMENTATION---------

    storage = DistrictStorageImplementation()
    presenter = PresenterImplementation()
    interactor = GetDayWiseDistrictDetails(
        storage=storage, presenter=presenter)

    request_data = kwargs['request_data']
    district_id = kwargs['district_id']
    print(district_id)
    try:
        response = interactor.get_day_wise_district_details(
            district_id=district_id)
    except InvalidDistrictId:
        raise NotFound(*INVALID_DISTRICT_ID)

    data = json.dumps(response)
    response = HttpResponse(data, status=200)
    return response


    # try:
    #     from covid_dashboard.views.get_day_wise_district_details.tests.test_case_01 \
    #         import TEST_CASE as test_case
    # except ImportError:
    #     from covid_dashboard.views.get_day_wise_district_details.tests.test_case_01 \
    #         import test_case

    # from django_swagger_utils.drf_server.utils.server_gen.mock_response \
    #     import mock_response
    # try:
    #     from covid_dashboard.views.get_day_wise_district_details.request_response_mocks \
    #         import RESPONSE_200_JSON
    # except ImportError:
    #     RESPONSE_200_JSON = ''
    # response_tuple = mock_response(
    #     app_name="covid_dashboard", test_case=test_case,
    #     operation_name="get_day_wise_district_details",
    #     kwargs=kwargs, default_response_body=RESPONSE_200_JSON,
    #     group_name="")
    # return response_tuple[1]