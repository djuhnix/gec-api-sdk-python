# gec_api_sdk.HelloAssoWebhooksApi

All URIs are relative to *https://multisegmented-diane-superexpressively.ngrok-free.dev*

Method | HTTP request | Description
------------- | ------------- | -------------
[**api_hello_assowebhook_post**](HelloAssoWebhooksApi.md#api_hello_assowebhook_post) | **POST** /api/hello_asso/webhook | Receive HelloAsso webhook notifications


# **api_hello_assowebhook_post**
> HelloAssoWebhookDTOMember api_hello_assowebhook_post(hello_asso_webhook_dto)

Receive HelloAsso webhook notifications

Endpoint to receive webhook notifications from HelloAsso. The payload will be processed and stored in the database.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.hello_asso_webhook_dto import HelloAssoWebhookDTO
from gec_api_sdk.models.hello_asso_webhook_dto_member import HelloAssoWebhookDTOMember
from gec_api_sdk.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://multisegmented-diane-superexpressively.ngrok-free.dev
# See configuration.py for a list of all supported configuration parameters.
configuration = gec_api_sdk.Configuration(
    host = "https://multisegmented-diane-superexpressively.ngrok-free.dev"
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
    api_instance = gec_api_sdk.HelloAssoWebhooksApi(api_client)
    hello_asso_webhook_dto = gec_api_sdk.HelloAssoWebhookDTO() # HelloAssoWebhookDTO | The new HelloAssoWebhookDTO resource

    try:
        # Receive HelloAsso webhook notifications
        api_response = api_instance.api_hello_assowebhook_post(hello_asso_webhook_dto)
        print("The response of HelloAssoWebhooksApi->api_hello_assowebhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling HelloAssoWebhooksApi->api_hello_assowebhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hello_asso_webhook_dto** | [**HelloAssoWebhookDTO**](HelloAssoWebhookDTO.md)| The new HelloAssoWebhookDTO resource | 

### Return type

[**HelloAssoWebhookDTOMember**](HelloAssoWebhookDTOMember.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | HelloAssoWebhookDTO resource created |  -  |
**400** | Invalid input |  -  |
**422** | An error occurred |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

