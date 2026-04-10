# MemberPublicViewPublicRead

Read-only projection of active members for unauthenticated public access. Backed by the public.member_public_view PostgreSQL materialized view. Contains only non-PII fields — no email, birth date, phone, address, or financial data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**display_name** | **str** | Anonymised display name computed from initials: \&quot;J. D.\&quot; Real first and last names are never exposed in this projection. | [optional] [readonly] 
**membership_type** | **str** |  | [optional] [readonly] 
**status** | **str** |  | [optional] [readonly] 
**city** | **str** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.member_public_view_public_read import MemberPublicViewPublicRead

# TODO update the JSON string below
json = "{}"
# create an instance of MemberPublicViewPublicRead from a JSON string
member_public_view_public_read_instance = MemberPublicViewPublicRead.from_json(json)
# print the JSON string representation of the object
print(MemberPublicViewPublicRead.to_json())

# convert the object into a dict
member_public_view_public_read_dict = member_public_view_public_read_instance.to_dict()
# create an instance of MemberPublicViewPublicRead from a dict
member_public_view_public_read_from_dict = MemberPublicViewPublicRead.from_dict(member_public_view_public_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


