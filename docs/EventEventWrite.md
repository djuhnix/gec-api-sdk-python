# EventEventWrite



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
from gec_api_sdk.models.event_event_write import EventEventWrite

# TODO update the JSON string below
json = "{}"
# create an instance of EventEventWrite from a JSON string
event_event_write_instance = EventEventWrite.from_json(json)
# print the JSON string representation of the object
print(EventEventWrite.to_json())

# convert the object into a dict
event_event_write_dict = event_event_write_instance.to_dict()
# create an instance of EventEventWrite from a dict
event_event_write_from_dict = EventEventWrite.from_dict(event_event_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


