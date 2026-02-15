# gec_api_sdk.TaskApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_tasks_get_collection**](TaskApi.md#api_tasks_get_collection) | **GET** /api/tasks | Retrieves the collection of Task resources.
[**api_tasks_id_delete**](TaskApi.md#api_tasks_id_delete) | **DELETE** /api/tasks/{id} | Removes the Task resource.
[**api_tasks_id_get**](TaskApi.md#api_tasks_id_get) | **GET** /api/tasks/{id} | Retrieves a Task resource.
[**api_tasks_id_put**](TaskApi.md#api_tasks_id_put) | **PUT** /api/tasks/{id} | Replaces the Task resource.
[**api_tasks_post**](TaskApi.md#api_tasks_post) | **POST** /api/tasks | Creates a Task resource.


# **api_tasks_get_collection**
> ApiTasksGetCollection200Response api_tasks_get_collection(page=page)

Retrieves the collection of Task resources.

Retrieves the collection of Task resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_tasks_get_collection200_response import ApiTasksGetCollection200Response
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
    api_instance = gec_api_sdk.TaskApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Task resources.
        api_response = api_instance.api_tasks_get_collection(page=page)
        print("The response of TaskApi->api_tasks_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->api_tasks_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiTasksGetCollection200Response**](ApiTasksGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_delete**
> api_tasks_id_delete(id)

Removes the Task resource.

Removes the Task resource.

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
    api_instance = gec_api_sdk.TaskApi(api_client)
    id = 'id_example' # str | Task identifier

    try:
        # Removes the Task resource.
        api_instance.api_tasks_id_delete(id)
    except Exception as e:
        print("Exception when calling TaskApi->api_tasks_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task identifier | 

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
**204** | Task resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_get**
> TaskJsonldTaskRead api_tasks_id_get(id)

Retrieves a Task resource.

Retrieves a Task resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.task_jsonld_task_read import TaskJsonldTaskRead
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
    api_instance = gec_api_sdk.TaskApi(api_client)
    id = 'id_example' # str | Task identifier

    try:
        # Retrieves a Task resource.
        api_response = api_instance.api_tasks_id_get(id)
        print("The response of TaskApi->api_tasks_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->api_tasks_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task identifier | 

### Return type

[**TaskJsonldTaskRead**](TaskJsonldTaskRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_id_put**
> TaskJsonldTaskRead api_tasks_id_put(id, task_task_write)

Replaces the Task resource.

Replaces the Task resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.task_jsonld_task_read import TaskJsonldTaskRead
from gec_api_sdk.models.task_task_write import TaskTaskWrite
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
    api_instance = gec_api_sdk.TaskApi(api_client)
    id = 'id_example' # str | Task identifier
    task_task_write = gec_api_sdk.TaskTaskWrite() # TaskTaskWrite | The updated Task resource

    try:
        # Replaces the Task resource.
        api_response = api_instance.api_tasks_id_put(id, task_task_write)
        print("The response of TaskApi->api_tasks_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->api_tasks_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Task identifier | 
 **task_task_write** | [**TaskTaskWrite**](TaskTaskWrite.md)| The updated Task resource | 

### Return type

[**TaskJsonldTaskRead**](TaskJsonldTaskRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Task resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_tasks_post**
> TaskJsonldTaskRead api_tasks_post(task_task_write)

Creates a Task resource.

Creates a Task resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.task_jsonld_task_read import TaskJsonldTaskRead
from gec_api_sdk.models.task_task_write import TaskTaskWrite
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
    api_instance = gec_api_sdk.TaskApi(api_client)
    task_task_write = gec_api_sdk.TaskTaskWrite() # TaskTaskWrite | The new Task resource

    try:
        # Creates a Task resource.
        api_response = api_instance.api_tasks_post(task_task_write)
        print("The response of TaskApi->api_tasks_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TaskApi->api_tasks_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_task_write** | [**TaskTaskWrite**](TaskTaskWrite.md)| The new Task resource | 

### Return type

[**TaskJsonldTaskRead**](TaskJsonldTaskRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Task resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

