# HelloAssoWebhookDTO

DTO for HelloAsso webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**HelloAssoDataDTO**](HelloAssoDataDTO.md) |  | 
**event_type** | **str** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_webhook_dto import HelloAssoWebhookDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoWebhookDTO from a JSON string
hello_asso_webhook_dto_instance = HelloAssoWebhookDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoWebhookDTO.to_json())

# convert the object into a dict
hello_asso_webhook_dto_dict = hello_asso_webhook_dto_instance.to_dict()
# create an instance of HelloAssoWebhookDTO from a dict
hello_asso_webhook_dto_from_dict = HelloAssoWebhookDTO.from_dict(hello_asso_webhook_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


