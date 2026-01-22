# MemberJsonldMemberWrite



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
from gec_api_sdk.models.member_jsonld_member_write import MemberJsonldMemberWrite

# TODO update the JSON string below
json = "{}"
# create an instance of MemberJsonldMemberWrite from a JSON string
member_jsonld_member_write_instance = MemberJsonldMemberWrite.from_json(json)
# print the JSON string representation of the object
print(MemberJsonldMemberWrite.to_json())

# convert the object into a dict
member_jsonld_member_write_dict = member_jsonld_member_write_instance.to_dict()
# create an instance of MemberJsonldMemberWrite from a dict
member_jsonld_member_write_from_dict = MemberJsonldMemberWrite.from_dict(member_jsonld_member_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


