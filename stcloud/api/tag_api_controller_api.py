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


class TagApiControllerApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_tag_names_using_get1(self, app_ids, **kwargs):  # noqa: E501
        """Gets tag names for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag_names_using_get1(app_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: TagNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_tag_names_using_get1_with_http_info(app_ids, **kwargs)  # noqa: E501
        else:
            (data) = self.get_tag_names_using_get1_with_http_info(app_ids, **kwargs)  # noqa: E501
            return data

    def get_tag_names_using_get1_with_http_info(self, app_ids, **kwargs):  # noqa: E501
        """Gets tag names for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_tag_names_using_get1_with_http_info(app_ids, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: TagNamesResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_ids', '_from', 'to', 'metrics', 'logs', 'events', 'rum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tag_names_using_get1" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_ids' is set
        if ('app_ids' not in params or
                params['app_ids'] is None):
            raise ValueError("Missing the required parameter `app_ids` when calling `get_tag_names_using_get1`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_ids' in params:
            path_params['appIds'] = params['app_ids']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'logs' in params:
            query_params.append(('logs', params['logs']))  # noqa: E501
        if 'events' in params:
            query_params.append(('events', params['events']))  # noqa: E501
        if 'rum' in params:
            query_params.append(('rum', params['rum']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/spm-reports/api/v3/apps/{appIds}/tagNames', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TagNamesResponse',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_using_get2(self, app_ids, tag, **kwargs):  # noqa: E501
        """Gets values for specified tags for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get2(app_ids, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param list[str] tag: tag (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: dict(str, Dimension)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_using_get2_with_http_info(app_ids, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_using_get2_with_http_info(app_ids, tag, **kwargs)  # noqa: E501
            return data

    def get_using_get2_with_http_info(self, app_ids, tag, **kwargs):  # noqa: E501
        """Gets values for specified tags for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get2_with_http_info(app_ids, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param list[str] tag: tag (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: dict(str, Dimension)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_ids', 'tag', '_from', 'to', 'metrics', 'logs', 'events', 'rum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_using_get2" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_ids' is set
        if ('app_ids' not in params or
                params['app_ids'] is None):
            raise ValueError("Missing the required parameter `app_ids` when calling `get_using_get2`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_using_get2`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_ids' in params:
            path_params['appIds'] = params['app_ids']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
            collection_formats['tag'] = 'multi'  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'logs' in params:
            query_params.append(('logs', params['logs']))  # noqa: E501
        if 'events' in params:
            query_params.append(('events', params['events']))  # noqa: E501
        if 'rum' in params:
            query_params.append(('rum', params['rum']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/spm-reports/api/v3/apps/{appIds}/metrics/filters', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, Dimension)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_using_get3(self, app_ids, tag, **kwargs):  # noqa: E501
        """Gets values for specified tags for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get3(app_ids, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param list[str] tag: tag (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: dict(str, Dimension)
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_using_get3_with_http_info(app_ids, tag, **kwargs)  # noqa: E501
        else:
            (data) = self.get_using_get3_with_http_info(app_ids, tag, **kwargs)  # noqa: E501
            return data

    def get_using_get3_with_http_info(self, app_ids, tag, **kwargs):  # noqa: E501
        """Gets values for specified tags for the given application identifiers appearing in the given time frame.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_using_get3_with_http_info(app_ids, tag, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str app_ids: appIds (required)
        :param list[str] tag: tag (required)
        :param int _from: from
        :param int to: to
        :param bool metrics: metrics
        :param bool logs: logs
        :param bool events: events
        :param bool rum: rum
        :return: dict(str, Dimension)
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_ids', 'tag', '_from', 'to', 'metrics', 'logs', 'events', 'rum']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_using_get3" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_ids' is set
        if ('app_ids' not in params or
                params['app_ids'] is None):
            raise ValueError("Missing the required parameter `app_ids` when calling `get_using_get3`")  # noqa: E501
        # verify the required parameter 'tag' is set
        if ('tag' not in params or
                params['tag'] is None):
            raise ValueError("Missing the required parameter `tag` when calling `get_using_get3`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_ids' in params:
            path_params['appIds'] = params['app_ids']  # noqa: E501

        query_params = []
        if '_from' in params:
            query_params.append(('from', params['_from']))  # noqa: E501
        if 'to' in params:
            query_params.append(('to', params['to']))  # noqa: E501
        if 'tag' in params:
            query_params.append(('tag', params['tag']))  # noqa: E501
            collection_formats['tag'] = 'multi'  # noqa: E501
        if 'metrics' in params:
            query_params.append(('metrics', params['metrics']))  # noqa: E501
        if 'logs' in params:
            query_params.append(('logs', params['logs']))  # noqa: E501
        if 'events' in params:
            query_params.append(('events', params['events']))  # noqa: E501
        if 'rum' in params:
            query_params.append(('rum', params['rum']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/spm-reports/api/v3/apps/{appIds}/tags', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='dict(str, Dimension)',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
