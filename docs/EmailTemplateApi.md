# gec_api_sdk.EmailTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_email_template**](EmailTemplateApi.md#create_email_template) | **POST** /api/email_templates | Creates a EmailTemplate resource.
[**delete_email_template**](EmailTemplateApi.md#delete_email_template) | **DELETE** /api/email_templates/{id} | Removes the EmailTemplate resource.
[**get_email_template**](EmailTemplateApi.md#get_email_template) | **GET** /api/email_templates/{id} | Retrieves a EmailTemplate resource.
[**list_email_templates**](EmailTemplateApi.md#list_email_templates) | **GET** /api/email_templates | Retrieves the collection of EmailTemplate resources.
[**update_email_template**](EmailTemplateApi.md#update_email_template) | **PUT** /api/email_templates/{id} | Replaces the EmailTemplate resource.


# **create_email_template**
> EmailTemplateRead create_email_template(email_template_write)

Creates a EmailTemplate resource.

Creates a EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_read import EmailTemplateRead
from gec_api_sdk.models.email_template_write import EmailTemplateWrite
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
    api_instance = gec_api_sdk.EmailTemplateApi(api_client)
    email_template_write = gec_api_sdk.EmailTemplateWrite() # EmailTemplateWrite | The new EmailTemplate resource

    try:
        # Creates a EmailTemplate resource.
        api_response = api_instance.create_email_template(email_template_write)
        print("The response of EmailTemplateApi->create_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->create_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_write** | [**EmailTemplateWrite**](EmailTemplateWrite.md)| The new EmailTemplate resource | 

### Return type

[**EmailTemplateRead**](EmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EmailTemplate resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_email_template**
> delete_email_template(id)

Removes the EmailTemplate resource.

Removes the EmailTemplate resource.

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
    api_instance = gec_api_sdk.EmailTemplateApi(api_client)
    id = 'id_example' # str | EmailTemplate identifier

    try:
        # Removes the EmailTemplate resource.
        api_instance.delete_email_template(id)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->delete_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EmailTemplate identifier | 

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
**204** | EmailTemplate resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_email_template**
> EmailTemplateRead get_email_template(id)

Retrieves a EmailTemplate resource.

Retrieves a EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_read import EmailTemplateRead
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
    api_instance = gec_api_sdk.EmailTemplateApi(api_client)
    id = 'id_example' # str | EmailTemplate identifier

    try:
        # Retrieves a EmailTemplate resource.
        api_response = api_instance.get_email_template(id)
        print("The response of EmailTemplateApi->get_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->get_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EmailTemplate identifier | 

### Return type

[**EmailTemplateRead**](EmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_email_templates**
> List[EmailTemplateRead] list_email_templates(page=page)

Retrieves the collection of EmailTemplate resources.

Retrieves the collection of EmailTemplate resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_read import EmailTemplateRead
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
    api_instance = gec_api_sdk.EmailTemplateApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of EmailTemplate resources.
        api_response = api_instance.list_email_templates(page=page)
        print("The response of EmailTemplateApi->list_email_templates:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->list_email_templates: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**List[EmailTemplateRead]**](EmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_email_template**
> EmailTemplateRead update_email_template(id, email_template_write)

Replaces the EmailTemplate resource.

Replaces the EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_read import EmailTemplateRead
from gec_api_sdk.models.email_template_write import EmailTemplateWrite
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
    api_instance = gec_api_sdk.EmailTemplateApi(api_client)
    id = 'id_example' # str | EmailTemplate identifier
    email_template_write = gec_api_sdk.EmailTemplateWrite() # EmailTemplateWrite | The updated EmailTemplate resource

    try:
        # Replaces the EmailTemplate resource.
        api_response = api_instance.update_email_template(id, email_template_write)
        print("The response of EmailTemplateApi->update_email_template:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->update_email_template: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EmailTemplate identifier | 
 **email_template_write** | [**EmailTemplateWrite**](EmailTemplateWrite.md)| The updated EmailTemplate resource | 

### Return type

[**EmailTemplateRead**](EmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

