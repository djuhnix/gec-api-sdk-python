# gec_api_sdk.WifCredentialTokenResponseDTOApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_internalwifcredential_token_get**](WifCredentialTokenResponseDTOApi.md#api_internalwifcredential_token_get) | **GET** /api/internal/wif/credential-token | Retrieves a WifCredentialTokenResponseDTO resource.
[**api_internalwifcredential_token_post**](WifCredentialTokenResponseDTOApi.md#api_internalwifcredential_token_post) | **POST** /api/internal/wif/credential-token | Creates a WifCredentialTokenResponseDTO resource.


# **api_internalwifcredential_token_get**
> WifCredentialTokenResponseDTO api_internalwifcredential_token_get()

Retrieves a WifCredentialTokenResponseDTO resource.

Retrieves a WifCredentialTokenResponseDTO resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.wif_credential_token_response_dto import WifCredentialTokenResponseDTO
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
    api_instance = gec_api_sdk.WifCredentialTokenResponseDTOApi(api_client)

    try:
        # Retrieves a WifCredentialTokenResponseDTO resource.
        api_response = api_instance.api_internalwifcredential_token_get()
        print("The response of WifCredentialTokenResponseDTOApi->api_internalwifcredential_token_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WifCredentialTokenResponseDTOApi->api_internalwifcredential_token_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**WifCredentialTokenResponseDTO**](WifCredentialTokenResponseDTO.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | WifCredentialTokenResponseDTO resource |  -  |
**404** | Not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **api_internalwifcredential_token_post**
> WifCredentialTokenResponseDTO api_internalwifcredential_token_post(wif_credential_token_response_dto_wif_credential_token_request_dto)

Creates a WifCredentialTokenResponseDTO resource.

Creates a WifCredentialTokenResponseDTO resource.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.wif_credential_token_response_dto import WifCredentialTokenResponseDTO
from gec_api_sdk.models.wif_credential_token_response_dto_wif_credential_token_request_dto import WifCredentialTokenResponseDTOWifCredentialTokenRequestDTO
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
    api_instance = gec_api_sdk.WifCredentialTokenResponseDTOApi(api_client)
    wif_credential_token_response_dto_wif_credential_token_request_dto = gec_api_sdk.WifCredentialTokenResponseDTOWifCredentialTokenRequestDTO() # WifCredentialTokenResponseDTOWifCredentialTokenRequestDTO | The new WifCredentialTokenResponseDTO resource

    try:
        # Creates a WifCredentialTokenResponseDTO resource.
        api_response = api_instance.api_internalwifcredential_token_post(wif_credential_token_response_dto_wif_credential_token_request_dto)
        print("The response of WifCredentialTokenResponseDTOApi->api_internalwifcredential_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WifCredentialTokenResponseDTOApi->api_internalwifcredential_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **wif_credential_token_response_dto_wif_credential_token_request_dto** | [**WifCredentialTokenResponseDTOWifCredentialTokenRequestDTO**](WifCredentialTokenResponseDTOWifCredentialTokenRequestDTO.md)| The new WifCredentialTokenResponseDTO resource | 

### Return type

[**WifCredentialTokenResponseDTO**](WifCredentialTokenResponseDTO.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/ld+json, application/problem+json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | WifCredentialTokenResponseDTO resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

