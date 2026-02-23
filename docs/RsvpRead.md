# RsvpRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**event** | **str** |  | 
**member** | **str** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.rsvp_read import RsvpRead

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpRead from a JSON string
rsvp_read_instance = RsvpRead.from_json(json)
# print the JSON string representation of the object
print(RsvpRead.to_json())

# convert the object into a dict
rsvp_read_dict = rsvp_read_instance.to_dict()
# create an instance of RsvpRead from a dict
rsvp_read_from_dict = RsvpRead.from_dict(rsvp_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


