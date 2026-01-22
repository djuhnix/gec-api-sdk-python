# ConstraintViolationJsonldJsonld

Unprocessable entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**status** | **int** |  | [optional] [default to 422]
**violations** | [**List[ConstraintViolationJsonViolationsInner]**](ConstraintViolationJsonViolationsInner.md) |  | [optional] 
**detail** | **str** |  | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**title** | **str** |  | [optional] [readonly] 
**instance** | **str** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.constraint_violation_jsonld_jsonld import ConstraintViolationJsonldJsonld

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintViolationJsonldJsonld from a JSON string
constraint_violation_jsonld_jsonld_instance = ConstraintViolationJsonldJsonld.from_json(json)
# print the JSON string representation of the object
print(ConstraintViolationJsonldJsonld.to_json())

# convert the object into a dict
constraint_violation_jsonld_jsonld_dict = constraint_violation_jsonld_jsonld_instance.to_dict()
# create an instance of ConstraintViolationJsonldJsonld from a dict
constraint_violation_jsonld_jsonld_from_dict = ConstraintViolationJsonldJsonld.from_dict(constraint_violation_jsonld_jsonld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


