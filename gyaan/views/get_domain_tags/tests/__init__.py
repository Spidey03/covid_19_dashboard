# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_domain_tags"
REQUEST_METHOD = "get"
URL_SUFFIX = "domain/{domain_id}/tags/v1/"

from .test_case_01 import TestCase01GetDomainTagsAPITestCase

__all__ = [
    "TestCase01GetDomainTagsAPITestCase"
]
