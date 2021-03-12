# stcloud.MonitoringAppApi

All URIs are relative to */*

| Method                                                                     | HTTP request                      | Description           |
| -------------------------------------------------------------------------- | --------------------------------- | --------------------- |
| [**create_spm_application1**](MonitoringAppApi.md#create_spm_application1) | **POST** /spm-reports/api/v3/apps | Create Monitoring App |

# **create_spm_application1**
> AppsResponse create_spm_application1(body)

Create Monitoring App

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
api_instance = stcloud.MonitoringAppApi(stcloud.ApiClient(configuration))
body = stcloud.CreateAppInfo() # CreateAppInfo | Details of the application to be created

try:
    # Create Monitoring App
    api_response = api_instance.create_spm_application1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAppApi->create_spm_application1: %s\n" % e)
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
