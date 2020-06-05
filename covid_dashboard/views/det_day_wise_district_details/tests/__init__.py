# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "det_day_wise_district_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/daily_cases/v1/"

from .test_case_01 import TestCase01DetDayWiseDistrictDetailsAPITestCase

__all__ = [
    "TestCase01DetDayWiseDistrictDetailsAPITestCase"
]
