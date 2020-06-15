# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "state_get_cumulative_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/cumulative/"

from .test_case_01 import TestCase01StateGetCumulativeReportAPITestCase

__all__ = [
    "TestCase01StateGetCumulativeReportAPITestCase"
]
