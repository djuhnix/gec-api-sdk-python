# gec_api_sdk.MemberPublicViewApi

All URIs are relative to *https://multisegmented-diane-superexpressively.ngrok-free.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_public_member**](MemberPublicViewApi.md#get_public_member) | **GET** /api/public/members/{id} | Retrieves a MemberPublicView resource.
[**list_public_members**](MemberPublicViewApi.md#list_public_members) | **GET** /api/public/members | Retrieves the collection of MemberPublicView resources.


# **get_public_member**
> MemberPublicViewPublicRead get_public_member(id)

Retrieves a MemberPublicView resource.

Retrieves a MemberPublicView resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.member_public_view_public_read import MemberPublicViewPublicRead
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://multisegmented-diane-superexpressively.ngrok-free.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "https://multisegmented-diane-superexpressively.ngrok-free.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = gec_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gec_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gec_api_sdk.MemberPublicViewApi(api_client)
    id = 'id_example' # str | MemberPublicView identifier

    try:
        # Retrieves a MemberPublicView resource.
        api_response = api_instance.get_public_member(id)
        print("The response of MemberPublicViewApi->get_public_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPublicViewApi->get_public_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| MemberPublicView identifier | 

### Return type

[**MemberPublicViewPublicRead**](MemberPublicViewPublicRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberPublicView resource |  -  |
**403** | Forbidden |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_public_members**
> List[MemberPublicViewPublicRead] list_public_members(page=page)

Retrieves the collection of MemberPublicView resources.

Retrieves the collection of MemberPublicView resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.member_public_view_public_read import MemberPublicViewPublicRead
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://multisegmented-diane-superexpressively.ngrok-free.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "https://multisegmented-diane-superexpressively.ngrok-free.dev"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): JWT
configuration = gec_api_sdk.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with gec_api_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = gec_api_sdk.MemberPublicViewApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of MemberPublicView resources.
        api_response = api_instance.list_public_members(page=page)
        print("The response of MemberPublicViewApi->list_public_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberPublicViewApi->list_public_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[MemberPublicViewPublicRead]**](MemberPublicViewPublicRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | MemberPublicView collection |  -  |
**403** | Forbidden |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

