# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "get_day_wise_mandal_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districts/{district_id}/mandals/v1/"

from .test_case_01 import TestCase01GetDayWiseMandalDetailsAPITestCase

__all__ = [
    "TestCase01GetDayWiseMandalDetailsAPITestCase"
]
