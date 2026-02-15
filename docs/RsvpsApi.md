# gec_api_sdk.RsvpsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_rsvps_get_collection**](RsvpsApi.md#api_rsvps_get_collection) | **GET** /api/rsvps | Retrieves the collection of rsvps resources.
[**api_rsvps_id_delete**](RsvpsApi.md#api_rsvps_id_delete) | **DELETE** /api/rsvps/{id} | Removes the rsvps resource.
[**api_rsvps_id_get**](RsvpsApi.md#api_rsvps_id_get) | **GET** /api/rsvps/{id} | Retrieves a rsvps resource.
[**api_rsvps_id_put**](RsvpsApi.md#api_rsvps_id_put) | **PUT** /api/rsvps/{id} | Replaces the rsvps resource.
[**api_rsvps_post**](RsvpsApi.md#api_rsvps_post) | **POST** /api/rsvps | Creates a rsvps resource.


# **api_rsvps_get_collection**
> ApiRsvpsGetCollection200Response api_rsvps_get_collection(page=page)

Retrieves the collection of rsvps resources.

Retrieves the collection of rsvps resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_rsvps_get_collection200_response import ApiRsvpsGetCollection200Response
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
    api_instance = gec_api_sdk.RsvpsApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of rsvps resources.
        api_response = api_instance.api_rsvps_get_collection(page=page)
        print("The response of RsvpsApi->api_rsvps_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpsApi->api_rsvps_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiRsvpsGetCollection200Response**](ApiRsvpsGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rsvps collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_rsvps_id_delete**
> api_rsvps_id_delete(id)

Removes the rsvps resource.

Removes the rsvps resource.

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
    api_instance = gec_api_sdk.RsvpsApi(api_client)
    id = 'id_example' # str | rsvps identifier

    try:
        # Removes the rsvps resource.
        api_instance.api_rsvps_id_delete(id)
    except Exception as e:
        print("Exception when calling RsvpsApi->api_rsvps_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| rsvps identifier | 

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
**204** | rsvps resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_rsvps_id_get**
> RsvpsJsonldRsvpRead api_rsvps_id_get(id)

Retrieves a rsvps resource.

Retrieves a rsvps resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvps_jsonld_rsvp_read import RsvpsJsonldRsvpRead
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
    api_instance = gec_api_sdk.RsvpsApi(api_client)
    id = 'id_example' # str | rsvps identifier

    try:
        # Retrieves a rsvps resource.
        api_response = api_instance.api_rsvps_id_get(id)
        print("The response of RsvpsApi->api_rsvps_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpsApi->api_rsvps_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| rsvps identifier | 

### Return type

[**RsvpsJsonldRsvpRead**](RsvpsJsonldRsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rsvps resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_rsvps_id_put**
> RsvpsJsonldRsvpRead api_rsvps_id_put(id, rsvps_rsvp_write)

Replaces the rsvps resource.

Replaces the rsvps resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvps_jsonld_rsvp_read import RsvpsJsonldRsvpRead
from gec_api_sdk.models.rsvps_rsvp_write import RsvpsRsvpWrite
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
    api_instance = gec_api_sdk.RsvpsApi(api_client)
    id = 'id_example' # str | rsvps identifier
    rsvps_rsvp_write = gec_api_sdk.RsvpsRsvpWrite() # RsvpsRsvpWrite | The updated rsvps resource

    try:
        # Replaces the rsvps resource.
        api_response = api_instance.api_rsvps_id_put(id, rsvps_rsvp_write)
        print("The response of RsvpsApi->api_rsvps_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpsApi->api_rsvps_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| rsvps identifier | 
 **rsvps_rsvp_write** | [**RsvpsRsvpWrite**](RsvpsRsvpWrite.md)| The updated rsvps resource | 

### Return type

[**RsvpsJsonldRsvpRead**](RsvpsJsonldRsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | rsvps resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_rsvps_post**
> RsvpsJsonldRsvpRead api_rsvps_post(rsvps_rsvp_write)

Creates a rsvps resource.

Creates a rsvps resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.rsvps_jsonld_rsvp_read import RsvpsJsonldRsvpRead
from gec_api_sdk.models.rsvps_rsvp_write import RsvpsRsvpWrite
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
    api_instance = gec_api_sdk.RsvpsApi(api_client)
    rsvps_rsvp_write = gec_api_sdk.RsvpsRsvpWrite() # RsvpsRsvpWrite | The new rsvps resource

    try:
        # Creates a rsvps resource.
        api_response = api_instance.api_rsvps_post(rsvps_rsvp_write)
        print("The response of RsvpsApi->api_rsvps_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RsvpsApi->api_rsvps_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **rsvps_rsvp_write** | [**RsvpsRsvpWrite**](RsvpsRsvpWrite.md)| The new rsvps resource | 

### Return type

[**RsvpsJsonldRsvpRead**](RsvpsJsonldRsvpRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | rsvps resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

