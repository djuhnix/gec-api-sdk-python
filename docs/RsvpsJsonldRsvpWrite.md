# RsvpsJsonldRsvpWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**member** | **str** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.rsvps_jsonld_rsvp_write import RsvpsJsonldRsvpWrite

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpsJsonldRsvpWrite from a JSON string
rsvps_jsonld_rsvp_write_instance = RsvpsJsonldRsvpWrite.from_json(json)
# print the JSON string representation of the object
print(RsvpsJsonldRsvpWrite.to_json())

# convert the object into a dict
rsvps_jsonld_rsvp_write_dict = rsvps_jsonld_rsvp_write_instance.to_dict()
# create an instance of RsvpsJsonldRsvpWrite from a dict
rsvps_jsonld_rsvp_write_from_dict = RsvpsJsonldRsvpWrite.from_dict(rsvps_jsonld_rsvp_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


