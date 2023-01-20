# ducksms_api.SmsScheduleApi

All URIs are relative to *https://ducksms.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_sms_schedule**](SmsScheduleApi.md#cancel_sms_schedule) | **DELETE** /api/v1/sms/scheduled/{id} | Cancel Sms Schedule
[**list_sms_schedule**](SmsScheduleApi.md#list_sms_schedule) | **GET** /api/v1/sms/scheduled | List Sms Schedule


# **cancel_sms_schedule**
> CancelSmsSchedule cancel_sms_schedule(id)

Cancel Sms Schedule

Cancel existing sms schedule

### Example

```python
from __future__ import print_function
import time
import ducksms_api
from ducksms_api.rest import ApiException
from pprint import pprint


# Enter a context with an instance of the API client
with ducksms_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ducksms_api.SmsScheduleApi(api_client)
    id = 'id_example' # str |  (required)

    try:
        # Cancel Sms Schedule
        api_response = api_instance.cancel_sms_schedule(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmsScheduleApi->cancel_sms_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CancelSmsSchedule**](CancelSmsSchedule.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Cancel existing sms schedule |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sms_schedule**
> ListSmsSchedule list_sms_schedule(page=page, filter_sender_name=filter_sender_name, filter_type=filter_type, filter_message_type=filter_message_type, filter_status=filter_status)

List Sms Schedule

List all the sms schedule

### Example

```python
from __future__ import print_function
import time
import ducksms_api
from ducksms_api.rest import ApiException
from pprint import pprint


# Enter a context with an instance of the API client
with ducksms_api.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ducksms_api.SmsScheduleApi(api_client)
    page = 1 # int | Page number
    filter_sender_name = 'DUCKSMS' # str | Filter by sender id name
    filter_type = 'quick' # str | Filter by sms type
    filter_message_type = 'ascii' # str | Filter by sms message type
    filter_status = 'pending' # str | Filter by sms status

    try:
        # List Sms Schedule
        api_response = api_instance.list_sms_schedule(page=page, filter_sender_name=filter_sender_name, filter_type=filter_type, filter_message_type=filter_message_type, filter_status=filter_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmsScheduleApi->list_sms_schedule: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **filter_sender_name** | **str**| Filter by sender id name | [optional] 
 **filter_type** | **str**| Filter by sms type | [optional] 
 **filter_message_type** | **str**| Filter by sms message type | [optional] 
 **filter_status** | **str**| Filter by sms status | [optional] 

### Return type

[**ListSmsSchedule**](ListSmsSchedule.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all the sms schedule |  * X-Pagination-Count - Total data count <br>  * X-Pagination-Page - Pagination page number <br>  * X-Pagination-Limit - Pagination limit per page <br>  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

