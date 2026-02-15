# RsvpsYamlRsvpRead


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
from gec_api_sdk.models.rsvps_yaml_rsvp_read import RsvpsYamlRsvpRead

# TODO update the JSON string below
json = "{}"
# create an instance of RsvpsYamlRsvpRead from a JSON string
rsvps_yaml_rsvp_read_instance = RsvpsYamlRsvpRead.from_json(json)
# print the JSON string representation of the object
print(RsvpsYamlRsvpRead.to_json())

# convert the object into a dict
rsvps_yaml_rsvp_read_dict = rsvps_yaml_rsvp_read_instance.to_dict()
# create an instance of RsvpsYamlRsvpRead from a dict
rsvps_yaml_rsvp_read_from_dict = RsvpsYamlRsvpRead.from_dict(rsvps_yaml_rsvp_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


