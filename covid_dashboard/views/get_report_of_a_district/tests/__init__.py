# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_report_of_a_district"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/v1/"

from .test_case_01 import TestCase01GetReportOfADistrictAPITestCase

__all__ = [
    "TestCase01GetReportOfADistrictAPITestCase"
]
