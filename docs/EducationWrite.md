# EducationWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_first_year_study** | **bool** |  | [optional] 
**first_year** | **datetime** |  | [optional] 
**formation** | **str** |  | [optional] 
**establishment** | **str** |  | [optional] 
**study_level** | **str** |  | [optional] 
**training_cycle** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.education_write import EducationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of EducationWrite from a JSON string
education_write_instance = EducationWrite.from_json(json)
# print the JSON string representation of the object
print(EducationWrite.to_json())

# convert the object into a dict
education_write_dict = education_write_instance.to_dict()
# create an instance of EducationWrite from a dict
education_write_from_dict = EducationWrite.from_dict(education_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


