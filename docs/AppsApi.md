# swagger_client.AppsApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_app_types_using_get**](AppsApi.md#get_app_types_using_get) | **GET** /users-web/api/v3/apps/types | Get all App types supported for the account identified with apiKey
[**get_using_get**](AppsApi.md#get_using_get) | **GET** /users-web/api/v3/apps/{anyStateAppId} | Gets defails for one particular App
[**invite_app_guests_using_post**](AppsApi.md#invite_app_guests_using_post) | **POST** /users-web/api/v3/apps/guests | Invite guests to an app
[**list_apps_users_using_get**](AppsApi.md#list_apps_users_using_get) | **GET** /users-web/api/v3/apps/users | Get all users of apps accessible to this account
[**list_using_get**](AppsApi.md#list_using_get) | **GET** /users-web/api/v3/apps | Get all apps accessible by account identified with apiKey
[**update_description_using_put**](AppsApi.md#update_description_using_put) | **PUT** /users-web/api/v3/apps/{anyStateAppId}/description | Update description of the app
[**update_using_put1**](AppsApi.md#update_using_put1) | **PUT** /users-web/api/v3/apps/{anyStateAppId} | Update app


# **get_app_types_using_get**
> GenericApiResponse get_app_types_using_get()

Get all App types supported for the account identified with apiKey

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))

try:
    # Get all App types supported for the account identified with apiKey
    api_response = api_instance.get_app_types_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_app_types_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get**
> GenericApiResponse get_using_get(any_state_app_id)

Gets defails for one particular App

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
any_state_app_id = 789 # int | anyStateAppId

try:
    # Gets defails for one particular App
    api_response = api_instance.get_using_get(any_state_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->get_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any_state_app_id** | **int**| anyStateAppId | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_app_guests_using_post**
> GenericApiResponse invite_app_guests_using_post(invitation)

Invite guests to an app

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
invitation = swagger_client.Invitation() # Invitation | For `app` and `apps` fields only `id` needs to be populated.Other fields can be left empty or with default values

try:
    # Invite guests to an app
    api_response = api_instance.invite_app_guests_using_post(invitation)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->invite_app_guests_using_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **invitation** | [**Invitation**](Invitation.md)| For &#x60;app&#x60; and &#x60;apps&#x60; fields only &#x60;id&#x60; needs to be populated.Other fields can be left empty or with default values | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps_users_using_get**
> GenericApiResponse list_apps_users_using_get()

Get all users of apps accessible to this account

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))

try:
    # Get all users of apps accessible to this account
    api_response = api_instance.list_apps_users_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_apps_users_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get**
> GenericApiResponse list_using_get()

Get all apps accessible by account identified with apiKey

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))

try:
    # Get all apps accessible by account identified with apiKey
    api_response = api_instance.list_using_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_using_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_description_using_put**
> GenericApiResponse update_description_using_put(any_state_app_id, update_details=update_details)

Update description of the app

App can be in any state

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
any_state_app_id = 789 # int | App Id
update_details = swagger_client.AppDescription() # AppDescription | Update Details (optional)

try:
    # Update description of the app
    api_response = api_instance.update_description_using_put(any_state_app_id, update_details=update_details)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_description_using_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any_state_app_id** | **int**| App Id | 
 **update_details** | [**AppDescription**](AppDescription.md)| Update Details | [optional] 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put1**
> GenericApiResponse update_using_put1(dto, any_state_app_id)

Update app

App can be in any state

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
api_instance = swagger_client.AppsApi(swagger_client.ApiClient(configuration))
dto = swagger_client.UpdateAppInfo() # UpdateAppInfo | dto
any_state_app_id = 789 # int | App Id

try:
    # Update app
    api_response = api_instance.update_using_put1(dto, any_state_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dto** | [**UpdateAppInfo**](UpdateAppInfo.md)| dto | 
 **any_state_app_id** | **int**| App Id | 

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

