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


class SavedQueriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def delete_saved_query_using_delete(self, updateable_query_id, **kwargs):  # noqa: E501
        """Delete saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saved_query_using_delete(updateable_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int updateable_query_id: updateableQueryId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_saved_query_using_delete_with_http_info(updateable_query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_saved_query_using_delete_with_http_info(updateable_query_id, **kwargs)  # noqa: E501
            return data

    def delete_saved_query_using_delete_with_http_info(self, updateable_query_id, **kwargs):  # noqa: E501
        """Delete saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_saved_query_using_delete_with_http_info(updateable_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int updateable_query_id: updateableQueryId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['updateable_query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_saved_query_using_delete" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'updateable_query_id' is set
        if ('updateable_query_id' not in params or
                params['updateable_query_id'] is None):
            raise ValueError("Missing the required parameter `updateable_query_id` when calling `delete_saved_query_using_delete`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'updateable_query_id' in params:
            path_params['updateableQueryId'] = params['updateable_query_id']  # noqa: E501

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
            '/users-web/api/v3/savedQueries/{updateableQueryId}', 'DELETE',
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

    def get_saved_queries_for_app_using_get(self, app_id, **kwargs):  # noqa: E501
        """Get saved queries for an app  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saved_queries_for_app_using_get(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_saved_queries_for_app_using_get_with_http_info(app_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_saved_queries_for_app_using_get_with_http_info(app_id, **kwargs)  # noqa: E501
            return data

    def get_saved_queries_for_app_using_get_with_http_info(self, app_id, **kwargs):  # noqa: E501
        """Get saved queries for an app  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_saved_queries_for_app_using_get_with_http_info(app_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int app_id: appId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['app_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_saved_queries_for_app_using_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'app_id' is set
        if ('app_id' not in params or
                params['app_id'] is None):
            raise ValueError("Missing the required parameter `app_id` when calling `get_saved_queries_for_app_using_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'app_id' in params:
            path_params['appId'] = params['app_id']  # noqa: E501

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
            '/users-web/api/v3/apps/{appId}/savedQueries', 'GET',
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

    def save_query_using_post(self, saved_query_dto, **kwargs):  # noqa: E501
        """Create saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_query_using_post(saved_query_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SavedQuery saved_query_dto: savedQueryDto (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_query_using_post_with_http_info(saved_query_dto, **kwargs)  # noqa: E501
        else:
            (data) = self.save_query_using_post_with_http_info(saved_query_dto, **kwargs)  # noqa: E501
            return data

    def save_query_using_post_with_http_info(self, saved_query_dto, **kwargs):  # noqa: E501
        """Create saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_query_using_post_with_http_info(saved_query_dto, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SavedQuery saved_query_dto: savedQueryDto (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['saved_query_dto']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_query_using_post" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'saved_query_dto' is set
        if ('saved_query_dto' not in params or
                params['saved_query_dto'] is None):
            raise ValueError("Missing the required parameter `saved_query_dto` when calling `save_query_using_post`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'saved_query_dto' in params:
            body_params = params['saved_query_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/savedQueries', 'POST',
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

    def save_query_using_put(self, saved_query_dto, updateable_query_id, **kwargs):  # noqa: E501
        """Update saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_query_using_put(saved_query_dto, updateable_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SavedQuery saved_query_dto: savedQueryDto (required)
        :param int updateable_query_id: updateableQueryId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.save_query_using_put_with_http_info(saved_query_dto, updateable_query_id, **kwargs)  # noqa: E501
        else:
            (data) = self.save_query_using_put_with_http_info(saved_query_dto, updateable_query_id, **kwargs)  # noqa: E501
            return data

    def save_query_using_put_with_http_info(self, saved_query_dto, updateable_query_id, **kwargs):  # noqa: E501
        """Update saved query  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.save_query_using_put_with_http_info(saved_query_dto, updateable_query_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param SavedQuery saved_query_dto: savedQueryDto (required)
        :param int updateable_query_id: updateableQueryId (required)
        :return: GenericApiResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['saved_query_dto', 'updateable_query_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method save_query_using_put" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'saved_query_dto' is set
        if ('saved_query_dto' not in params or
                params['saved_query_dto'] is None):
            raise ValueError("Missing the required parameter `saved_query_dto` when calling `save_query_using_put`")  # noqa: E501
        # verify the required parameter 'updateable_query_id' is set
        if ('updateable_query_id' not in params or
                params['updateable_query_id'] is None):
            raise ValueError("Missing the required parameter `updateable_query_id` when calling `save_query_using_put`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'updateable_query_id' in params:
            path_params['updateableQueryId'] = params['updateable_query_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'saved_query_dto' in params:
            body_params = params['saved_query_dto']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = ['api_key']  # noqa: E501

        return self.api_client.call_api(
            '/users-web/api/v3/savedQueries/{updateableQueryId}', 'PUT',
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
