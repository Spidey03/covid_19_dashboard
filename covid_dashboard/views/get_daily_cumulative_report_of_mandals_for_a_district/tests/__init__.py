# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_daily_cumulative_report_of_mandals_for_a_district"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/mandals/daily_cumulative/v1/"

from .test_case_01 import TestCase01GetDailyCumulativeReportOfMandalsForADistrictAPITestCase

__all__ = [
    "TestCase01GetDailyCumulativeReportOfMandalsForADistrictAPITestCase"
]
