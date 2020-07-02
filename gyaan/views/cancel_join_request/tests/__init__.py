# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "cancel_join_request"
REQUEST_METHOD = "delete"
URL_SUFFIX = "domain/{domain_id}/request/cancel/v1/"

from .test_case_01 import TestCase01CancelJoinRequestAPITestCase

__all__ = [
    "TestCase01CancelJoinRequestAPITestCase"
]
