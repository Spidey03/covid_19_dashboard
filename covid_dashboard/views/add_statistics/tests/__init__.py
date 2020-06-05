# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "add_statistics"
REQUEST_METHOD = "post"
URL_SUFFIX = "stats/add/v1/"

from .test_case_01 import TestCase01AddStatisticsAPITestCase

__all__ = [
    "TestCase01AddStatisticsAPITestCase"
]
