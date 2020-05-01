# coding: utf-8

"""
    Sematext Cloud API

    API Explorer provides access and documentation for Sematext REST API. The REST API requires the API Key to be sent as part of `Authorization` header. E.g.: `Authorization : apiKey e5f18450-205a-48eb-8589-7d49edaea813`.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.billing_api import BillingApi  # noqa: E501
from swagger_client.rest import ApiException


class TestBillingApi(unittest.TestCase):
    """BillingApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.billing_api.BillingApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_detailed_invoice_using_get(self):
        """Test case for get_detailed_invoice_using_get

        Get invoice details  # noqa: E501
        """
        pass

    def test_list_available_plans_using_get(self):
        """Test case for list_available_plans_using_get

        Get available plans  # noqa: E501
        """
        pass

    def test_update_plan_using_put(self):
        """Test case for update_plan_using_put

        Update plan for an app  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
