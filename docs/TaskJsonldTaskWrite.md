# TaskJsonldTaskWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'pending']
**assignee** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**priority** | **str** |  | [optional] 
**related_event** | **str** |  | [optional] 
**related_member** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.task_jsonld_task_write import TaskJsonldTaskWrite

# TODO update the JSON string below
json = "{}"
# create an instance of TaskJsonldTaskWrite from a JSON string
task_jsonld_task_write_instance = TaskJsonldTaskWrite.from_json(json)
# print the JSON string representation of the object
print(TaskJsonldTaskWrite.to_json())

# convert the object into a dict
task_jsonld_task_write_dict = task_jsonld_task_write_instance.to_dict()
# create an instance of TaskJsonldTaskWrite from a dict
task_jsonld_task_write_from_dict = TaskJsonldTaskWrite.from_dict(task_jsonld_task_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


