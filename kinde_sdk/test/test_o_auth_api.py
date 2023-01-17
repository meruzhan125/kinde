"""
    Kinde Management API

    Provides endpoints to manage your Kinde Businesses  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Contact: support@kinde.com
    Generated by: https://openapi-generator.tech
"""


import unittest

import kinde_sdk
from kinde_sdk.api.o_auth_api import OAuthApi  # noqa: E501


class TestOAuthApi(unittest.TestCase):
    """OAuthApi unit test stubs"""

    def setUp(self):
        self.api = OAuthApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_user(self):
        """Test case for get_user

        Returns the details of the currently logged in user  # noqa: E501
        """
        pass

    def test_get_user_profile_v2(self):
        """Test case for get_user_profile_v2

        Returns the details of the currently logged in user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
