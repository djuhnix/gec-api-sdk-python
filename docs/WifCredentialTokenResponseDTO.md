# WifCredentialTokenResponseDTO

DTO for WIF credential token API endpoint.  This DTO acts as both the API Platform resource definition and the response format. It follows the HelloAssoWebhookDTO pattern where the DTO defines the API endpoint and the processor handles the business logic.  Unlike HelloAsso which returns a Member entity, this endpoint returns a credential response with a JWT token, which is better represented as a DTO rather than an entity since we don't persist credential tokens.  Security Features (enforced via processor): - Rate limiting per IP and user (A07: Authentication Failures) - Input validation and sanitization (A03: Injection) - Comprehensive audit logging (A09: Security Logging) - IP allowlist support (A01: Broken Access Control) - Protection against timing attacks

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** |  | [optional] 
**success** | **bool** |  | [optional] 
**token_type** | **str** |  | [optional] 
**expires_in** | **int** |  | [optional] 
**expiration_time** | **int** |  | [optional] 
**access_token** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.wif_credential_token_response_dto import WifCredentialTokenResponseDTO

# TODO update the JSON string below
json = "{}"
# create an instance of WifCredentialTokenResponseDTO from a JSON string
wif_credential_token_response_dto_instance = WifCredentialTokenResponseDTO.from_json(json)
# print the JSON string representation of the object
print(WifCredentialTokenResponseDTO.to_json())

# convert the object into a dict
wif_credential_token_response_dto_dict = wif_credential_token_response_dto_instance.to_dict()
# create an instance of WifCredentialTokenResponseDTO from a dict
wif_credential_token_response_dto_from_dict = WifCredentialTokenResponseDTO.from_dict(wif_credential_token_response_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


