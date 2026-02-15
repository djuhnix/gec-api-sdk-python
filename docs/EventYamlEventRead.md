# EventYamlEventRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | [optional] 
**location** | **str** |  | [optional] 
**max_attendees** | **int** |  | [optional] 
**current_attendees** | **int** |  | [optional] [default to 0]
**status** | **str** |  | [optional] [default to 'draft']
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**rsvps** | **List[str]** |  | [optional] 
**tasks** | **List[str]** |  | [optional] 

## Example

```python
from gec_api_sdk.models.event_yaml_event_read import EventYamlEventRead

# TODO update the JSON string below
json = "{}"
# create an instance of EventYamlEventRead from a JSON string
event_yaml_event_read_instance = EventYamlEventRead.from_json(json)
# print the JSON string representation of the object
print(EventYamlEventRead.to_json())

# convert the object into a dict
event_yaml_event_read_dict = event_yaml_event_read_instance.to_dict()
# create an instance of EventYamlEventRead from a dict
event_yaml_event_read_from_dict = EventYamlEventRead.from_dict(event_yaml_event_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


