# stcloud.SubscriptionsApi

All URIs are relative to */*

| Method                                                                             | HTTP request                                                          | Description                              |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------- |
| [**create_for_app_using_post**](SubscriptionsApi.md#create_for_app_using_post)     | **POST** /users-web/api/v3/apps/{appId}/subscription                  | Create App subscription                  |
| [**create_for_dash_using_post1**](SubscriptionsApi.md#create_for_dash_using_post1) | **POST** /users-web/api/v3/dashboards/{dashId}/subscription           | Create dashboard subscription            |
| [**delete_using_delete2**](SubscriptionsApi.md#delete_using_delete2)               | **DELETE** /users-web/api/v3/subscriptions/{updateableSubscriptionId} | Delete subscription                      |
| [**list_using_get3**](SubscriptionsApi.md#list_using_get3)                         | **GET** /users-web/api/v3/apps/{appId}/subscriptions                  | Get subscriptions for an App             |
| [**list_using_get5**](SubscriptionsApi.md#list_using_get5)                         | **GET** /users-web/api/v3/subscriptions                               | Get current account&#x27;s subscriptions |
| [**send_app_report_using_post**](SubscriptionsApi.md#send_app_report_using_post)   | **POST** /users-web/api/v3/apps/{appId}/report/send                   | Email an App report                      |
| [**send_dash_report_using_post**](SubscriptionsApi.md#send_dash_report_using_post) | **POST** /users-web/api/v3/dashboards/{dashId}/report/send            | Email a dashboard report                 |
| [**toggle_enabled_using_put1**](SubscriptionsApi.md#toggle_enabled_using_put1)     | **PUT** /users-web/api/v3/subscriptions/{updateableSubscriptionId}    | Toggle subscription status               |
| [**update_for_app_using_put**](SubscriptionsApi.md#update_for_app_using_put)       | **PUT** /users-web/api/v3/apps/{appId}/subscription                   | Update App subscription                  |
| [**update_for_dash_using_put1**](SubscriptionsApi.md#update_for_dash_using_put1)   | **PUT** /users-web/api/v3/dashboards/{dashId}/subscription            | Update dashboard subscription            |

# **create_for_app_using_post**

> SubscriptionResponse create_for_app_using_post(body, app_id)

Create App subscription

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
body = stcloud.SubscriptionDto() # SubscriptionDto | subscription
app_id = 789 # int | appId

try:
    # Create App subscription
    api_response = api_instance.create_for_app_using_post(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_for_app_using_post: %s\n" % e)
```

### Parameters

| Name       | Type                                      | Description  | Notes |
| ---------- | ----------------------------------------- | ------------ | ----- |
| **body**   | [**SubscriptionDto**](SubscriptionDto.md) | subscription |
| **app_id** | **int**                                   | appId        |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_for_dash_using_post1**

> SubscriptionResponse create_for_dash_using_post1(body, dash_id)

Create dashboard subscription

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
body = stcloud.SubscriptionDashboardDto() # SubscriptionDashboardDto | subscription
dash_id = 789 # int | dashId

try:
    # Create dashboard subscription
    api_response = api_instance.create_for_dash_using_post1(body, dash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->create_for_dash_using_post1: %s\n" % e)
```

### Parameters

| Name        | Type                                                        | Description  | Notes |
| ----------- | ----------------------------------------------------------- | ------------ | ----- |
| **body**    | [**SubscriptionDashboardDto**](SubscriptionDashboardDto.md) | subscription |
| **dash_id** | **int**                                                     | dashId       |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_using_delete2**

> GenericMapBasedApiResponse delete_using_delete2(updateable_subscription_id)

Delete subscription

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
updateable_subscription_id = 789 # int | updateableSubscriptionId

try:
    # Delete subscription
    api_response = api_instance.delete_using_delete2(updateable_subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->delete_using_delete2: %s\n" % e)
```

### Parameters

| Name                           | Type    | Description              | Notes |
| ------------------------------ | ------- | ------------------------ | ----- |
| **updateable_subscription_id** | **int** | updateableSubscriptionId |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get3**

> SubscriptionsResponse list_using_get3(app_id)

Get subscriptions for an App

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
    # Get subscriptions for an App
    api_response = api_instance.list_using_get3(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_using_get3: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **app_id** | **int** | appId       |

### Return type

[**SubscriptionsResponse**](SubscriptionsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get5**

> SubscriptionsResponse list_using_get5()

Get current account's subscriptions

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

try:
    # Get current account's subscriptions
    api_response = api_instance.list_using_get5()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->list_using_get5: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**SubscriptionsResponse**](SubscriptionsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_app_report_using_post**

> MailReportResponse send_app_report_using_post(body, app_id)

Email an App report

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
body = stcloud.ReportInfo() # ReportInfo | emailDto
app_id = 789 # int | appId

try:
    # Email an App report
    api_response = api_instance.send_app_report_using_post(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->send_app_report_using_post: %s\n" % e)
```

### Parameters

| Name       | Type                            | Description | Notes |
| ---------- | ------------------------------- | ----------- | ----- |
| **body**   | [**ReportInfo**](ReportInfo.md) | emailDto    |
| **app_id** | **int**                         | appId       |

### Return type

[**MailReportResponse**](MailReportResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **send_dash_report_using_post**

> MailReportResponse send_dash_report_using_post(body, dash_id)

Email a dashboard report

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
body = stcloud.ReportInfo() # ReportInfo | emailDto
dash_id = 789 # int | dashId

try:
    # Email a dashboard report
    api_response = api_instance.send_dash_report_using_post(body, dash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->send_dash_report_using_post: %s\n" % e)
```

### Parameters

| Name        | Type                            | Description | Notes |
| ----------- | ------------------------------- | ----------- | ----- |
| **body**    | [**ReportInfo**](ReportInfo.md) | emailDto    |
| **dash_id** | **int**                         | dashId      |

### Return type

[**MailReportResponse**](MailReportResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **toggle_enabled_using_put1**

> SubscriptionResponse toggle_enabled_using_put1(body, updateable_subscription_id)

Toggle subscription status

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
body = stcloud.UpdateSubscriptionDto() # UpdateSubscriptionDto | dto
updateable_subscription_id = 789 # int | updateableSubscriptionId

try:
    # Toggle subscription status
    api_response = api_instance.toggle_enabled_using_put1(body, updateable_subscription_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->toggle_enabled_using_put1: %s\n" % e)
```

### Parameters

| Name                           | Type                                                  | Description              | Notes |
| ------------------------------ | ----------------------------------------------------- | ------------------------ | ----- |
| **body**                       | [**UpdateSubscriptionDto**](UpdateSubscriptionDto.md) | dto                      |
| **updateable_subscription_id** | **int**                                               | updateableSubscriptionId |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_for_app_using_put**

> SubscriptionResponse update_for_app_using_put(body, app_id)

Update App subscription

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
body = stcloud.SubscriptionDto() # SubscriptionDto | subscription
app_id = 789 # int | appId

try:
    # Update App subscription
    api_response = api_instance.update_for_app_using_put(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_for_app_using_put: %s\n" % e)
```

### Parameters

| Name       | Type                                      | Description  | Notes |
| ---------- | ----------------------------------------- | ------------ | ----- |
| **body**   | [**SubscriptionDto**](SubscriptionDto.md) | subscription |
| **app_id** | **int**                                   | appId        |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_for_dash_using_put1**

> SubscriptionResponse update_for_dash_using_put1(body, dash_id)

Update dashboard subscription

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
body = stcloud.SubscriptionDashboardDto() # SubscriptionDashboardDto | subscription
dash_id = 789 # int | dashId

try:
    # Update dashboard subscription
    api_response = api_instance.update_for_dash_using_put1(body, dash_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubscriptionsApi->update_for_dash_using_put1: %s\n" % e)
```

### Parameters

| Name        | Type                                                        | Description  | Notes |
| ----------- | ----------------------------------------------------------- | ------------ | ----- |
| **body**    | [**SubscriptionDashboardDto**](SubscriptionDashboardDto.md) | subscription |
| **dash_id** | **int**                                                     | dashId       |

### Return type

[**SubscriptionResponse**](SubscriptionResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
