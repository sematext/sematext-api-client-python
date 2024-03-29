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
from stcloud.api.aws_settings_controller_api import AwsSettingsControllerApi  # noqa: E501
from stcloud.rest import ApiException


class TestAwsSettingsControllerApi(unittest.TestCase):
    """AwsSettingsControllerApi unit test stubs"""

    def setUp(self):
        self.api = AwsSettingsControllerApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_update_using_put(self):
        """Test case for update_using_put

        Update App's AWS CloudWatch settings  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
