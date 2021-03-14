# stcloud.AlertsApi

All URIs are relative to */*

| Method                                                                                  | HTTP request                                                 | Description                |
| --------------------------------------------------------------------------------------- | ------------------------------------------------------------ | -------------------------- |
| [**create_alert_using_post1**](AlertsApi.md#create_alert_using_post1)                   | **POST** /users-web/api/v3/alerts                            | Create alert rule          |
| [**delete_alert_rule_using_delete1**](AlertsApi.md#delete_alert_rule_using_delete1)     | **DELETE** /users-web/api/v3/alerts/{updateableAlertId}      | Delete alert rule          |
| [**disable_alert_rule_using_put1**](AlertsApi.md#disable_alert_rule_using_put1)         | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/disable | Disable alert rule         |
| [**enable_alert_rule_using_put1**](AlertsApi.md#enable_alert_rule_using_put1)           | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/enable  | Enable alert rule          |
| [**get_alert_rules_for_app_using_get**](AlertsApi.md#get_alert_rules_for_app_using_get) | **GET** /users-web/api/v3/apps/{appId}/alerts                | Get alert rules for an app |

# **create_alert_using_post1**
> AlertRuleResponse create_alert_using_post1(body)

Create alert rule

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
api_instance = stcloud.AlertsApi(stcloud.ApiClient(configuration))
body = stcloud.AlertRule() # AlertRule | dto

try:
    # Create alert rule
    api_response = api_instance.create_alert_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert_using_post1: %s\n" % e)
```

### Parameters

| Name     | Type                          | Description | Notes |
| -------- | ----------------------------- | ----------- | ----- |
| **body** | [**AlertRule**](AlertRule.md) | dto         |

### Return type

[**AlertRuleResponse**](AlertRuleResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_using_delete1**
> GenericMapBasedApiResponse delete_alert_rule_using_delete1(updateable_alert_id)

Delete alert rule

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
api_instance = stcloud.AlertsApi(stcloud.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Delete alert rule
    api_response = api_instance.delete_alert_rule_using_delete1(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert_rule_using_delete1: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description       | Notes |
| ----------------------- | ------- | ----------------- | ----- |
| **updateable_alert_id** | **int** | updateableAlertId |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alert_rule_using_put1**
> GenericMapBasedApiResponse disable_alert_rule_using_put1(updateable_alert_id)

Disable alert rule

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
api_instance = stcloud.AlertsApi(stcloud.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Disable alert rule
    api_response = api_instance.disable_alert_rule_using_put1(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->disable_alert_rule_using_put1: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description       | Notes |
| ----------------------- | ------- | ----------------- | ----- |
| **updateable_alert_id** | **int** | updateableAlertId |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alert_rule_using_put1**
> GenericMapBasedApiResponse enable_alert_rule_using_put1(updateable_alert_id)

Enable alert rule

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
api_instance = stcloud.AlertsApi(stcloud.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Enable alert rule
    api_response = api_instance.enable_alert_rule_using_put1(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->enable_alert_rule_using_put1: %s\n" % e)
```

### Parameters

| Name                    | Type    | Description       | Notes |
| ----------------------- | ------- | ----------------- | ----- |
| **updateable_alert_id** | **int** | updateableAlertId |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rules_for_app_using_get**
> AlertRulesResponse get_alert_rules_for_app_using_get(app_id)

Get alert rules for an app

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
api_instance = stcloud.AlertsApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get alert rules for an app
    api_response = api_instance.get_alert_rules_for_app_using_get(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert_rules_for_app_using_get: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **app_id** | **int** | appId       |

### Return type

[**AlertRulesResponse**](AlertRulesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
