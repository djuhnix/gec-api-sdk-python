# ErrorJsonld

A representation of common errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**title** | **str** | A short, human-readable summary of the problem. | [optional] [readonly] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] [readonly] 
**status** | **float** |  | [optional] [default to 400]
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. | [optional] [readonly] 
**type** | **str** | A URI reference that identifies the problem type | [optional] [readonly] 
**description** | **str** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.error_jsonld import ErrorJsonld

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorJsonld from a JSON string
error_jsonld_instance = ErrorJsonld.from_json(json)
# print the JSON string representation of the object
print(ErrorJsonld.to_json())

# convert the object into a dict
error_jsonld_dict = error_jsonld_instance.to_dict()
# create an instance of ErrorJsonld from a dict
error_jsonld_from_dict = ErrorJsonld.from_dict(error_jsonld_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


