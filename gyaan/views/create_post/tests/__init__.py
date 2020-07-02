# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "create_post"
REQUEST_METHOD = "post"
URL_SUFFIX = "domains/{domain_id}/posts/v1/"

from .test_case_01 import TestCase01CreatePostAPITestCase

__all__ = [
    "TestCase01CreatePostAPITestCase"
]
