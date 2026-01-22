# gec_api_sdk.DocumentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_documents_get_collection**](DocumentApi.md#api_documents_get_collection) | **GET** /api/documents | Retrieves the collection of Document resources.
[**api_documents_id_delete**](DocumentApi.md#api_documents_id_delete) | **DELETE** /api/documents/{id} | Removes the Document resource.
[**api_documents_id_get**](DocumentApi.md#api_documents_id_get) | **GET** /api/documents/{id} | Retrieves a Document resource.
[**api_documents_id_put**](DocumentApi.md#api_documents_id_put) | **PUT** /api/documents/{id} | Replaces the Document resource.
[**api_documents_post**](DocumentApi.md#api_documents_post) | **POST** /api/documents | Creates a Document resource.


# **api_documents_get_collection**
> ApiDocumentsGetCollection200Response api_documents_get_collection(page=page)

Retrieves the collection of Document resources.

Retrieves the collection of Document resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_documents_get_collection200_response import ApiDocumentsGetCollection200Response
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
    api_instance = gec_api_sdk.DocumentApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Document resources.
        api_response = api_instance.api_documents_get_collection(page=page)
        print("The response of DocumentApi->api_documents_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->api_documents_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiDocumentsGetCollection200Response**](ApiDocumentsGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_id_delete**
> api_documents_id_delete(id)

Removes the Document resource.

Removes the Document resource.

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
    api_instance = gec_api_sdk.DocumentApi(api_client)
    id = 'id_example' # str | Document identifier

    try:
        # Removes the Document resource.
        api_instance.api_documents_id_delete(id)
    except Exception as e:
        print("Exception when calling DocumentApi->api_documents_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document identifier | 

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
**204** | Document resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_id_get**
> DocumentJsonldDocumentRead api_documents_id_get(id)

Retrieves a Document resource.

Retrieves a Document resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.document_jsonld_document_read import DocumentJsonldDocumentRead
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
    api_instance = gec_api_sdk.DocumentApi(api_client)
    id = 'id_example' # str | Document identifier

    try:
        # Retrieves a Document resource.
        api_response = api_instance.api_documents_id_get(id)
        print("The response of DocumentApi->api_documents_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->api_documents_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document identifier | 

### Return type

[**DocumentJsonldDocumentRead**](DocumentJsonldDocumentRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_id_put**
> DocumentJsonldDocumentRead api_documents_id_put(id, document_jsonld_document_write)

Replaces the Document resource.

Replaces the Document resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.document_jsonld_document_read import DocumentJsonldDocumentRead
from gec_api_sdk.models.document_jsonld_document_write import DocumentJsonldDocumentWrite
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
    api_instance = gec_api_sdk.DocumentApi(api_client)
    id = 'id_example' # str | Document identifier
    document_jsonld_document_write = gec_api_sdk.DocumentJsonldDocumentWrite() # DocumentJsonldDocumentWrite | The updated Document resource

    try:
        # Replaces the Document resource.
        api_response = api_instance.api_documents_id_put(id, document_jsonld_document_write)
        print("The response of DocumentApi->api_documents_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->api_documents_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Document identifier | 
 **document_jsonld_document_write** | [**DocumentJsonldDocumentWrite**](DocumentJsonldDocumentWrite.md)| The updated Document resource | 

### Return type

[**DocumentJsonldDocumentRead**](DocumentJsonldDocumentRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Document resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_documents_post**
> DocumentJsonldDocumentRead api_documents_post(document_jsonld_document_write)

Creates a Document resource.

Creates a Document resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.document_jsonld_document_read import DocumentJsonldDocumentRead
from gec_api_sdk.models.document_jsonld_document_write import DocumentJsonldDocumentWrite
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
    api_instance = gec_api_sdk.DocumentApi(api_client)
    document_jsonld_document_write = gec_api_sdk.DocumentJsonldDocumentWrite() # DocumentJsonldDocumentWrite | The new Document resource

    try:
        # Creates a Document resource.
        api_response = api_instance.api_documents_post(document_jsonld_document_write)
        print("The response of DocumentApi->api_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentApi->api_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **document_jsonld_document_write** | [**DocumentJsonldDocumentWrite**](DocumentJsonldDocumentWrite.md)| The new Document resource | 

### Return type

[**DocumentJsonldDocumentRead**](DocumentJsonldDocumentRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Document resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

