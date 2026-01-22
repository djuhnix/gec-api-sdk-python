# ConstraintViolationJsonViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_path** | **str** | The property path of the violation | [optional] 
**message** | **str** | The message associated with the violation | [optional] 

## Example

```python
from gec_api_sdk.models.constraint_violation_json_violations_inner import ConstraintViolationJsonViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintViolationJsonViolationsInner from a JSON string
constraint_violation_json_violations_inner_instance = ConstraintViolationJsonViolationsInner.from_json(json)
# print the JSON string representation of the object
print(ConstraintViolationJsonViolationsInner.to_json())

# convert the object into a dict
constraint_violation_json_violations_inner_dict = constraint_violation_json_violations_inner_instance.to_dict()
# create an instance of ConstraintViolationJsonViolationsInner from a dict
constraint_violation_json_violations_inner_from_dict = ConstraintViolationJsonViolationsInner.from_dict(constraint_violation_json_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


