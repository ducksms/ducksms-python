# ducksms_api.CreditApi

All URIs are relative to *https://ducksms.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**credit_balance**](CreditApi.md#credit_balance) | **GET** /api/v1/credits/balance | Credit Balance
[**credit_history**](CreditApi.md#credit_history) | **GET** /api/v1/credits/history | Credit History


# **credit_balance**
> CreditBalance credit_balance()

Credit Balance

Get available credit balance

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
    api_instance = ducksms_api.CreditApi(api_client)

    try:
        # Credit Balance
        api_response = api_instance.credit_balance()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CreditApi->credit_balance: %s\n" % e)
```


### Parameters
This endpoint does not need any parameter.

### Return type

[**CreditBalance**](CreditBalance.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get available credit balance |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **credit_history**
> CreditHistory credit_history(page=page, filter_type=filter_type, filter_sms_smsid=filter_sms_smsid)

Credit History

Get all credit history

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
    api_instance = ducksms_api.CreditApi(api_client)
    page = 1 # int | Page number
    filter_type = 'credit' # str | Filter by credit type
    filter_sms_smsid = 1009771270 # int | Filter by sms id

    try:
        # Credit History
        api_response = api_instance.credit_history(page=page, filter_type=filter_type, filter_sms_smsid=filter_sms_smsid)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling CreditApi->credit_history: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **filter_type** | **str**| Filter by credit type | [optional] 
 **filter_sms_smsid** | **int**| Filter by sms id | [optional] 

### Return type

[**CreditHistory**](CreditHistory.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all the credit history |  * X-Pagination-Count - Total data count <br>  * X-Pagination-Page - Pagination page number <br>  * X-Pagination-Limit - Pagination limit per page <br>  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

