# swagger_client.AlertsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_alert_using_post**](AlertsApi.md#create_alert_using_post) | **POST** /users-web/api/v3/alerts | Create alert rule
[**delete_alert_rule_using_delete**](AlertsApi.md#delete_alert_rule_using_delete) | **DELETE** /users-web/api/v3/alerts/{updateableAlertId} | Delete alert rule
[**disable_alert_rule_using_put**](AlertsApi.md#disable_alert_rule_using_put) | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/disable | Disable alert rule
[**enable_alert_rule_using_put**](AlertsApi.md#enable_alert_rule_using_put) | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/enable | Enable alert rule
[**get_alert_rules_for_app_using_get**](AlertsApi.md#get_alert_rules_for_app_using_get) | **GET** /users-web/api/v3/apps/{appId}/alerts | Get alert rules for an app


# **create_alert_using_post**
> GenericApiResponse create_alert_using_post(dto)

Create alert rule

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
dto = swagger_client.AlertRule() # AlertRule | dto

try:
    # Create alert rule
    api_response = api_instance.create_alert_using_post(dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->create_alert_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**AlertRule**](AlertRule.md)| dto | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_alert_rule_using_delete**
> GenericApiResponse delete_alert_rule_using_delete(updateable_alert_id)

Delete alert rule

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Delete alert rule
    api_response = api_instance.delete_alert_rule_using_delete(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->delete_alert_rule_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateable_alert_id** | **int**| updateableAlertId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **disable_alert_rule_using_put**
> GenericApiResponse disable_alert_rule_using_put(updateable_alert_id)

Disable alert rule

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Disable alert rule
    api_response = api_instance.disable_alert_rule_using_put(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->disable_alert_rule_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateable_alert_id** | **int**| updateableAlertId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **enable_alert_rule_using_put**
> GenericApiResponse enable_alert_rule_using_put(updateable_alert_id)

Enable alert rule

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
updateable_alert_id = 789 # int | updateableAlertId

try:
    # Enable alert rule
    api_response = api_instance.enable_alert_rule_using_put(updateable_alert_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->enable_alert_rule_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **updateable_alert_id** | **int**| updateableAlertId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_rules_for_app_using_get**
> GenericApiResponse get_alert_rules_for_app_using_get(app_id)

Get alert rules for an app

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
api_instance = swagger_client.AlertsApi(swagger_client.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get alert rules for an app
    api_response = api_instance.get_alert_rules_for_app_using_get(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertsApi->get_alert_rules_for_app_using_get: %s\n" % e)
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

