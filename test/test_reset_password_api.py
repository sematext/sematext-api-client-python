# coding: utf-8

"""
    Sematext Cloud API

    API Explorer provides access and documentation for Sematext REST API. The REST API requires the API Key to be sent as part of `Authorization` header. E.g.: `Authorization : apiKey e5f18450-205a-48eb-8589-7d49edaea813`.  # noqa: E501

    OpenAPI spec version: v3

    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import stcloud
from stcloud.api.reset_password_api import ResetPasswordApi  # noqa: E501
from stcloud.rest import ApiException


class TestResetPasswordApi(unittest.TestCase):
    """ResetPasswordApi unit test stubs"""

    def setUp(self):
        self.api = stcloud.api.reset_password_api.ResetPasswordApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_reset_password_using_post(self):
        """Test case for reset_password_using_post

        Reset Password  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
