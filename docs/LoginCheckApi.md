# gec_api_sdk.LoginCheckApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**login_check_post**](LoginCheckApi.md#login_check_post) | **POST** /api/auth | Creates a user token.


# **login_check_post**
> LoginCheckPost200Response login_check_post(login_check_post_request)

Creates a user token.

Creates a user token.

### Example

* Bearer (JWT) Authentication (JWT):

```python
import gec_api_sdk
from gec_api_sdk.models.login_check_post200_response import LoginCheckPost200Response
from gec_api_sdk.models.login_check_post_request import LoginCheckPostRequest
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
    api_instance = gec_api_sdk.LoginCheckApi(api_client)
    login_check_post_request = gec_api_sdk.LoginCheckPostRequest() # LoginCheckPostRequest | The login data

    try:
        # Creates a user token.
        api_response = api_instance.login_check_post(login_check_post_request)
        print("The response of LoginCheckApi->login_check_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LoginCheckApi->login_check_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **login_check_post_request** | [**LoginCheckPostRequest**](LoginCheckPostRequest.md)| The login data | 

### Return type

[**LoginCheckPost200Response**](LoginCheckPost200Response.md)

### Authorization

[JWT](../README.md#JWT)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User token created |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

