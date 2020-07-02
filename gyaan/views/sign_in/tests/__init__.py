# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "sign_in"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_in/v1/"

from .test_case_01 import TestCase01SignInAPITestCase

__all__ = [
    "TestCase01SignInAPITestCase"
]
