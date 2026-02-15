# RsvpsRsvpWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**member** | **str** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.rsvps_rsvp_write import RsvpsRsvpWrite

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpsRsvpWrite from a JSON string
rsvps_rsvp_write_instance = RsvpsRsvpWrite.from_json(json)
# print the JSON string representation of the object
print(RsvpsRsvpWrite.to_json())

# convert the object into a dict
rsvps_rsvp_write_dict = rsvps_rsvp_write_instance.to_dict()
# create an instance of RsvpsRsvpWrite from a dict
rsvps_rsvp_write_from_dict = RsvpsRsvpWrite.from_dict(rsvps_rsvp_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


