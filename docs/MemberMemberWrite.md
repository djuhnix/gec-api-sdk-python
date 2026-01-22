# MemberMemberWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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

## Example

```python
from gec_api_sdk.models.member_member_write import MemberMemberWrite

# TODO update the JSON string below
json = "{}"
# create an instance of MemberMemberWrite from a JSON string
member_member_write_instance = MemberMemberWrite.from_json(json)
# print the JSON string representation of the object
print(MemberMemberWrite.to_json())

# convert the object into a dict
member_member_write_dict = member_member_write_instance.to_dict()
# create an instance of MemberMemberWrite from a dict
member_member_write_from_dict = MemberMemberWrite.from_dict(member_member_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


