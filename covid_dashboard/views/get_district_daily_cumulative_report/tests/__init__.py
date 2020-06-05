# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_district_daily_cumulative_report"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/daily_cumulative/v1/"

from .test_case_01 import TestCase01GetDistrictDailyCumulativeReportAPITestCase

__all__ = [
    "TestCase01GetDistrictDailyCumulativeReportAPITestCase"
]
