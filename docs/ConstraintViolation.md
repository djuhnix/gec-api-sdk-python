# ConstraintViolation

Unprocessable entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] [default to 422]
**violations** | [**List[ConstraintViolationViolationsInner]**](ConstraintViolationViolationsInner.md) |  | [optional] 
**detail** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 
**instance** | **str** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.constraint_violation import ConstraintViolation

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintViolation from a JSON string
constraint_violation_instance = ConstraintViolation.from_json(json)
# print the JSON string representation of the object
print(ConstraintViolation.to_json())

# convert the object into a dict
constraint_violation_dict = constraint_violation_instance.to_dict()
# create an instance of ConstraintViolation from a dict
constraint_violation_from_dict = ConstraintViolation.from_dict(constraint_violation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


