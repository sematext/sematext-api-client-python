# stcloud.SavedQueriesApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_saved_query_using_delete**](SavedQueriesApi.md#delete_saved_query_using_delete) | **DELETE** /users-web/api/v3/savedQueries/{updateableQueryId} | Delete saved query
[**get_saved_queries_for_app_using_get**](SavedQueriesApi.md#get_saved_queries_for_app_using_get) | **GET** /users-web/api/v3/apps/{appId}/savedQueries | Get saved queries for an app
[**save_query_using_post**](SavedQueriesApi.md#save_query_using_post) | **POST** /users-web/api/v3/savedQueries | Create saved query
[**save_query_using_put**](SavedQueriesApi.md#save_query_using_put) | **PUT** /users-web/api/v3/savedQueries/{updateableQueryId} | Update saved query


# **delete_saved_query_using_delete**
> GenericApiResponse delete_saved_query_using_delete(updateable_query_id)

Delete saved query

### Example
```python
from __future__ import print_function
import time
import stcloud
from stcloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = stcloud.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = stcloud.SavedQueriesApi(stcloud.ApiClient(configuration))
updateable_query_id = 789 # int | updateableQueryId

try:
    # Delete saved query
    api_response = api_instance.delete_saved_query_using_delete(updateable_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesApi->delete_saved_query_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateable_query_id** | **int**| updateableQueryId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_saved_queries_for_app_using_get**
> GenericApiResponse get_saved_queries_for_app_using_get(app_id)

Get saved queries for an app

### Example
```python
from __future__ import print_function
import time
import stcloud
from stcloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = stcloud.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = stcloud.SavedQueriesApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get saved queries for an app
    api_response = api_instance.get_saved_queries_for_app_using_get(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesApi->get_saved_queries_for_app_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| appId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_query_using_post**
> GenericApiResponse save_query_using_post(saved_query_dto)

Create saved query

### Example
```python
from __future__ import print_function
import time
import stcloud
from stcloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = stcloud.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = stcloud.SavedQueriesApi(stcloud.ApiClient(configuration))
saved_query_dto = stcloud.SavedQuery() # SavedQuery | savedQueryDto

try:
    # Create saved query
    api_response = api_instance.save_query_using_post(saved_query_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesApi->save_query_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_query_dto** | [**SavedQuery**](SavedQuery.md)| savedQueryDto | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **save_query_using_put**
> GenericApiResponse save_query_using_put(saved_query_dto, updateable_query_id)

Update saved query

### Example
```python
from __future__ import print_function
import time
import stcloud
from stcloud.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = stcloud.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = stcloud.SavedQueriesApi(stcloud.ApiClient(configuration))
saved_query_dto = stcloud.SavedQuery() # SavedQuery | savedQueryDto
updateable_query_id = 789 # int | updateableQueryId

try:
    # Update saved query
    api_response = api_instance.save_query_using_put(saved_query_dto, updateable_query_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SavedQueriesApi->save_query_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **saved_query_dto** | [**SavedQuery**](SavedQuery.md)| savedQueryDto | 
 **updateable_query_id** | **int**| updateableQueryId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

