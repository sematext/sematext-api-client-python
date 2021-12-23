# stcloud.AwsSettingsControllerApi

All URIs are relative to */*

| Method                                                                 | HTTP request                               | Description                               |
| ---------------------------------------------------------------------- | ------------------------------------------ | ----------------------------------------- |
| [**update_using_put1**](AwsSettingsControllerApi.md#update_using_put1) | **PUT** /users-web/api/v3/apps/{appId}/aws | Update App&#x27;s AWS CloudWatch settings |

# **update_using_put1**

> CloudWatchSettingsResponse update_using_put1(body, app_id)

Update App's AWS CloudWatch settings

Applicable only for AWS Apps

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
api_instance = stcloud.AwsSettingsControllerApi(stcloud.ApiClient(configuration))
body = stcloud.CloudWatchSettings() # CloudWatchSettings | dto
app_id = 789 # int | appId

try:
    # Update App's AWS CloudWatch settings
    api_response = api_instance.update_using_put1(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AwsSettingsControllerApi->update_using_put1: %s\n" % e)
```

### Parameters

| Name       | Type                                            | Description | Notes |
| ---------- | ----------------------------------------------- | ----------- | ----- |
| **body**   | [**CloudWatchSettings**](CloudWatchSettings.md) | dto         |
| **app_id** | **int**                                         | appId       |

### Return type

[**CloudWatchSettingsResponse**](CloudWatchSettingsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
