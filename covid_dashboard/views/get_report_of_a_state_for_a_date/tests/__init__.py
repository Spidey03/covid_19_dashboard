# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_report_of_a_state_for_a_date"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/v1/"

from .test_case_01 import TestCase01GetReportOfAStateForADateAPITestCase

__all__ = [
    "TestCase01GetReportOfAStateForADateAPITestCase"
]
