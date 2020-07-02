# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_user_profile"
REQUEST_METHOD = "get"
URL_SUFFIX = "user/{user_id}/v1/"

from .test_case_01 import TestCase01GetUserProfileAPITestCase

__all__ = [
    "TestCase01GetUserProfileAPITestCase"
]
