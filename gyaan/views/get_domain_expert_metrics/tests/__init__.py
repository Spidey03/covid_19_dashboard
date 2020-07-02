# pylint: disable=wrong-import-position

APP_NAME = "gyaan"
OPERATION_NAME = "get_domain_expert_metrics"
REQUEST_METHOD = "get"
URL_SUFFIX = "domain_expert/metrics/v1/"

from .test_case_01 import TestCase01GetDomainExpertMetricsAPITestCase

__all__ = [
    "TestCase01GetDomainExpertMetricsAPITestCase"
]
