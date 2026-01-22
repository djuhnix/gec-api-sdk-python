# HelloAssoWebhookDTOMember

DTO for HelloAsso webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**first_name** | **str** |  | 
**last_name** | **str** |  | 
**email** | **str** |  | 
**birth_date** | **datetime** |  | [optional] 
**gender** | **str** |  | [optional] 
**phone_number_fr** | **str** |  | [optional] 
**phone_number_cg** | **str** |  | [optional] 
**postal_address** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**first_year** | **bool** |  | [optional] 
**formation** | **str** |  | [optional] 
**establishment** | **str** |  | [optional] 
**study_level** | **str** |  | [optional] 
**training_cycle** | **str** |  | [optional] 
**other_associations** | **bool** |  | [optional] 
**association_names** | **str** |  | [optional] 
**has_passport_cg** | **bool** |  | [optional] 
**has_visa** | **bool** |  | [optional] 
**has_school_certificate** | **bool** |  | [optional] 
**photo_url** | **str** |  | [optional] 
**status** | **str** |  | 
**membership_type** | **str** |  | 
**contribution** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**documents** | **List[str]** |  | [optional] 
**rsvps** | **List[str]** |  | [optional] 
**donations** | **List[str]** |  | [optional] 

## Example

```python
from gec_api_sdk.models.hello_asso_webhook_dto_member import HelloAssoWebhookDTOMember

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoWebhookDTOMember from a JSON string
hello_asso_webhook_dto_member_instance = HelloAssoWebhookDTOMember.from_json(json)
# print the JSON string representation of the object
print(HelloAssoWebhookDTOMember.to_json())

# convert the object into a dict
hello_asso_webhook_dto_member_dict = hello_asso_webhook_dto_member_instance.to_dict()
# create an instance of HelloAssoWebhookDTOMember from a dict
hello_asso_webhook_dto_member_from_dict = HelloAssoWebhookDTOMember.from_dict(hello_asso_webhook_dto_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


