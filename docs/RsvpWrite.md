# RsvpWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**event** | **str** |  | 
**member** | **str** |  | 
**status** | **str** |  | 
**notes** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.rsvp_write import RsvpWrite

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpWrite from a JSON string
rsvp_write_instance = RsvpWrite.from_json(json)
# print the JSON string representation of the object
print(RsvpWrite.to_json())

# convert the object into a dict
rsvp_write_dict = rsvp_write_instance.to_dict()
# create an instance of RsvpWrite from a dict
rsvp_write_from_dict = RsvpWrite.from_dict(rsvp_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


