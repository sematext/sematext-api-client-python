# Sematext Cloud - API Client - sematext-api-python

This client code talks to [Sematext Cloud API](https://sematext.com/cloud/) providing a way to automate setup of solution monitoring.<br>
<br><br>

Further information and API browsing refer to the [Sematext Cloud API web page](https://sematext.com/docs/api/) 


## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Authentication

This client code requires a Sematext API Access token to function. You can find this by logging into your [Sematext Cloud Account](https://apps.sematext.com/ui/account/api)


## Requirements.

Python 2.7 and 3.4+

## Installation & Usage
### pip install

If the python package is hosted on Github, you can install directly from Github

```sh
pip install git+https://github.com/sematext/sematext-api-client-python.git
```
(you may need to run `pip` with root permission: `sudo pip install git+https://github.com/sematext-api-client-python.git`)

Then import the package:
```python
import stcloud 
```

### Testing

```bash
python -m unittest discover
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
python setup.py install --user
```
(or `sudo python setup.py install` to install the package for all users)

Then import the package:
```python
import stcloud
```

## Getting Started

Please follow the [installation procedure](#installation--usage) and then run the following:

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

## Documentation for API Endpoints

All URIs are relative to *https://localhost*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*AlertNotificationsApi* | [**get_alert_notifications_for_app_using_post**](docs/AlertNotificationsApi.md#get_alert_notifications_for_app_using_post) | **POST** /users-web/api/v3/apps/{appId}/notifications/alerts | Get alert notifications for an app
*AlertNotificationsApi* | [**get_alert_notifications_for_user_using_post**](docs/AlertNotificationsApi.md#get_alert_notifications_for_user_using_post) | **POST** /users-web/api/v3/notifications/alerts | Get alert notifications for a user
*AlertsApi* | [**create_alert_using_post**](docs/AlertsApi.md#create_alert_using_post) | **POST** /users-web/api/v3/alerts | Create alert rule
*AlertsApi* | [**delete_alert_rule_using_delete**](docs/AlertsApi.md#delete_alert_rule_using_delete) | **DELETE** /users-web/api/v3/alerts/{updateableAlertId} | Delete alert rule
*AlertsApi* | [**disable_alert_rule_using_put**](docs/AlertsApi.md#disable_alert_rule_using_put) | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/disable | Disable alert rule
*AlertsApi* | [**enable_alert_rule_using_put**](docs/AlertsApi.md#enable_alert_rule_using_put) | **PUT** /users-web/api/v3/alerts/{updateableAlertId}/enable | Enable alert rule
*AlertsApi* | [**get_alert_rules_for_app_using_get**](docs/AlertsApi.md#get_alert_rules_for_app_using_get) | **GET** /users-web/api/v3/apps/{appId}/alerts | Get alert rules for an app
*AppsApi* | [**get_app_types_using_get**](docs/AppsApi.md#get_app_types_using_get) | **GET** /users-web/api/v3/apps/types | Get all App types supported for the account identified with apiKey
*AppsApi* | [**get_using_get**](docs/AppsApi.md#get_using_get) | **GET** /users-web/api/v3/apps/{anyStateAppId} | Gets defails for one particular App
*AppsApi* | [**invite_app_guests_using_post**](docs/AppsApi.md#invite_app_guests_using_post) | **POST** /users-web/api/v3/apps/guests | Invite guests to an app
*AppsApi* | [**list_apps_users_using_get**](docs/AppsApi.md#list_apps_users_using_get) | **GET** /users-web/api/v3/apps/users | Get all users of apps accessible to this account
*AppsApi* | [**list_using_get**](docs/AppsApi.md#list_using_get) | **GET** /users-web/api/v3/apps | Get all apps accessible by account identified with apiKey
*AppsApi* | [**update_description_using_put**](docs/AppsApi.md#update_description_using_put) | **PUT** /users-web/api/v3/apps/{anyStateAppId}/description | Update description of the app
*AppsApi* | [**update_using_put1**](docs/AppsApi.md#update_using_put1) | **PUT** /users-web/api/v3/apps/{anyStateAppId} | Update app
*BillingApi* | [**get_detailed_invoice_using_get**](docs/BillingApi.md#get_detailed_invoice_using_get) | **GET** /users-web/api/v3/billing/invoice/{service}/{year}/{month} | Get invoice details
*BillingApi* | [**list_available_plans_using_get**](docs/BillingApi.md#list_available_plans_using_get) | **GET** /users-web/api/v3/billing/availablePlans | Get available plans
*BillingApi* | [**update_plan_using_put**](docs/BillingApi.md#update_plan_using_put) | **PUT** /users-web/api/v3/billing/info/{appId} | Update plan for an app
*LogsAppApi* | [**create_logsene_application**](docs/LogsAppApi.md#create_logsene_application) | **POST** /logsene-reports/api/v3/apps | Create Logs App
*MetricsApi* | [**list_data_series_using_post1**](docs/MetricsApi.md#list_data_series_using_post1) | **POST** /spm-reports/api/v3/apps/{appId}/metrics/data | Get metrics data points for an app
*MetricsApi* | [**list_filters_using_post**](docs/MetricsApi.md#list_filters_using_post) | **POST** /spm-reports/api/v3/apps/{appId}/metrics/filters | Get metrics filters and their values for an app
*MetricsApi* | [**list_metrics_keys_using_get1**](docs/MetricsApi.md#list_metrics_keys_using_get1) | **GET** /spm-reports/api/v3/apps/{appId}/metrics/keys | Get metrics keys for an app
*MetricsApi* | [**list_metrics_using_get1**](docs/MetricsApi.md#list_metrics_using_get1) | **GET** /spm-reports/api/v3/apps/{appId}/metrics | Get metrics info for an app
*MonitoringAppApi* | [**create_spm_application**](docs/MonitoringAppApi.md#create_spm_application) | **POST** /spm-reports/api/v3/apps | Create Monitoring App
*ResetPasswordApi* | [**reset_password_using_post**](docs/ResetPasswordApi.md#reset_password_using_post) | **POST** /users-web/api/v3/account/password/reset | Reset Password
*SavedQueriesApi* | [**delete_saved_query_using_delete**](docs/SavedQueriesApi.md#delete_saved_query_using_delete) | **DELETE** /users-web/api/v3/savedQueries/{updateableQueryId} | Delete saved query
*SavedQueriesApi* | [**get_saved_queries_for_app_using_get**](docs/SavedQueriesApi.md#get_saved_queries_for_app_using_get) | **GET** /users-web/api/v3/apps/{appId}/savedQueries | Get saved queries for an app
*SavedQueriesApi* | [**save_query_using_post**](docs/SavedQueriesApi.md#save_query_using_post) | **POST** /users-web/api/v3/savedQueries | Create saved query
*SavedQueriesApi* | [**save_query_using_put**](docs/SavedQueriesApi.md#save_query_using_put) | **PUT** /users-web/api/v3/savedQueries/{updateableQueryId} | Update saved query
*SubscriptionsApi* | [**list_using_get1**](docs/SubscriptionsApi.md#list_using_get1) | **GET** /users-web/api/v3/apps/{appId}/subscriptions | Get subscriptions for an app
*SubscriptionsApi* | [**send_report_using_post**](docs/SubscriptionsApi.md#send_report_using_post) | **POST** /users-web/api/v3/apps/{appId}/report/send | Trigger emailing of report for an app
*AwsSettingsControllerApi* | [**update_using_put**](docs/AwsSettingsControllerApi.md#update_using_put) | **PUT** /users-web/api/v3/apps/{appId}/aws | Update App&#39;s AWS CloudWatch settings
*TagApiControllerApi* | [**get_tag_names_using_get**](docs/TagApiControllerApi.md#get_tag_names_using_get) | **GET** /spm-reports/api/v3/apps/{appIds}/tagNames | Gets tag names for the given application identifiers appearing in the given time frame.
*TagApiControllerApi* | [**get_using_get2**](docs/TagApiControllerApi.md#get_using_get2) | **GET** /spm-reports/api/v3/apps/{appIds}/metrics/filters | Gets values for specified tags for the given application identifiers appearing in the given time frame.
*TagApiControllerApi* | [**get_using_get3**](docs/TagApiControllerApi.md#get_using_get3) | **GET** /spm-reports/api/v3/apps/{appIds}/tags | Gets values for specified tags for the given application identifiers appearing in the given time frame.


## Documentation For Models

 - [AlertNotificationRequest](docs/AlertNotificationRequest.md)
 - [AlertRule](docs/AlertRule.md)
 - [AlertRuleScheduleTimeRangeDto](docs/AlertRuleScheduleTimeRangeDto.md)
 - [AlertRuleScheduleWeekdayDto](docs/AlertRuleScheduleWeekdayDto.md)
 - [App](docs/App.md)
 - [AppDescription](docs/AppDescription.md)
 - [AppMetadata](docs/AppMetadata.md)
 - [BasicAuthMethodDto](docs/BasicAuthMethodDto.md)
 - [BasicOrganizationDto](docs/BasicOrganizationDto.md)
 - [BillingInfo](docs/BillingInfo.md)
 - [CloudWatchSettings](docs/CloudWatchSettings.md)
 - [CreateAppInfo](docs/CreateAppInfo.md)
 - [DataSeriesFilter](docs/DataSeriesFilter.md)
 - [DataSeriesRequest](docs/DataSeriesRequest.md)
 - [Error](docs/Error.md)
 - [FilterValue](docs/FilterValue.md)
 - [GenericApiResponse](docs/GenericApiResponse.md)
 - [Invitation](docs/Invitation.md)
 - [NotificationIntegration](docs/NotificationIntegration.md)
 - [Plan](docs/Plan.md)
 - [ReportInfo](docs/ReportInfo.md)
 - [SavedQuery](docs/SavedQuery.md)
 - [ServiceIntegration](docs/ServiceIntegration.md)
 - [UpdateAppInfo](docs/UpdateAppInfo.md)
 - [UserInfo](docs/UserInfo.md)
 - [UserPermissions](docs/UserPermissions.md)
 - [UserRole](docs/UserRole.md)


