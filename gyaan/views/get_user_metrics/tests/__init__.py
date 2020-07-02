# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_user_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/metrics/v1/"

from .test_case_01 import TestCase01GetUserMetricsAPITestCase

__all__ = [
    "TestCase01GetUserMetricsAPITestCase"
]
