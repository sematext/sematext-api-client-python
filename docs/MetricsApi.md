# swagger_client.MetricsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_data_series_using_post1**](MetricsApi.md#list_data_series_using_post1) | **POST** /spm-reports/api/v3/apps/{appId}/metrics/data | Get metrics data points for an app
[**list_filters_using_post**](MetricsApi.md#list_filters_using_post) | **POST** /spm-reports/api/v3/apps/{appId}/metrics/filters | Get metrics filters and their values for an app
[**list_metrics_keys_using_get1**](MetricsApi.md#list_metrics_keys_using_get1) | **GET** /spm-reports/api/v3/apps/{appId}/metrics/keys | Get metrics keys for an app
[**list_metrics_using_get1**](MetricsApi.md#list_metrics_using_get1) | **GET** /spm-reports/api/v3/apps/{appId}/metrics | Get metrics info for an app


# **list_data_series_using_post1**
> GenericApiResponse list_data_series_using_post1(app_id, request_body)

Get metrics data points for an app

Default value of interval is 5m

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
app_id = 789 # int | appId
request_body = swagger_client.DataSeriesRequest() # DataSeriesRequest | Metric data points request

try:
    # Get metrics data points for an app
    api_response = api_instance.list_data_series_using_post1(app_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_data_series_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| appId | 
 **request_body** | [**DataSeriesRequest**](DataSeriesRequest.md)| Metric data points request | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_filters_using_post**
> GenericApiResponse list_filters_using_post(app_id, request_body)

Get metrics filters and their values for an app

Default value of interval is 5m

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
app_id = 789 # int | appId
request_body = swagger_client.DataSeriesRequest() # DataSeriesRequest | Metric filters request

try:
    # Get metrics filters and their values for an app
    api_response = api_instance.list_filters_using_post(app_id, request_body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_filters_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| appId | 
 **request_body** | [**DataSeriesRequest**](DataSeriesRequest.md)| Metric filters request | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_metrics_keys_using_get1**
> GenericApiResponse list_metrics_keys_using_get1(app_id)

Get metrics keys for an app

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get metrics keys for an app
    api_response = api_instance.list_metrics_keys_using_get1(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_metrics_keys_using_get1: %s\n" % e)
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

# **list_metrics_using_get1**
> GenericApiResponse list_metrics_using_get1(app_id)

Get metrics info for an app

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: api_key
configuration = swagger_client.Configuration()
configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.MetricsApi(swagger_client.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get metrics info for an app
    api_response = api_instance.list_metrics_using_get1(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MetricsApi->list_metrics_using_get1: %s\n" % e)
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

