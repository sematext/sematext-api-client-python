# stcloud.TagApiControllerApi

All URIs are relative to *https://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tag_names_using_get**](TagApiControllerApi.md#get_tag_names_using_get) | **GET** /spm-reports/api/v3/apps/{appIds}/tagNames | Gets tag names for the given application identifiers appearing in the given time frame.
[**get_using_get2**](TagApiControllerApi.md#get_using_get2) | **GET** /spm-reports/api/v3/apps/{appIds}/metrics/filters | Gets values for specified tags for the given application identifiers appearing in the given time frame.
[**get_using_get3**](TagApiControllerApi.md#get_using_get3) | **GET** /spm-reports/api/v3/apps/{appIds}/tags | Gets values for specified tags for the given application identifiers appearing in the given time frame.


# **get_tag_names_using_get**
> object get_tag_names_using_get(app_ids, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)

Gets tag names for the given application identifiers appearing in the given time frame.

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
api_instance = stcloud.TagApiControllerApi(stcloud.ApiClient(configuration))
app_ids = 'app_ids_example' # str | appIds
_from = 789 # int | from (optional)
to = 789 # int | to (optional)
metrics = true # bool | metrics (optional) (default to true)
logs = true # bool | logs (optional) (default to true)
events = false # bool | events (optional) (default to false)
rum = true # bool | rum (optional) (default to true)

try:
    # Gets tag names for the given application identifiers appearing in the given time frame.
    api_response = api_instance.get_tag_names_using_get(app_ids, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApiControllerApi->get_tag_names_using_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ids** | **str**| appIds | 
 **_from** | **int**| from | [optional] 
 **to** | **int**| to | [optional] 
 **metrics** | **bool**| metrics | [optional] [default to true]
 **logs** | **bool**| logs | [optional] [default to true]
 **events** | **bool**| events | [optional] [default to false]
 **rum** | **bool**| rum | [optional] [default to true]

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get2**
> object get_using_get2(app_ids, tag, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)

Gets values for specified tags for the given application identifiers appearing in the given time frame.

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
api_instance = stcloud.TagApiControllerApi(stcloud.ApiClient(configuration))
app_ids = 'app_ids_example' # str | appIds
tag = ['tag_example'] # list[str] | tag
_from = 789 # int | from (optional)
to = 789 # int | to (optional)
metrics = true # bool | metrics (optional) (default to true)
logs = true # bool | logs (optional) (default to true)
events = false # bool | events (optional) (default to false)
rum = true # bool | rum (optional) (default to true)

try:
    # Gets values for specified tags for the given application identifiers appearing in the given time frame.
    api_response = api_instance.get_using_get2(app_ids, tag, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApiControllerApi->get_using_get2: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ids** | **str**| appIds | 
 **tag** | [**list[str]**](str.md)| tag | 
 **_from** | **int**| from | [optional] 
 **to** | **int**| to | [optional] 
 **metrics** | **bool**| metrics | [optional] [default to true]
 **logs** | **bool**| logs | [optional] [default to true]
 **events** | **bool**| events | [optional] [default to false]
 **rum** | **bool**| rum | [optional] [default to true]

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_using_get3**
> object get_using_get3(app_ids, tag, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)

Gets values for specified tags for the given application identifiers appearing in the given time frame.

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
api_instance = stcloud.TagApiControllerApi(stcloud.ApiClient(configuration))
app_ids = 'app_ids_example' # str | appIds
tag = ['tag_example'] # list[str] | tag
_from = 789 # int | from (optional)
to = 789 # int | to (optional)
metrics = true # bool | metrics (optional) (default to true)
logs = true # bool | logs (optional) (default to true)
events = false # bool | events (optional) (default to false)
rum = true # bool | rum (optional) (default to true)

try:
    # Gets values for specified tags for the given application identifiers appearing in the given time frame.
    api_response = api_instance.get_using_get3(app_ids, tag, _from=_from, to=to, metrics=metrics, logs=logs, events=events, rum=rum)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling TagApiControllerApi->get_using_get3: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_ids** | **str**| appIds | 
 **tag** | [**list[str]**](str.md)| tag | 
 **_from** | **int**| from | [optional] 
 **to** | **int**| to | [optional] 
 **metrics** | **bool**| metrics | [optional] [default to true]
 **logs** | **bool**| logs | [optional] [default to true]
 **events** | **bool**| events | [optional] [default to false]
 **rum** | **bool**| rum | [optional] [default to true]

### Return type

**object**

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

