"""
# TODO: Update test case description
"""

from django_swagger_utils.utils.test import CustomAPITestCase
from . import APP_NAME, OPERATION_NAME, REQUEST_METHOD, URL_SUFFIX
from covid_dashboard.utils.custom_test_utils_2 import CustomTestUtils
from covid_dashboard.tests.factories import UserFactory
from freezegun import freeze_time

REQUEST_BODY = """
{
    "username": "Spidey",
    "password": "Codist"
}
"""

TEST_CASE = {
    "request": {
        "path_params": {},
        "query_params": {},
        "header_params": {},
        "securities": {},
        "body": REQUEST_BODY,
    },
}


class TestCase02LogInAPITestCase(CustomTestUtils):
    app_name = APP_NAME
    operation_name = OPERATION_NAME
    request_method = REQUEST_METHOD
    url_suffix = URL_SUFFIX
    test_case_dict = TEST_CASE

    
    @freeze_time('2020-05-22')
    def test_case(self):
        user = UserFactory(username='Spidey')
        user.set_password('Codist')
        user.save()
        print('*0'*30)
        print(user.__dict__)
        print('*0'*30)
        self.default_test_case() # Returns response object.
        # Which can be used for further response object checks.
        # Add database state checks here.