# gec_api_sdk.DonationApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_donations_get_collection**](DonationApi.md#api_donations_get_collection) | **GET** /api/donations | Retrieves the collection of Donation resources.
[**api_donations_id_delete**](DonationApi.md#api_donations_id_delete) | **DELETE** /api/donations/{id} | Removes the Donation resource.
[**api_donations_id_get**](DonationApi.md#api_donations_id_get) | **GET** /api/donations/{id} | Retrieves a Donation resource.
[**api_donations_id_put**](DonationApi.md#api_donations_id_put) | **PUT** /api/donations/{id} | Replaces the Donation resource.
[**api_donations_post**](DonationApi.md#api_donations_post) | **POST** /api/donations | Creates a Donation resource.


# **api_donations_get_collection**
> ApiDonationsGetCollection200Response api_donations_get_collection(page=page)

Retrieves the collection of Donation resources.

Retrieves the collection of Donation resources.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.api_donations_get_collection200_response import ApiDonationsGetCollection200Response
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
    api_instance = gec_api_sdk.DonationApi(api_client)
    page = 1 # int | The collection page number (optional) (default to 1)

    try:
        # Retrieves the collection of Donation resources.
        api_response = api_instance.api_donations_get_collection(page=page)
        print("The response of DonationApi->api_donations_get_collection:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationApi->api_donations_get_collection: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **int**| The collection page number | [optional] [default to 1]

### Return type

[**ApiDonationsGetCollection200Response**](ApiDonationsGetCollection200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Donation collection |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_donations_id_delete**
> api_donations_id_delete(id)

Removes the Donation resource.

Removes the Donation resource.

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
    api_instance = gec_api_sdk.DonationApi(api_client)
    id = 'id_example' # str | Donation identifier

    try:
        # Removes the Donation resource.
        api_instance.api_donations_id_delete(id)
    except Exception as e:
        print("Exception when calling DonationApi->api_donations_id_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Donation identifier | 

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
**204** | Donation resource deleted |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_donations_id_get**
> DonationJsonldDonationRead api_donations_id_get(id)

Retrieves a Donation resource.

Retrieves a Donation resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.donation_jsonld_donation_read import DonationJsonldDonationRead
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
    api_instance = gec_api_sdk.DonationApi(api_client)
    id = 'id_example' # str | Donation identifier

    try:
        # Retrieves a Donation resource.
        api_response = api_instance.api_donations_id_get(id)
        print("The response of DonationApi->api_donations_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationApi->api_donations_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Donation identifier | 

### Return type

[**DonationJsonldDonationRead**](DonationJsonldDonationRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Donation resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_donations_id_put**
> DonationJsonldDonationRead api_donations_id_put(id, donation_jsonld_donation_write)

Replaces the Donation resource.

Replaces the Donation resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.donation_jsonld_donation_read import DonationJsonldDonationRead
from gec_api_sdk.models.donation_jsonld_donation_write import DonationJsonldDonationWrite
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
    api_instance = gec_api_sdk.DonationApi(api_client)
    id = 'id_example' # str | Donation identifier
    donation_jsonld_donation_write = gec_api_sdk.DonationJsonldDonationWrite() # DonationJsonldDonationWrite | The updated Donation resource

    try:
        # Replaces the Donation resource.
        api_response = api_instance.api_donations_id_put(id, donation_jsonld_donation_write)
        print("The response of DonationApi->api_donations_id_put:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationApi->api_donations_id_put: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Donation identifier | 
 **donation_jsonld_donation_write** | [**DonationJsonldDonationWrite**](DonationJsonldDonationWrite.md)| The updated Donation resource | 

### Return type

[**DonationJsonldDonationRead**](DonationJsonldDonationRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Donation resource updated |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_donations_post**
> DonationJsonldDonationRead api_donations_post(donation_jsonld_donation_write)

Creates a Donation resource.

Creates a Donation resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.donation_jsonld_donation_read import DonationJsonldDonationRead
from gec_api_sdk.models.donation_jsonld_donation_write import DonationJsonldDonationWrite
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
    api_instance = gec_api_sdk.DonationApi(api_client)
    donation_jsonld_donation_write = gec_api_sdk.DonationJsonldDonationWrite() # DonationJsonldDonationWrite | The new Donation resource

    try:
        # Creates a Donation resource.
        api_response = api_instance.api_donations_post(donation_jsonld_donation_write)
        print("The response of DonationApi->api_donations_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DonationApi->api_donations_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **donation_jsonld_donation_write** | [**DonationJsonldDonationWrite**](DonationJsonldDonationWrite.md)| The new Donation resource | 

### Return type

[**DonationJsonldDonationRead**](DonationJsonldDonationRead.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/ld+json, application/json, application/x-yaml, text/csv
 - **Accept**: application/ld+json, application/json, application/x-yaml, text/csv, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Donation resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

