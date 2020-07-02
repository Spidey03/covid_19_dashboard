"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from gyaan.utils.custom_test_utils_2 import CustomTestUtils

REQUEST_BODY = """
{

}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {"limit": 5, "offset": 0},
        "header_params": {},
        "securities": {"oauth": {"type": "oauth2", "tokenUrl": "http://auth.ibtspl.com/oauth2/", "flow": "password", "scopes": ["read"]}},
        "body": REQUEST_BODY,
    },
}


class TestCase01GetPostsAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    def setupUser(self, username, password):
        super(TestCase01GetPostsAPITestCase, self).setupUser(
            username=username, password=password
        )
        self.get_home_feed()

    def test_case(self):
        response = self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.

        import json
        response_data = json.loads(response.content)

        self.assert_match_snapshot(
            name="get_home_feed",
            value=response_data
        )