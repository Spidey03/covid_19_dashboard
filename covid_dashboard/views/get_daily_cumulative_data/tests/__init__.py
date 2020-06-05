# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_daily_cumulative_data"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/daily_cumulative_report/v1/"

from .test_case_01 import TestCase01GetDailyCumulativeDataAPITestCase

__all__ = [
    "TestCase01GetDailyCumulativeDataAPITestCase"
]
