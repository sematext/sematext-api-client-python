# coding: utf-8

"""
    Sematext Cloud API

    API Explorer provides access and documentation for Sematext REST API. The REST API requires the API Key to be sent as part of `Authorization` header. E.g.: `Authorization : apiKey e5f18450-205a-48eb-8589-7d49edaea813`.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class AlertNotificationsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_alert_notifications_for_app_using_post(self, app_id, time_interval, **kwargs):  # noqa: E501
        """Get alert notifications for an app  # noqa: E501

        Default value of interval is 1d  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_notifications_for_app_using_post(app_id, time_interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :param AlertNotificationRequest time_interval: Time Interval (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alert_notifications_for_app_using_post_with_http_info(app_id, time_interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alert_notifications_for_app_using_post_with_http_info(app_id, time_interval, **kwargs)  # noqa: E501
            return data

    def get_alert_notifications_for_app_using_post_with_http_info(self, app_id, time_interval, **kwargs):  # noqa: E501
        """Get alert notifications for an app  # noqa: E501

        Default value of interval is 1d  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_notifications_for_app_using_post_with_http_info(app_id, time_interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :param AlertNotificationRequest time_interval: Time Interval (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'time_interval']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alert_notifications_for_app_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `get_alert_notifications_for_app_using_post`")  # noqa: E501
        # verify the required parameter 'time_interval' is set
        if ('time_interval' not in params or
                params['time_interval'] is None):
            raise ValueError("Missing the required parameter `time_interval` when calling `get_alert_notifications_for_app_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'time_interval' in params:
            body_params = params['time_interval']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/apps/{appId}/notifications/alerts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_alert_notifications_for_user_using_post(self, time_interval, **kwargs):  # noqa: E501
        """Get alert notifications for a user  # noqa: E501

        Default value of interval is 1d  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_notifications_for_user_using_post(time_interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlertNotificationRequest time_interval: Time Interval (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_alert_notifications_for_user_using_post_with_http_info(time_interval, **kwargs)  # noqa: E501
        else:
            (data) = self.get_alert_notifications_for_user_using_post_with_http_info(time_interval, **kwargs)  # noqa: E501
            return data

    def get_alert_notifications_for_user_using_post_with_http_info(self, time_interval, **kwargs):  # noqa: E501
        """Get alert notifications for a user  # noqa: E501

        Default value of interval is 1d  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_alert_notifications_for_user_using_post_with_http_info(time_interval, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AlertNotificationRequest time_interval: Time Interval (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['time_interval']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_alert_notifications_for_user_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'time_interval' is set
        if ('time_interval' not in params or
                params['time_interval'] is None):
            raise ValueError("Missing the required parameter `time_interval` when calling `get_alert_notifications_for_user_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'time_interval' in params:
            body_params = params['time_interval']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/notifications/alerts', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='GenericApiResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
