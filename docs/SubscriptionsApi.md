# stcloud.SubscriptionsApi

All URIs are relative to *https://localhost*

| Method                                                                   | HTTP request                                         | Description                           |
| ------------------------------------------------------------------------ | ---------------------------------------------------- | ------------------------------------- |
| [**list_using_get1**](SubscriptionsApi.md#list_using_get1)               | **GET** /users-web/api/v3/apps/{appId}/subscriptions | Get subscriptions for an app          |
| [**send_report_using_post**](SubscriptionsApi.md#send_report_using_post) | **POST** /users-web/api/v3/apps/{appId}/report/send  | Trigger emailing of report for an app |


# **list_using_get1**
> GenericApiResponse list_using_get1(app_id)

Get subscriptions for an app

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
api_instance = stcloud.SubscriptionsApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get subscriptions for an app
    api_response = api_instance.list_using_get1(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_using_get1: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **app_id** | **int** | appId       |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_report_using_post**
> GenericApiResponse send_report_using_post(app_id, email_dto)

Trigger emailing of report for an app

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
api_instance = stcloud.SubscriptionsApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
email_dto = stcloud.ReportInfo() # ReportInfo | emailDto

try:
    # Trigger emailing of report for an app
    api_response = api_instance.send_report_using_post(app_id, email_dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->send_report_using_post: %s\n" % e)
```

### Parameters

| Name          | Type                            | Description | Notes |
| ------------- | ------------------------------- | ----------- | ----- |
| **app_id**    | **int**                         | appId       |
| **email_dto** | [**ReportInfo**](ReportInfo.md) | emailDto    |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
