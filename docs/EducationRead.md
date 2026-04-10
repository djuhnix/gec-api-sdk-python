# EducationRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**is_first_year_study** | **bool** |  | [optional] 
**first_year** | **datetime** |  | [optional] 
**formation** | **str** |  | [optional] 
**establishment** | **str** |  | [optional] 
**study_level** | **str** |  | [optional] 
**training_cycle** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.education_read import EducationRead

# TODO update the JSON string below
json = "{}"
# create an instance of EducationRead from a JSON string
education_read_instance = EducationRead.from_json(json)
# print the JSON string representation of the object
print(EducationRead.to_json())

# convert the object into a dict
education_read_dict = education_read_instance.to_dict()
# create an instance of EducationRead from a dict
education_read_from_dict = EducationRead.from_dict(education_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


