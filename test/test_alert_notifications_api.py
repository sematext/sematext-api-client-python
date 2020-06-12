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
from stcloud.api.alert_notifications_api import AlertNotificationsApi  # noqa: E501
from stcloud.rest import ApiException


class TestAlertNotificationsApi(unittest.TestCase):
    """AlertNotificationsApi unit test stubs"""

    def setUp(self):
        self.api = stcloud.api.alert_notifications_api.AlertNotificationsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_alert_notifications_for_app_using_post(self):
        """Test case for get_alert_notifications_for_app_using_post

        Get alert notifications for an app  # noqa: E501
        """
        pass

    def test_get_alert_notifications_for_user_using_post(self):
        """Test case for get_alert_notifications_for_user_using_post

        Get alert notifications for a user  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
