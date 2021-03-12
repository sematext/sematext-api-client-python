# stcloud.LogsAppApi

All URIs are relative to */*

| Method                                                                     | HTTP request                          | Description     |
| -------------------------------------------------------------------------- | ------------------------------------- | --------------- |
| [**create_logsene_application**](LogsAppApi.md#create_logsene_application) | **POST** /logsene-reports/api/v3/apps | Create Logs App |

# **create_logsene_application**
> AppsResponse create_logsene_application(body)

Create Logs App

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
api_instance = stcloud.LogsAppApi(stcloud.ApiClient(configuration))
body = stcloud.CreateAppInfo() # CreateAppInfo | Details of the application to be created

try:
    # Create Logs App
    api_response = api_instance.create_logsene_application(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsAppApi->create_logsene_application: %s\n" % e)
```

### Parameters

| Name     | Type                                  | Description                              | Notes |
| -------- | ------------------------------------- | ---------------------------------------- | ----- |
| **body** | [**CreateAppInfo**](CreateAppInfo.md) | Details of the application to be created |

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
