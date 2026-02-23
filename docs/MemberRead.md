# MemberRead


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
**created_at** | **datetime** | Timestamp when the member record was created. | [optional] [readonly] 
**updated_at** | **datetime** | Timestamp of the last update to this member record. | [optional] 
**documents** | **List[str]** | IRIs of documents attached to this member. | [optional] 
**rsvps** | **List[str]** | IRIs of event RSVPs for this member. | [optional] 
**donations** | **List[str]** | IRIs of donations made by this member. | [optional] 

## Example

```python
from gec_api_sdk.models.member_read import MemberRead

# TODO update the JSON string below
json = "{}"
# create an instance of MemberRead from a JSON string
member_read_instance = MemberRead.from_json(json)
# print the JSON string representation of the object
print(MemberRead.to_json())

# convert the object into a dict
member_read_dict = member_read_instance.to_dict()
# create an instance of MemberRead from a dict
member_read_from_dict = MemberRead.from_dict(member_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


