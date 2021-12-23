# stcloud.BillingApi

All URIs are relative to */*

| Method                                                                               | HTTP request                                                       | Description            |
| ------------------------------------------------------------------------------------ | ------------------------------------------------------------------ | ---------------------- |
| [**get_detailed_invoice_using_get**](BillingApi.md#get_detailed_invoice_using_get)   | **GET** /users-web/api/v3/billing/invoice/{service}/{year}/{month} | Get invoice details    |
| [**list_available_plans_using_get1**](BillingApi.md#list_available_plans_using_get1) | **GET** /users-web/api/v3/billing/availablePlans                   | Get available plans    |
| [**update_plan_using_put**](BillingApi.md#update_plan_using_put)                     | **PUT** /users-web/api/v3/billing/info/{appId}                     | Update plan for an app |

# **get_detailed_invoice_using_get**

> InvoiceResponse get_detailed_invoice_using_get(service, year, month)

Get invoice details

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
api_instance = stcloud.BillingApi(stcloud.ApiClient(configuration))
service = 'service_example' # str | service
year = 56 # int | year
month = 56 # int | month

try:
    # Get invoice details
    api_response = api_instance.get_detailed_invoice_using_get(service, year, month)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->get_detailed_invoice_using_get: %s\n" % e)
```

### Parameters

| Name        | Type    | Description | Notes |
| ----------- | ------- | ----------- | ----- |
| **service** | **str** | service     |
| **year**    | **int** | year        |
| **month**   | **int** | month       |

### Return type

[**InvoiceResponse**](InvoiceResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_available_plans_using_get1**

> PlansResponse list_available_plans_using_get1(integration_id=integration_id, app_type=app_type)

Get available plans

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
api_instance = stcloud.BillingApi(stcloud.ApiClient(configuration))
integration_id = 789 # int | integrationId (optional)
app_type = 'app_type_example' # str | appType (optional)

try:
    # Get available plans
    api_response = api_instance.list_available_plans_using_get1(integration_id=integration_id, app_type=app_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->list_available_plans_using_get1: %s\n" % e)
```

### Parameters

| Name               | Type    | Description   | Notes      |
| ------------------ | ------- | ------------- | ---------- |
| **integration_id** | **int** | integrationId | [optional] |
| **app_type**       | **str** | appType       | [optional] |

### Return type

[**PlansResponse**](PlansResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: Not defined
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_plan_using_put**

> UpdatePlanResponse update_plan_using_put(body, app_id)

Update plan for an app

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
api_instance = stcloud.BillingApi(stcloud.ApiClient(configuration))
body = stcloud.BillingInfo() # BillingInfo | dto
app_id = 789 # int | appId

try:
    # Update plan for an app
    api_response = api_instance.update_plan_using_put(body, app_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BillingApi->update_plan_using_put: %s\n" % e)
```

### Parameters

| Name       | Type                              | Description | Notes |
| ---------- | --------------------------------- | ----------- | ----- |
| **body**   | [**BillingInfo**](BillingInfo.md) | dto         |
| **app_id** | **int**                           | appId       |

### Return type

[**UpdatePlanResponse**](UpdatePlanResponse.md)

### Authorization

[api_key](../README.md#api_key)

### HTTP request headers

- **Content-Type**: application/json
- **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)
