# MemberJsonldMemberRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
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
from gec_api_sdk.models.member_jsonld_member_read import MemberJsonldMemberRead

# TODO update the JSON string below
json = "{}"
# create an instance of MemberJsonldMemberRead from a JSON string
member_jsonld_member_read_instance = MemberJsonldMemberRead.from_json(json)
# print the JSON string representation of the object
print(MemberJsonldMemberRead.to_json())

# convert the object into a dict
member_jsonld_member_read_dict = member_jsonld_member_read_instance.to_dict()
# create an instance of MemberJsonldMemberRead from a dict
member_jsonld_member_read_from_dict = MemberJsonldMemberRead.from_dict(member_jsonld_member_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


