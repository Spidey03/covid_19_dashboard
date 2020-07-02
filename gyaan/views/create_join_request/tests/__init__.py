# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "create_join_request"
REQUEST_METHOD = "post"
URL_SUFFIX = "users/domains/{domain_id}/request/v1/"

from .test_case_01 import TestCase01CreateJoinRequestAPITestCase

__all__ = [
    "TestCase01CreateJoinRequestAPITestCase"
]
