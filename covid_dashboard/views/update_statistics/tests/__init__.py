# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "update_statistics"
REQUEST_METHOD = "put"
URL_SUFFIX = "stats/update/v1/"

from .test_case_01 import TestCase01UpdateStatisticsAPITestCase

__all__ = [
    "TestCase01UpdateStatisticsAPITestCase"
]
