# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "request_status"
REQUEST_METHOD = "post"
URL_SUFFIX = "domain_experts/domains/requests/v1/"

from .test_case_01 import TestCase01RequestStatusAPITestCase

__all__ = [
    "TestCase01RequestStatusAPITestCase"
]
