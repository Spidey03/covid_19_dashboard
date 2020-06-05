# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_cumulative_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/cumulative/v1/"

from .test_case_01 import TestCase01GetDistrictCumulativeReportAPITestCase

__all__ = [
    "TestCase01GetDistrictCumulativeReportAPITestCase"
]
