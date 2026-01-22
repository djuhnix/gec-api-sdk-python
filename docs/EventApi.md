# gec_api_sdk.EventApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_events_get_collection**](EventApi.md#api_events_get_collection) | **GET** /api/events | Retrieves the collection of Event resources.
[**api_events_id_delete**](EventApi.md#api_events_id_delete) | **DELETE** /api/events/{id} | Removes the Event resource.
[**api_events_id_get**](EventApi.md#api_events_id_get) | **GET** /api/events/{id} | Retrieves a Event resource.
[**api_events_id_put**](EventApi.md#api_events_id_put) | **PUT** /api/events/{id} | Replaces the Event resource.
[**api_events_post**](EventApi.md#api_events_post) | **POST** /api/events | Creates a Event resource.


# **api_events_get_collection**
> ApiEventsGetCollection200Response api_events_get_collection(page=page)

Retrieves the collection of Event resources.

Retrieves the collection of Event resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_events_get_collection200_response import ApiEventsGetCollection200Response
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
    api_instance = gec_api_sdk.EventApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Event resources.
        api_response = api_instance.api_events_get_collection(page=page)
        print("The response of EventApi->api_events_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->api_events_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiEventsGetCollection200Response**](ApiEventsGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_events_id_delete**
> api_events_id_delete(id)

Removes the Event resource.

Removes the Event resource.

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
    api_instance = gec_api_sdk.EventApi(api_client)
    id = 'id_example' # str | Event identifier

    try:
        # Removes the Event resource.
        api_instance.api_events_id_delete(id)
    except Exception as e:
        print("Exception when calling EventApi->api_events_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event identifier | 

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
**204** | Event resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_events_id_get**
> EventJsonldEventRead api_events_id_get(id)

Retrieves a Event resource.

Retrieves a Event resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.event_jsonld_event_read import EventJsonldEventRead
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
    api_instance = gec_api_sdk.EventApi(api_client)
    id = 'id_example' # str | Event identifier

    try:
        # Retrieves a Event resource.
        api_response = api_instance.api_events_id_get(id)
        print("The response of EventApi->api_events_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->api_events_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event identifier | 

### Return type

[**EventJsonldEventRead**](EventJsonldEventRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_events_id_put**
> EventJsonldEventRead api_events_id_put(id, event_jsonld_event_write)

Replaces the Event resource.

Replaces the Event resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.event_jsonld_event_read import EventJsonldEventRead
from gec_api_sdk.models.event_jsonld_event_write import EventJsonldEventWrite
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
    api_instance = gec_api_sdk.EventApi(api_client)
    id = 'id_example' # str | Event identifier
    event_jsonld_event_write = gec_api_sdk.EventJsonldEventWrite() # EventJsonldEventWrite | The updated Event resource

    try:
        # Replaces the Event resource.
        api_response = api_instance.api_events_id_put(id, event_jsonld_event_write)
        print("The response of EventApi->api_events_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->api_events_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Event identifier | 
 **event_jsonld_event_write** | [**EventJsonldEventWrite**](EventJsonldEventWrite.md)| The updated Event resource | 

### Return type

[**EventJsonldEventRead**](EventJsonldEventRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Event resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_events_post**
> EventJsonldEventRead api_events_post(event_jsonld_event_write)

Creates a Event resource.

Creates a Event resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.event_jsonld_event_read import EventJsonldEventRead
from gec_api_sdk.models.event_jsonld_event_write import EventJsonldEventWrite
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
    api_instance = gec_api_sdk.EventApi(api_client)
    event_jsonld_event_write = gec_api_sdk.EventJsonldEventWrite() # EventJsonldEventWrite | The new Event resource

    try:
        # Creates a Event resource.
        api_response = api_instance.api_events_post(event_jsonld_event_write)
        print("The response of EventApi->api_events_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventApi->api_events_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_jsonld_event_write** | [**EventJsonldEventWrite**](EventJsonldEventWrite.md)| The new Event resource | 

### Return type

[**EventJsonldEventRead**](EventJsonldEventRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Event resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

