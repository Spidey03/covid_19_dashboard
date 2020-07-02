# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "sign_up"
REQUEST_METHOD = "post"
URL_SUFFIX = "sign_up/v1/"

from .test_case_01 import TestCase01SignUpAPITestCase

__all__ = [
    "TestCase01SignUpAPITestCase"
]
