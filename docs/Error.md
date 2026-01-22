# Error

A representation of common errors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** | A short, human-readable summary of the problem. | [optional] [readonly] 
**detail** | **str** | A human-readable explanation specific to this occurrence of the problem. | [optional] [readonly] 
**status** | **float** |  | [optional] [default to 400]
**instance** | **str** | A URI reference that identifies the specific occurrence of the problem. It may or may not yield further information if dereferenced. | [optional] [readonly] 
**type** | **str** | A URI reference that identifies the problem type | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.error import Error

# TODO update the JSON string below
json = "{}"
# create an instance of Error from a JSON string
error_instance = Error.from_json(json)
# print the JSON string representation of the object
print(Error.to_json())

# convert the object into a dict
error_dict = error_instance.to_dict()
# create an instance of Error from a dict
error_from_dict = Error.from_dict(error_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


