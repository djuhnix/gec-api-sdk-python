# Education


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
**first_year_study** | **bool** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.education import Education

# TODO update the JSON string below
json = "{}"
# create an instance of Education from a JSON string
education_instance = Education.from_json(json)
# print the JSON string representation of the object
print(Education.to_json())

# convert the object into a dict
education_dict = education_instance.to_dict()
# create an instance of Education from a dict
education_from_dict = Education.from_dict(education_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


