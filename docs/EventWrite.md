# EventWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**start_date** | **datetime** |  | 
**end_date** | **datetime** |  | [optional] 
**location** | **str** |  | [optional] 
**max_attendees** | **int** |  | [optional] 
**status** | **str** |  | [optional] [default to 'draft']

## Example

```python
from gec_api_sdk.models.event_write import EventWrite

# TODO update the JSON string below
json = "{}"
# create an instance of EventWrite from a JSON string
event_write_instance = EventWrite.from_json(json)
# print the JSON string representation of the object
print(EventWrite.to_json())

# convert the object into a dict
event_write_dict = event_write_instance.to_dict()
# create an instance of EventWrite from a dict
event_write_from_dict = EventWrite.from_dict(event_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


