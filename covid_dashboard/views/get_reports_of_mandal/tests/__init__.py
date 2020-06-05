# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_reports_of_mandal"
REQUEST_METHOD = "get"
URL_SUFFIX = "statstics/v1/"

from .test_case_01 import TestCase01GetReportsOfMandalAPITestCase

__all__ = [
    "TestCase01GetReportsOfMandalAPITestCase"
]
