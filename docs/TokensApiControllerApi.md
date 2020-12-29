# stcloud.TokensApiControllerApi

All URIs are relative to *https://localhost*

| Method                                                                       | HTTP request                                                        | Description                               |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------- |
| [**create_app_token1**](TokensApiControllerApi.md#create_app_token1)         | **POST** /users-web/api/v3/apps/{appId}/tokens                      | Create new app token                      |
| [**delete_app_token1**](TokensApiControllerApi.md#delete_app_token1)         | **DELETE** /users-web/api/v3/apps/{appId}/tokens/{tokenId}          | Delete app token                          |
| [**get_app_tokens**](TokensApiControllerApi.md#get_app_tokens)               | **GET** /users-web/api/v3/apps/{appId}/tokens                       | Get app available tokens                  |
| [**regenerate_app_token1**](TokensApiControllerApi.md#regenerate_app_token1) | **POST** /users-web/api/v3/apps/{appId}/tokens/{tokenId}/regenerate | Regenerate app token)                     |
| [**update_app_token**](TokensApiControllerApi.md#update_app_token)           | **PUT** /users-web/api/v3/apps/{appId}/tokens/{tokenId}             | Update app token (enable/disable or name) |


# **create_app_token1**
> GenericApiResponse create_app_token1(app_id, dto)

Create new app token

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
api_instance = stcloud.TokensApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
dto = stcloud.CreateTokenDto() # CreateTokenDto | dto

try:
    # Create new app token
    api_response = api_instance.create_app_token1(app_id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->create_app_token1: %s\n" % e)
```

### Parameters

| Name       | Type                                    | Description | Notes |
| ---------- | --------------------------------------- | ----------- | ----- |
| **app_id** | **int**                                 | appId       |
| **dto**    | [**CreateTokenDto**](CreateTokenDto.md) | dto         |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_token1**
> GenericApiResponse delete_app_token1(app_id, token_id)

Delete app token

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
api_instance = stcloud.TokensApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
token_id = 789 # int | tokenId

try:
    # Delete app token
    api_response = api_instance.delete_app_token1(app_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->delete_app_token1: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **app_id**   | **int** | appId       |
| **token_id** | **int** | tokenId     |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_tokens**
> GenericApiResponse get_app_tokens(app_id)

Get app available tokens

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
api_instance = stcloud.TokensApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId

try:
    # Get app available tokens
    api_response = api_instance.get_app_tokens(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->get_app_tokens: %s\n" % e)
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

# **regenerate_app_token1**
> GenericApiResponse regenerate_app_token1(app_id, token_id)

Regenerate app token)

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
api_instance = stcloud.TokensApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
token_id = 789 # int | tokenId

try:
    # Regenerate app token)
    api_response = api_instance.regenerate_app_token1(app_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->regenerate_app_token1: %s\n" % e)
```

### Parameters

| Name         | Type    | Description | Notes |
| ------------ | ------- | ----------- | ----- |
| **app_id**   | **int** | appId       |
| **token_id** | **int** | tokenId     |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_token**
> GenericApiResponse update_app_token(app_id, token_id, dto)

Update app token (enable/disable or name)

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
api_instance = stcloud.TokensApiControllerApi(stcloud.ApiClient(configuration))
app_id = 789 # int | appId
token_id = 789 # int | tokenId
dto = stcloud.UpdateTokenDto() # UpdateTokenDto | dto

try:
    # Update app token (enable/disable or name)
    api_response = api_instance.update_app_token(app_id, token_id, dto)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->update_app_token: %s\n" % e)
```

### Parameters

| Name         | Type                                    | Description | Notes |
| ------------ | --------------------------------------- | ----------- | ----- |
| **app_id**   | **int**                                 | appId       |
| **token_id** | **int**                                 | tokenId     |
| **dto**      | [**UpdateTokenDto**](UpdateTokenDto.md) | dto         |

### Return type

[**GenericApiResponse**](GenericApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
