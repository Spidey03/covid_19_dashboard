# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_wise_cumulative_report_of_cases"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/cumulative/v1/"

from .test_case_01 import TestCase01GetStateWiseCumulativeReportOfCasesAPITestCase

__all__ = [
    "TestCase01GetStateWiseCumulativeReportOfCasesAPITestCase"
]
