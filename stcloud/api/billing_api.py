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

from stcloud.api_client import ApiClient


class BillingApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_detailed_invoice_using_get(self, service, year, month, **kwargs):  # noqa: E501
        """Get invoice details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_detailed_invoice_using_get(service, year, month, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service: service (required)
        :param int year: year (required)
        :param int month: month (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_detailed_invoice_using_get_with_http_info(service, year, month, **kwargs)  # noqa: E501
        else:
            (data) = self.get_detailed_invoice_using_get_with_http_info(service, year, month, **kwargs)  # noqa: E501
            return data

    def get_detailed_invoice_using_get_with_http_info(self, service, year, month, **kwargs):  # noqa: E501
        """Get invoice details  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_detailed_invoice_using_get_with_http_info(service, year, month, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str service: service (required)
        :param int year: year (required)
        :param int month: month (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service', 'year', 'month']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_detailed_invoice_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service' is set
        if ('service' not in params
                or params['service'] is None):
            raise ValueError("Missing the required parameter `service` when calling `get_detailed_invoice_using_get`")  # noqa: E501
        # verify the required parameter 'year' is set
        if ('year' not in params
                or params['year'] is None):
            raise ValueError("Missing the required parameter `year` when calling `get_detailed_invoice_using_get`")  # noqa: E501
        # verify the required parameter 'month' is set
        if ('month' not in params
                or params['month'] is None):
            raise ValueError("Missing the required parameter `month` when calling `get_detailed_invoice_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'service' in params:
            path_params['service'] = params['service']  # noqa: E501
        if 'year' in params:
            path_params['year'] = params['year']  # noqa: E501
        if 'month' in params:
            path_params['month'] = params['month']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/billing/invoice/{service}/{year}/{month}', 'GET',
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

    def list_available_plans_using_get(self, **kwargs):  # noqa: E501
        """Get available plans  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_available_plans_using_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int integration_id: integrationId
        :param str app_type: appType
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_available_plans_using_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_available_plans_using_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_available_plans_using_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get available plans  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_available_plans_using_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int integration_id: integrationId
        :param str app_type: appType
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['integration_id', 'app_type']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_available_plans_using_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'integration_id' in params:
            query_params.append(('integrationId', params['integration_id']))  # noqa: E501
        if 'app_type' in params:
            query_params.append(('appType', params['app_type']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/billing/availablePlans', 'GET',
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

    def update_plan_using_put(self, app_id, dto, **kwargs):  # noqa: E501
        """Update plan for an app  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_plan_using_put(app_id, dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :param BillingInfo dto: dto (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_plan_using_put_with_http_info(app_id, dto, **kwargs)  # noqa: E501
        else:
            (data) = self.update_plan_using_put_with_http_info(app_id, dto, **kwargs)  # noqa: E501
            return data

    def update_plan_using_put_with_http_info(self, app_id, dto, **kwargs):  # noqa: E501
        """Update plan for an app  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_plan_using_put_with_http_info(app_id, dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :param BillingInfo dto: dto (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id', 'dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_plan_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params
                or params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `update_plan_using_put`")  # noqa: E501
        # verify the required parameter 'dto' is set
        if ('dto' not in params
                or params['dto'] is None):
            raise ValueError("Missing the required parameter `dto` when calling `update_plan_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'dto' in params:
            body_params = params['dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/billing/info/{appId}', 'PUT',
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
