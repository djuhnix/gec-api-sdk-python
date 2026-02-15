# ConstraintViolationViolationsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**property_path** | **str** | The property path of the violation | 
**message** | **str** | The message associated with the violation | 
**code** | **str** | The code of the violation | [optional] 
**hint** | **str** | An extra hint to understand the violation | [optional] 
**payload** | **Dict[str, object]** | The serialized payload of the violation | [optional] 

## Example

```python
from gec_api_sdk.models.constraint_violation_violations_inner import ConstraintViolationViolationsInner

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintViolationViolationsInner from a JSON string
constraint_violation_violations_inner_instance = ConstraintViolationViolationsInner.from_json(json)
# print the JSON string representation of the object
print(ConstraintViolationViolationsInner.to_json())

# convert the object into a dict
constraint_violation_violations_inner_dict = constraint_violation_violations_inner_instance.to_dict()
# create an instance of ConstraintViolationViolationsInner from a dict
constraint_violation_violations_inner_from_dict = ConstraintViolationViolationsInner.from_dict(constraint_violation_violations_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


