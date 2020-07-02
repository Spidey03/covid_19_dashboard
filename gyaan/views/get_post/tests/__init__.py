# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_post"
REQUEST_METHOD = "get"
URL_SUFFIX = "post/{post_id}/v1/"

from .test_case_01 import TestCase01GetPostAPITestCase

__all__ = [
    "TestCase01GetPostAPITestCase"
]
