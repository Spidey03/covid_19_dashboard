# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "create_comment"
REQUEST_METHOD = "post"
URL_SUFFIX = "{entity_type}/{entity_id}/comment/v1/"

from .test_case_01 import TestCase01CreateCommentAPITestCase

__all__ = [
    "TestCase01CreateCommentAPITestCase"
]
