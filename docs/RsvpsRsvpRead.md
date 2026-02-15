# RsvpsRsvpRead


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
from gec_api_sdk.models.rsvps_rsvp_read import RsvpsRsvpRead

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpsRsvpRead from a JSON string
rsvps_rsvp_read_instance = RsvpsRsvpRead.from_json(json)
# print the JSON string representation of the object
print(RsvpsRsvpRead.to_json())

# convert the object into a dict
rsvps_rsvp_read_dict = rsvps_rsvp_read_instance.to_dict()
# create an instance of RsvpsRsvpRead from a dict
rsvps_rsvp_read_from_dict = RsvpsRsvpRead.from_dict(rsvps_rsvp_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


