# stcloud.LogsUsageApiControllerApi

All URIs are relative to */*

| Method                                                                              | HTTP request                                                   | Description |
| ----------------------------------------------------------------------------------- | -------------------------------------------------------------- | ----------- |
| [**get_for_range_using_get**](LogsUsageApiControllerApi.md#get_for_range_using_get) | **GET** /logsene-reports/api/v3/apps/{appId}/usage/{from}/{to} | getForRange |

# **get_for_range_using_get**

> UsageResponse get_for_range_using_get(app_id,_from, to)

getForRange

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
api_instance = stcloud.LogsUsageApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
_from = 789 # int | from
to = 789 # int | to

try:
    # getForRange
    api_response = api_instance.get_for_range_using_get(app_id, _from, to)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling LogsUsageApiControllerApi->get_for_range_using_get: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **app_id** | **int** | appId       |
| **_from**  | **int** | from        |
| **to**     | **int** | to          |

### Return type

[**UsageResponse**](UsageResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
