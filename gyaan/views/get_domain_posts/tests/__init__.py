# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_domain_posts"
REQUEST_METHOD = "get"
URL_SUFFIX = "domain/{domain_id}/posts/v1/"

from .test_case_01 import TestCase01GetDomainPostsAPITestCase

__all__ = [
    "TestCase01GetDomainPostsAPITestCase"
]
