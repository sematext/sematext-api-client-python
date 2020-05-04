# stcloud.AlertNotificationsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_alert_notifications_for_app_using_post**](AlertNotificationsApi.md#get_alert_notifications_for_app_using_post) | **POST** /users-web/api/v3/apps/{appId}/notifications/alerts | Get alert notifications for an app
[**get_alert_notifications_for_user_using_post**](AlertNotificationsApi.md#get_alert_notifications_for_user_using_post) | **POST** /users-web/api/v3/notifications/alerts | Get alert notifications for a user


# **get_alert_notifications_for_app_using_post**
> GenericApiResponse get_alert_notifications_for_app_using_post(app_id, time_interval)

Get alert notifications for an app

Default value of interval is 1d

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
api_instance = stcloud.AlertNotificationsApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
time_interval = stcloud.AlertNotificationRequest() # AlertNotificationRequest | Time Interval

try:
    # Get alert notifications for an app
    api_response = api_instance.get_alert_notifications_for_app_using_post(app_id, time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertNotificationsApi->get_alert_notifications_for_app_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **int**| appId | 
 **time_interval** | [**AlertNotificationRequest**](AlertNotificationRequest.md)| Time Interval | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_alert_notifications_for_user_using_post**
> GenericApiResponse get_alert_notifications_for_user_using_post(time_interval)

Get alert notifications for a user

Default value of interval is 1d

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
api_instance = stcloud.AlertNotificationsApi(stcloud.ApiClient(configuration))
time_interval = stcloud.AlertNotificationRequest() # AlertNotificationRequest | Time Interval

try:
    # Get alert notifications for a user
    api_response = api_instance.get_alert_notifications_for_user_using_post(time_interval)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AlertNotificationsApi->get_alert_notifications_for_user_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time_interval** | [**AlertNotificationRequest**](AlertNotificationRequest.md)| Time Interval | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

