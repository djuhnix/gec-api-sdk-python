# gec_api_sdk.RsvpApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_rsvp**](RsvpApi.md#create_rsvp) | **POST** /api/rsvps | Creates a Rsvp resource.
[**delete_rsvp**](RsvpApi.md#delete_rsvp) | **DELETE** /api/rsvps | Removes the Rsvp resource.
[**list_rsvps**](RsvpApi.md#list_rsvps) | **GET** /api/rsvps | Retrieves the collection of Rsvp resources.
[**update_rsvp**](RsvpApi.md#update_rsvp) | **PUT** /api/rsvps | Replaces the Rsvp resource.


# **create_rsvp**
> RsvpRead create_rsvp(rsvp_write)

Creates a Rsvp resource.

Creates a Rsvp resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvp_read import RsvpRead
from gec_api_sdk.models.rsvp_write import RsvpWrite
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
    api_instance = gec_api_sdk.RsvpApi(api_client)
    rsvp_write = gec_api_sdk.RsvpWrite() # RsvpWrite | The new Rsvp resource

    try:
        # Creates a Rsvp resource.
        api_response = api_instance.create_rsvp(rsvp_write)
        print("The response of RsvpApi->create_rsvp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpApi->create_rsvp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsvp_write** | [**RsvpWrite**](RsvpWrite.md)| The new Rsvp resource | 

### Return type

[**RsvpRead**](RsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Rsvp resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_rsvp**
> delete_rsvp()

Removes the Rsvp resource.

Removes the Rsvp resource.

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
    api_instance = gec_api_sdk.RsvpApi(api_client)

    try:
        # Removes the Rsvp resource.
        api_instance.delete_rsvp()
    except Exception as e:
        print("Exception when calling RsvpApi->delete_rsvp: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

void (empty response body)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Rsvp resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_rsvps**
> List[RsvpRead] list_rsvps(page=page)

Retrieves the collection of Rsvp resources.

Retrieves the collection of Rsvp resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvp_read import RsvpRead
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
    api_instance = gec_api_sdk.RsvpApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Rsvp resources.
        api_response = api_instance.list_rsvps(page=page)
        print("The response of RsvpApi->list_rsvps:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpApi->list_rsvps: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[RsvpRead]**](RsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rsvp collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_rsvp**
> RsvpRead update_rsvp(rsvp_write)

Replaces the Rsvp resource.

Replaces the Rsvp resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvp_read import RsvpRead
from gec_api_sdk.models.rsvp_write import RsvpWrite
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
    api_instance = gec_api_sdk.RsvpApi(api_client)
    rsvp_write = gec_api_sdk.RsvpWrite() # RsvpWrite | The updated Rsvp resource

    try:
        # Replaces the Rsvp resource.
        api_response = api_instance.update_rsvp(rsvp_write)
        print("The response of RsvpApi->update_rsvp:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpApi->update_rsvp: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsvp_write** | [**RsvpWrite**](RsvpWrite.md)| The updated Rsvp resource | 

### Return type

[**RsvpRead**](RsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Rsvp resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

