# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "state_get_day_wise_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/day_wise_report/"

from .test_case_01 import TestCase01StateGetDayWiseReportAPITestCase

__all__ = [
    "TestCase01StateGetDayWiseReportAPITestCase"
]
