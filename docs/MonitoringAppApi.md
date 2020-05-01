# swagger_client.MonitoringAppApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_spm_application**](MonitoringAppApi.md#create_spm_application) | **POST** /spm-reports/api/v3/apps | Create Monitoring App


# **create_spm_application**
> GenericApiResponse create_spm_application(application_details)

Create Monitoring App

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
api_instance = swagger_client.MonitoringAppApi(swagger_client.ApiClient(configuration))
application_details = swagger_client.CreateAppInfo() # CreateAppInfo | Details of the application to be created

try:
    # Create Monitoring App
    api_response = api_instance.create_spm_application(application_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling MonitoringAppApi->create_spm_application: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **application_details** | [**CreateAppInfo**](CreateAppInfo.md)| Details of the application to be created | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

