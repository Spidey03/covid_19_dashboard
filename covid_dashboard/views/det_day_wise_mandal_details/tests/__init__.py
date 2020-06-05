# pylint: disable=wrong-import-position

APP_NAME = "covid_dashboard"
OPERATION_NAME = "det_day_wise_mandal_details"
REQUEST_METHOD = "get"
URL_SUFFIX = "state/districs/{district_id}/mandals/v1/"

from .test_case_01 import TestCase01DetDayWiseMandalDetailsAPITestCase

__all__ = [
    "TestCase01DetDayWiseMandalDetailsAPITestCase"
]
