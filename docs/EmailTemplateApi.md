# gec_api_sdk.EmailTemplateApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_email_templates_get_collection**](EmailTemplateApi.md#api_email_templates_get_collection) | **GET** /api/email_templates | Retrieves the collection of EmailTemplate resources.
[**api_email_templates_id_delete**](EmailTemplateApi.md#api_email_templates_id_delete) | **DELETE** /api/email_templates/{id} | Removes the EmailTemplate resource.
[**api_email_templates_id_get**](EmailTemplateApi.md#api_email_templates_id_get) | **GET** /api/email_templates/{id} | Retrieves a EmailTemplate resource.
[**api_email_templates_id_put**](EmailTemplateApi.md#api_email_templates_id_put) | **PUT** /api/email_templates/{id} | Replaces the EmailTemplate resource.
[**api_email_templates_post**](EmailTemplateApi.md#api_email_templates_post) | **POST** /api/email_templates | Creates a EmailTemplate resource.


# **api_email_templates_get_collection**
> ApiEmailTemplatesGetCollection200Response api_email_templates_get_collection(page=page)

Retrieves the collection of EmailTemplate resources.

Retrieves the collection of EmailTemplate resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_email_templates_get_collection200_response import ApiEmailTemplatesGetCollection200Response
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
        api_response = api_instance.api_email_templates_get_collection(page=page)
        print("The response of EmailTemplateApi->api_email_templates_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->api_email_templates_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiEmailTemplatesGetCollection200Response**](ApiEmailTemplatesGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_email_templates_id_delete**
> api_email_templates_id_delete(id)

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
        api_instance.api_email_templates_id_delete(id)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->api_email_templates_id_delete: %s\n" % e)
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
 - **Accept**: application/ld+json, application/problem+json, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | EmailTemplate resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_email_templates_id_get**
> EmailTemplateJsonldEmailTemplateRead api_email_templates_id_get(id)

Retrieves a EmailTemplate resource.

Retrieves a EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_jsonld_email_template_read import EmailTemplateJsonldEmailTemplateRead
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
        api_response = api_instance.api_email_templates_id_get(id)
        print("The response of EmailTemplateApi->api_email_templates_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->api_email_templates_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EmailTemplate identifier | 

### Return type

[**EmailTemplateJsonldEmailTemplateRead**](EmailTemplateJsonldEmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_email_templates_id_put**
> EmailTemplateJsonldEmailTemplateRead api_email_templates_id_put(id, email_template_email_template_write)

Replaces the EmailTemplate resource.

Replaces the EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_email_template_write import EmailTemplateEmailTemplateWrite
from gec_api_sdk.models.email_template_jsonld_email_template_read import EmailTemplateJsonldEmailTemplateRead
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
    email_template_email_template_write = gec_api_sdk.EmailTemplateEmailTemplateWrite() # EmailTemplateEmailTemplateWrite | The updated EmailTemplate resource

    try:
        # Replaces the EmailTemplate resource.
        api_response = api_instance.api_email_templates_id_put(id, email_template_email_template_write)
        print("The response of EmailTemplateApi->api_email_templates_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->api_email_templates_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| EmailTemplate identifier | 
 **email_template_email_template_write** | [**EmailTemplateEmailTemplateWrite**](EmailTemplateEmailTemplateWrite.md)| The updated EmailTemplate resource | 

### Return type

[**EmailTemplateJsonldEmailTemplateRead**](EmailTemplateJsonldEmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | EmailTemplate resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_email_templates_post**
> EmailTemplateJsonldEmailTemplateRead api_email_templates_post(email_template_email_template_write)

Creates a EmailTemplate resource.

Creates a EmailTemplate resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.email_template_email_template_write import EmailTemplateEmailTemplateWrite
from gec_api_sdk.models.email_template_jsonld_email_template_read import EmailTemplateJsonldEmailTemplateRead
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
    email_template_email_template_write = gec_api_sdk.EmailTemplateEmailTemplateWrite() # EmailTemplateEmailTemplateWrite | The new EmailTemplate resource

    try:
        # Creates a EmailTemplate resource.
        api_response = api_instance.api_email_templates_post(email_template_email_template_write)
        print("The response of EmailTemplateApi->api_email_templates_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EmailTemplateApi->api_email_templates_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **email_template_email_template_write** | [**EmailTemplateEmailTemplateWrite**](EmailTemplateEmailTemplateWrite.md)| The new EmailTemplate resource | 

### Return type

[**EmailTemplateJsonldEmailTemplateRead**](EmailTemplateJsonldEmailTemplateRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | EmailTemplate resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

