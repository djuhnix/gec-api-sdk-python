# RsvpsJsonldRsvpRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**event** | **str** |  | 
**member** | **str** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.rsvps_jsonld_rsvp_read import RsvpsJsonldRsvpRead

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpsJsonldRsvpRead from a JSON string
rsvps_jsonld_rsvp_read_instance = RsvpsJsonldRsvpRead.from_json(json)
# print the JSON string representation of the object
print(RsvpsJsonldRsvpRead.to_json())

# convert the object into a dict
rsvps_jsonld_rsvp_read_dict = rsvps_jsonld_rsvp_read_instance.to_dict()
# create an instance of RsvpsJsonldRsvpRead from a dict
rsvps_jsonld_rsvp_read_from_dict = RsvpsJsonldRsvpRead.from_dict(rsvps_jsonld_rsvp_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


