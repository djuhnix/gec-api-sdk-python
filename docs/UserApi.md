# gec_api_sdk.UserApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_users_get_collection**](UserApi.md#api_users_get_collection) | **GET** /api/users | Retrieves the collection of User resources.
[**api_users_id_delete**](UserApi.md#api_users_id_delete) | **DELETE** /api/users/{id} | Removes the User resource.
[**api_users_id_get**](UserApi.md#api_users_id_get) | **GET** /api/users/{id} | Retrieves a User resource.
[**api_users_id_patch**](UserApi.md#api_users_id_patch) | **PATCH** /api/users/{id} | Updates the User resource.
[**api_users_id_put**](UserApi.md#api_users_id_put) | **PUT** /api/users/{id} | Replaces the User resource.
[**api_users_post**](UserApi.md#api_users_post) | **POST** /api/users | Creates a User resource.


# **api_users_get_collection**
> ApiUsersGetCollection200Response api_users_get_collection(page=page)

Retrieves the collection of User resources.

Retrieves the collection of User resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_users_get_collection200_response import ApiUsersGetCollection200Response
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
    api_instance = gec_api_sdk.UserApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of User resources.
        api_response = api_instance.api_users_get_collection(page=page)
        print("The response of UserApi->api_users_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiUsersGetCollection200Response**](ApiUsersGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_delete**
> api_users_id_delete(id)

Removes the User resource.

Removes the User resource.

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
    api_instance = gec_api_sdk.UserApi(api_client)
    id = 'id_example' # str | User identifier

    try:
        # Removes the User resource.
        api_instance.api_users_id_delete(id)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 

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
**204** | User resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_get**
> UserJsonldUserRead api_users_id_get(id)

Retrieves a User resource.

Retrieves a User resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.user_jsonld_user_read import UserJsonldUserRead
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
    api_instance = gec_api_sdk.UserApi(api_client)
    id = 'id_example' # str | User identifier

    try:
        # Retrieves a User resource.
        api_response = api_instance.api_users_id_get(id)
        print("The response of UserApi->api_users_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 

### Return type

[**UserJsonldUserRead**](UserJsonldUserRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_patch**
> UserJsonldUserRead api_users_id_patch(id, user_user_write_json_merge_patch)

Updates the User resource.

Updates the User resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.user_jsonld_user_read import UserJsonldUserRead
from gec_api_sdk.models.user_user_write_json_merge_patch import UserUserWriteJsonMergePatch
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
    api_instance = gec_api_sdk.UserApi(api_client)
    id = 'id_example' # str | User identifier
    user_user_write_json_merge_patch = gec_api_sdk.UserUserWriteJsonMergePatch() # UserUserWriteJsonMergePatch | The updated User resource

    try:
        # Updates the User resource.
        api_response = api_instance.api_users_id_patch(id, user_user_write_json_merge_patch)
        print("The response of UserApi->api_users_id_patch:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_patch: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 
 **user_user_write_json_merge_patch** | [**UserUserWriteJsonMergePatch**](UserUserWriteJsonMergePatch.md)| The updated User resource | 

### Return type

[**UserJsonldUserRead**](UserJsonldUserRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/merge-patch+json
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_id_put**
> UserJsonldUserRead api_users_id_put(id, user_user_write)

Replaces the User resource.

Replaces the User resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.user_jsonld_user_read import UserJsonldUserRead
from gec_api_sdk.models.user_user_write import UserUserWrite
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
    api_instance = gec_api_sdk.UserApi(api_client)
    id = 'id_example' # str | User identifier
    user_user_write = gec_api_sdk.UserUserWrite() # UserUserWrite | The updated User resource

    try:
        # Replaces the User resource.
        api_response = api_instance.api_users_id_put(id, user_user_write)
        print("The response of UserApi->api_users_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| User identifier | 
 **user_user_write** | [**UserUserWrite**](UserUserWrite.md)| The updated User resource | 

### Return type

[**UserJsonldUserRead**](UserJsonldUserRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_users_post**
> UserJsonldUserRead api_users_post(user_user_write)

Creates a User resource.

Creates a User resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.user_jsonld_user_read import UserJsonldUserRead
from gec_api_sdk.models.user_user_write import UserUserWrite
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
    api_instance = gec_api_sdk.UserApi(api_client)
    user_user_write = gec_api_sdk.UserUserWrite() # UserUserWrite | The new User resource

    try:
        # Creates a User resource.
        api_response = api_instance.api_users_post(user_user_write)
        print("The response of UserApi->api_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserApi->api_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_user_write** | [**UserUserWrite**](UserUserWrite.md)| The new User resource | 

### Return type

[**UserJsonldUserRead**](UserJsonldUserRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | User resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

