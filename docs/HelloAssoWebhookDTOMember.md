# HelloAssoWebhookDTOMember

DTO for HelloAsso webhook notification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier (UUID). | [optional] [readonly] 
**first_name** | **str** | Member&#39;s first name. | 
**last_name** | **str** | Member&#39;s last name. | 
**email** | **str** | Unique email address. | [optional] 
**birth_date** | **date** | Date of birth. | [optional] 
**gender** | **str** | Gender. | [optional] 
**phone_number_fr** | **str** | French phone number. | [optional] 
**phone_number_cg** | **str** | Congolese phone number. | [optional] 
**postal_address** | **str** | Street address. | [optional] 
**postal_code** | **str** | Postal/zip code. | [optional] 
**city** | **str** | City of residence. | [optional] 
**other_associations** | **bool** | Whether the member belongs to other associations. | [optional] 
**association_names** | **str** | Names of other associations the member belongs to. | [optional] 
**has_passport_cg** | **bool** | Whether the member holds a Congolese passport. | [optional] 
**has_visa** | **bool** | Whether the member holds a valid visa. | [optional] 
**has_school_certificate** | **bool** | Whether the member has provided a school certificate. | [optional] 
**photo_url** | **str** | URL of the member&#39;s profile photo. | [optional] 
**status** | **str** | Membership status: active, pending, expired, or suspended. | 
**membership_type** | **str** | Membership type: student, active, sponsor, or alumni. | 
**membership_start_date** | **date** | Date when the current membership period started. | [optional] 
**contribution** | **float** | Membership fee amount paid (in euros). | [optional] 
**contribution_status** | **str** | Contribution payment status: paid, pending, or expired. | [optional] 
**created_at** | **datetime** | Timestamp when the member record was created. | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp of the last update to this member record. | [optional] 
**user** | **str** | IRI of the linked authentication user account, if any. | [optional] 
**education** | [**Education**](Education.md) |  | [optional] 
**documents** | **List[str]** | IRIs of documents attached to this member. | [optional] 
**rsvps** | **List[str]** | IRIs of event RSVPs for this member. | [optional] 
**donations** | **List[str]** | IRIs of donations made by this member. | [optional] 

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


