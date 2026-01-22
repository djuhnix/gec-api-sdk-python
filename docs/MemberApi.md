# gec_api_sdk.MemberApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_members_get_collection**](MemberApi.md#api_members_get_collection) | **GET** /api/members | Retrieves the collection of Member resources.
[**api_members_id_delete**](MemberApi.md#api_members_id_delete) | **DELETE** /api/members/{id} | Removes the Member resource.
[**api_members_id_get**](MemberApi.md#api_members_id_get) | **GET** /api/members/{id} | Retrieves a Member resource.
[**api_members_id_put**](MemberApi.md#api_members_id_put) | **PUT** /api/members/{id} | Replaces the Member resource.
[**api_members_post**](MemberApi.md#api_members_post) | **POST** /api/members | Creates a Member resource.


# **api_members_get_collection**
> ApiMembersGetCollection200Response api_members_get_collection(page=page)

Retrieves the collection of Member resources.

Retrieves the collection of Member resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_members_get_collection200_response import ApiMembersGetCollection200Response
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "http://localhost"
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
    api_instance = gec_api_sdk.MemberApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Member resources.
        api_response = api_instance.api_members_get_collection(page=page)
        print("The response of MemberApi->api_members_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api_members_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiMembersGetCollection200Response**](ApiMembersGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_delete**
> api_members_id_delete(id)

Removes the Member resource.

Removes the Member resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "http://localhost"
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
    api_instance = gec_api_sdk.MemberApi(api_client)
    id = 'id_example' # str | Member identifier

    try:
        # Removes the Member resource.
        api_instance.api_members_id_delete(id)
    except Exception as e:
        print("Exception when calling MemberApi->api_members_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Member identifier | 

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Member resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_get**
> MemberJsonldMemberRead api_members_id_get(id)

Retrieves a Member resource.

Retrieves a Member resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.member_jsonld_member_read import MemberJsonldMemberRead
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "http://localhost"
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
    api_instance = gec_api_sdk.MemberApi(api_client)
    id = 'id_example' # str | Member identifier

    try:
        # Retrieves a Member resource.
        api_response = api_instance.api_members_id_get(id)
        print("The response of MemberApi->api_members_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api_members_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Member identifier | 

### Return type

[**MemberJsonldMemberRead**](MemberJsonldMemberRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_id_put**
> MemberJsonldMemberRead api_members_id_put(id, member_jsonld_member_write)

Replaces the Member resource.

Replaces the Member resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.member_jsonld_member_read import MemberJsonldMemberRead
from gec_api_sdk.models.member_jsonld_member_write import MemberJsonldMemberWrite
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "http://localhost"
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
    api_instance = gec_api_sdk.MemberApi(api_client)
    id = 'id_example' # str | Member identifier
    member_jsonld_member_write = gec_api_sdk.MemberJsonldMemberWrite() # MemberJsonldMemberWrite | The updated Member resource

    try:
        # Replaces the Member resource.
        api_response = api_instance.api_members_id_put(id, member_jsonld_member_write)
        print("The response of MemberApi->api_members_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api_members_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Member identifier | 
 **member_jsonld_member_write** | [**MemberJsonldMemberWrite**](MemberJsonldMemberWrite.md)| The updated Member resource | 

### Return type

[**MemberJsonldMemberRead**](MemberJsonldMemberRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Member resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_members_post**
> MemberJsonldMemberRead api_members_post(member_jsonld_member_write)

Creates a Member resource.

Creates a Member resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.member_jsonld_member_read import MemberJsonldMemberRead
from gec_api_sdk.models.member_jsonld_member_write import MemberJsonldMemberWrite
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "http://localhost"
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
    api_instance = gec_api_sdk.MemberApi(api_client)
    member_jsonld_member_write = gec_api_sdk.MemberJsonldMemberWrite() # MemberJsonldMemberWrite | The new Member resource

    try:
        # Creates a Member resource.
        api_response = api_instance.api_members_post(member_jsonld_member_write)
        print("The response of MemberApi->api_members_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MemberApi->api_members_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **member_jsonld_member_write** | [**MemberJsonldMemberWrite**](MemberJsonldMemberWrite.md)| The new Member resource | 

### Return type

[**MemberJsonldMemberRead**](MemberJsonldMemberRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Member resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

