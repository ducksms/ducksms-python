# ducksms_api.SenderIDApi

All URIs are relative to *https://ducksms.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_sender**](SenderIDApi.md#create_sender) | **POST** /api/v1/senders | Create a Sender ID
[**delete_sender**](SenderIDApi.md#delete_sender) | **DELETE** /api/v1/senders/{id} | Delete a Sender ID
[**get_sender**](SenderIDApi.md#get_sender) | **GET** /api/v1/senders/{id} | Get a single Sender ID
[**list_sender**](SenderIDApi.md#list_sender) | **GET** /api/v1/senders | List Sender ID
[**update_sender**](SenderIDApi.md#update_sender) | **POST** /api/v1/senders/{id} | Update a Sender ID


# **create_sender**
> CreatedSender create_sender(sender=sender)

Create a Sender ID

Create a new sender id

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
    api_instance = ducksms_api.SenderIDApi(api_client)
    sender = ducksms_api.Sender() # Sender | Create a new sender

    try:
        # Create a Sender ID
        api_response = api_instance.create_sender(sender=sender)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SenderIDApi->create_sender: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sender** | [**Sender**](Sender.md)| Create a new sender | [optional] 

### Return type

[**CreatedSender**](CreatedSender.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Sender ID created |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**422** | Validation errors |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_sender**
> DeletedSender delete_sender(id)

Delete a Sender ID

Delete an existing sender id

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
    api_instance = ducksms_api.SenderIDApi(api_client)
    id = 'id_example' # str |  (required)

    try:
        # Delete a Sender ID
        api_response = api_instance.delete_sender(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SenderIDApi->delete_sender: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeletedSender**](DeletedSender.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender deleted |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_sender**
> GetSender get_sender(id)

Get a single Sender ID

Get details on a single sender id

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
    api_instance = ducksms_api.SenderIDApi(api_client)
    id = 'id_example' # str |  (required)

    try:
        # Get a single Sender ID
        api_response = api_instance.get_sender(id)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SenderIDApi->get_sender: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetSender**](GetSender.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Get details on a single sender |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_sender**
> ListSender list_sender(page=page, filter_name=filter_name, filter_status=filter_status)

List Sender ID

List all the senders

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
    api_instance = ducksms_api.SenderIDApi(api_client)
    page = 1 # int | Page number
    filter_name = 'DUCKSMS' # str | Filter by sender name
    filter_status = 'active' # str | Filter by sender status

    try:
        # List Sender ID
        api_response = api_instance.list_sender(page=page, filter_name=filter_name, filter_status=filter_status)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SenderIDApi->list_sender: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| Page number | [optional] 
 **filter_name** | **str**| Filter by sender name | [optional] 
 **filter_status** | **str**| Filter by sender status | [optional] 

### Return type

[**ListSender**](ListSender.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List all the senders |  * X-Pagination-Count - Total data count <br>  * X-Pagination-Page - Pagination page number <br>  * X-Pagination-Limit - Pagination limit per page <br>  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_sender**
> UpdatedSender update_sender(id, sender=sender)

Update a Sender ID

Update an existing sender id

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
    api_instance = ducksms_api.SenderIDApi(api_client)
    id = 'id_example' # str |  (required)
    sender = ducksms_api.Sender() # Sender | Update an existing sender id

    try:
        # Update a Sender ID
        api_response = api_instance.update_sender(id, sender=sender)
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling SenderIDApi->update_sender: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **sender** | [**Sender**](Sender.md)| Update an existing sender id | [optional] 

### Return type

[**UpdatedSender**](UpdatedSender.md)

### Authorization

[BearerToken](../README.md#BearerToken)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Sender updated |  -  |
**400** | Invalid request |  -  |
**401** | Unauthenticated |  -  |
**404** | No data found |  -  |
**422** | Validation errors |  -  |
**500** | Server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

