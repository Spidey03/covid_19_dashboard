# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "create_reaction"
REQUEST_METHOD = "post"
URL_SUFFIX = "{entity_type}/{entity_id}/react/v1/"

from .test_case_01 import TestCase01CreateReactionAPITestCase

__all__ = [
    "TestCase01CreateReactionAPITestCase"
]
