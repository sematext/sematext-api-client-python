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
from swagger_client.api.saved_queries_api import SavedQueriesApi  # noqa: E501
from swagger_client.rest import ApiException


class TestSavedQueriesApi(unittest.TestCase):
    """SavedQueriesApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.saved_queries_api.SavedQueriesApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_delete_saved_query_using_delete(self):
        """Test case for delete_saved_query_using_delete

        Delete saved query  # noqa: E501
        """
        pass

    def test_get_saved_queries_for_app_using_get(self):
        """Test case for get_saved_queries_for_app_using_get

        Get saved queries for an app  # noqa: E501
        """
        pass

    def test_save_query_using_post(self):
        """Test case for save_query_using_post

        Create saved query  # noqa: E501
        """
        pass

    def test_save_query_using_put(self):
        """Test case for save_query_using_put

        Update saved query  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
