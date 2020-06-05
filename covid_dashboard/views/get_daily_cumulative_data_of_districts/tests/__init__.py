# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_daily_cumulative_data_of_districts"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/daily_cumulative_report/v1/"

from .test_case_01 import TestCase01GetDailyCumulativeDataOfDistrictsAPITestCase

__all__ = [
    "TestCase01GetDailyCumulativeDataOfDistrictsAPITestCase"
]
