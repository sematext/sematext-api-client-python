# stcloud.TokensApiControllerApi

All URIs are relative to */*

| Method                                                                       | HTTP request                                                        | Description                               |
| ---------------------------------------------------------------------------- | ------------------------------------------------------------------- | ----------------------------------------- |
| [**create_app_token**](TokensApiControllerApi.md#create_app_token)           | **POST** /users-web/api/v3/apps/{appId}/tokens                      | Create new app token                      |
| [**delete_app_token1**](TokensApiControllerApi.md#delete_app_token1)         | **DELETE** /users-web/api/v3/apps/{appId}/tokens/{tokenId}          | Delete app token                          |
| [**get_app_tokens1**](TokensApiControllerApi.md#get_app_tokens1)             | **GET** /users-web/api/v3/apps/{appId}/tokens                       | Get app available tokens                  |
| [**regenerate_app_token1**](TokensApiControllerApi.md#regenerate_app_token1) | **POST** /users-web/api/v3/apps/{appId}/tokens/{tokenId}/regenerate | Regenerate app token)                     |
| [**update_app_token**](TokensApiControllerApi.md#update_app_token)           | **PUT** /users-web/api/v3/apps/{appId}/tokens/{tokenId}             | Update app token (enable/disable or name) |

# **create_app_token**

> TokenResponse create_app_token(body, app_id)

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
body = stcloud.CreateTokenDto() # CreateTokenDto | dto
app_id = 789 # int | appId

try:
    # Create new app token
    api_response = api_instance.create_app_token(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->create_app_token: %s\n" % e)
```

### Parameters

| Name       | Type                                    | Description | Notes |
| ---------- | --------------------------------------- | ----------- | ----- |
| **body**   | [**CreateTokenDto**](CreateTokenDto.md) | dto         |
| **app_id** | **int**                                 | appId       |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_app_token1**

> GenericMapBasedApiResponse delete_app_token1(app_id, token_id)

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

[**GenericMapBasedApiResponse**](GenericMapBasedApiResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_app_tokens1**

> TokensResponse get_app_tokens1(app_id)

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
    api_response = api_instance.get_app_tokens1(app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->get_app_tokens1: %s\n" % e)
```

### Parameters

| Name       | Type    | Description | Notes |
| ---------- | ------- | ----------- | ----- |
| **app_id** | **int** | appId       |

### Return type

[**TokensResponse**](TokensResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **regenerate_app_token1**

> TokenResponse regenerate_app_token1(app_id, token_id)

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

[**TokenResponse**](TokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_app_token**

> TokenResponse update_app_token(body, app_id, token_id)

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
body = stcloud.UpdateTokenDto() # UpdateTokenDto | dto
app_id = 789 # int | appId
token_id = 789 # int | tokenId

try:
    # Update app token (enable/disable or name)
    api_response = api_instance.update_app_token(body, app_id, token_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TokensApiControllerApi->update_app_token: %s\n" % e)
```

### Parameters

| Name         | Type                                    | Description | Notes |
| ------------ | --------------------------------------- | ----------- | ----- |
| **body**     | [**UpdateTokenDto**](UpdateTokenDto.md) | dto         |
| **app_id**   | **int**                                 | appId       |
| **token_id** | **int**                                 | tokenId     |

### Return type

[**TokenResponse**](TokenResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
