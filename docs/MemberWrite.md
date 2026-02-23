# MemberWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
**is_first_year_study** | **bool** | Whether this is the member&#39;s first year of study. | [optional] 
**first_year** | **date** | Start date of the first year of study. | [optional] 
**formation** | **str** | Field of study / training programme. | [optional] 
**establishment** | **str** | Educational establishment (school or university). | [optional] 
**study_level** | **str** | Current study level (e.g. Licence 1, Master 2). | [optional] 
**training_cycle** | **str** | Training cycle: initial, apprenticeship, or continuing education. | [optional] 
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

## Example

```python
from gec_api_sdk.models.member_write import MemberWrite

# TODO update the JSON string below
json = "{}"
# create an instance of MemberWrite from a JSON string
member_write_instance = MemberWrite.from_json(json)
# print the JSON string representation of the object
print(MemberWrite.to_json())

# convert the object into a dict
member_write_dict = member_write_instance.to_dict()
# create an instance of MemberWrite from a dict
member_write_from_dict = MemberWrite.from_dict(member_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


