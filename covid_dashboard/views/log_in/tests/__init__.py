# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "log_in"
REQUEST_METHOD = "post"
URL_SUFFIX = "login/v1/"

from .test_case_01 import TestCase01LogInAPITestCase

__all__ = [
    "TestCase01LogInAPITestCase"
]
