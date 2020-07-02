# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "leave_from_domain"
REQUEST_METHOD = "post"
URL_SUFFIX = "domains/{domain_id}/leave/v1/"

from .test_case_01 import TestCase01LeaveFromDomainAPITestCase

__all__ = [
    "TestCase01LeaveFromDomainAPITestCase"
]
