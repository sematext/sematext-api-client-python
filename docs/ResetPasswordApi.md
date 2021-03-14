# stcloud.ResetPasswordApi

All URIs are relative to */*

| Method                                                                         | HTTP request                                      | Description    |
| ------------------------------------------------------------------------------ | ------------------------------------------------- | -------------- |
| [**reset_password_using_post**](ResetPasswordApi.md#reset_password_using_post) | **POST** /users-web/api/v3/account/password/reset | Reset Password |

# **reset_password_using_post**
> GenericMapBasedApiResponse reset_password_using_post(body)

Reset Password

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
api_instance = stcloud.ResetPasswordApi(stcloud.ApiClient(configuration))
body = stcloud.UserInfo() # UserInfo | dto

try:
    # Reset Password
    api_response = api_instance.reset_password_using_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ResetPasswordApi->reset_password_using_post: %s\n" % e)
```

### Parameters

| Name     | Type                        | Description | Notes |
| -------- | --------------------------- | ----------- | ----- |
| **body** | [**UserInfo**](UserInfo.md) | dto         |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
