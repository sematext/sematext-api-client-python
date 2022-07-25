# stcloud.AppsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_using_delete**](AppsApi.md#delete_using_delete) | **DELETE** /users-web/api/v3/apps/{anyStateAppId} | delete
[**get_app_types_using_get**](AppsApi.md#get_app_types_using_get) | **GET** /users-web/api/v3/apps/types | Get all App types supported for the account identified with apiKey
[**get_using_get**](AppsApi.md#get_using_get) | **GET** /users-web/api/v3/apps/{anyStateAppId} | Gets defails for one particular App
[**invite_app_guests_using_post1**](AppsApi.md#invite_app_guests_using_post1) | **POST** /users-web/api/v3/apps/guests | Invite guests to an app
[**list_apps_users_using_get1**](AppsApi.md#list_apps_users_using_get1) | **GET** /users-web/api/v3/apps/users | Get all users of apps accessible to this account
[**list_using_get**](AppsApi.md#list_using_get) | **GET** /users-web/api/v3/apps | Get all apps accessible by account identified with apiKey
[**update_description_using_put1**](AppsApi.md#update_description_using_put1) | **PUT** /users-web/api/v3/apps/{anyStateAppId}/description | Update description of the app
[**update_using_put3**](AppsApi.md#update_using_put3) | **PUT** /users-web/api/v3/apps/{anyStateAppId} | Update app

# **delete_using_delete**

> GenericMapBasedApiResponse delete_using_delete(any_state_app_id)

delete

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))
any_state_app_id = 789 # int | anyStateAppId

try:
    # delete
    api_response = api_instance.delete_using_delete(any_state_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->delete_using_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any_state_app_id** | **int**| anyStateAppId |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_types_using_get**

> AppTypesResponse get_app_types_using_get()

Get all App types supported for the account identified with apiKey

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))

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

[**AppTypesResponse**](AppTypesResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get**

> AppResponse get_using_get(any_state_app_id)

Gets defails for one particular App

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))
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

[**AppResponse**](AppResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invite_app_guests_using_post1**

> GenericMapBasedApiResponse invite_app_guests_using_post1(body)

Invite guests to an app

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))
body = stcloud.Invitation() # Invitation | For `app` and `apps` fields only `id` needs to be populated.Other fields can be left empty or with default values

try:
    # Invite guests to an app
    api_response = api_instance.invite_app_guests_using_post1(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->invite_app_guests_using_post1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**Invitation**](Invitation.md)| For &#x60;app&#x60; and &#x60;apps&#x60; fields only &#x60;id&#x60; needs to be populated.Other fields can be left empty or with default values |

### Return type

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_apps_users_using_get1**

> AppsResponse list_apps_users_using_get1()

Get all users of apps accessible to this account

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))

try:
    # Get all users of apps accessible to this account
    api_response = api_instance.list_apps_users_using_get1()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->list_apps_users_using_get1: %s\n" % e)
```

### Parameters

This endpoint does not need any parameter.

### Return type

[**AppsResponse**](AppsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_using_get**

> AppsResponse list_using_get()

Get all apps accessible by account identified with apiKey

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))

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

[**AppsResponse**](AppsResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_description_using_put1**

> AppResponse update_description_using_put1(any_state_app_id, body=body)

Update description of the app

App can be in any state

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))
any_state_app_id = 789 # int | App Id
body = stcloud.AppDescription() # AppDescription | Update Details (optional)

try:
    # Update description of the app
    api_response = api_instance.update_description_using_put1(any_state_app_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_description_using_put1: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **any_state_app_id** | **int**| App Id |
 **body** | [**AppDescription**](AppDescription.md)| Update Details | [optional]

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_using_put3**

> AppResponse update_using_put3(body, any_state_app_id)

Update app

App can be in any state

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
api_instance = stcloud.AppsApi(stcloud.ApiClient(configuration))
body = stcloud.UpdateAppInfo() # UpdateAppInfo | dto
any_state_app_id = 789 # int | App Id

try:
    # Update app
    api_response = api_instance.update_using_put3(body, any_state_app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AppsApi->update_using_put3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateAppInfo**](UpdateAppInfo.md)| dto |
 **any_state_app_id** | **int**| App Id |

### Return type

[**AppResponse**](AppResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
