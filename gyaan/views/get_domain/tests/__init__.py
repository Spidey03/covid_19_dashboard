# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_domain"
REQUEST_METHOD = "get"
URL_SUFFIX = "domain/{domain_id}/metrics/v1/"

from .test_case_01 import TestCase01GetDomainAPITestCase

__all__ = [
    "TestCase01GetDomainAPITestCase"
]
