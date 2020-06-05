# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_state_wise_daily_cases"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/daily_cases/v1/"

from .test_case_01 import TestCase01GetStateWiseDailyCasesAPITestCase

__all__ = [
    "TestCase01GetStateWiseDailyCasesAPITestCase"
]
