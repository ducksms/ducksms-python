# ducksms_api.SmsApi

All URIs are relative to *https://ducksms.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sms_send**](SmsApi.md#sms_send) | **POST** /api/v1/sms/send | Send Sms


# **sms_send**
> PreviewSmsSend sms_send(sms_schema=sms_schema)

Send Sms

Create a new sms

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
    api_instance = ducksms_api.SmsApi(api_client)
    sms_schema = ducksms_api.SmsSchema() # SmsSchema | Create a new sms

    try:
        # Send Sms
        api_response = api_instance.sms_send(sms_schema=sms_schema)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SmsApi->sms_send: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sms_schema** | [**SmsSchema**](SmsSchema.md)| Create a new sms | [optional] 

### Return type

[**PreviewSmsSend**](PreviewSmsSend.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sms preview |  -  |
**201** | Sms created |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**422** | Validation errors |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

