# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "create_answer"
REQUEST_METHOD = "post"
URL_SUFFIX = "post/comment/{comment_id}/marK_as_answer/v1/"

from .test_case_01 import TestCase01CreateAnswerAPITestCase

__all__ = [
    "TestCase01CreateAnswerAPITestCase"
]
