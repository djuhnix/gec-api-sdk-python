# TaskWrite


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
from gec_api_sdk.models.task_write import TaskWrite

# TODO update the JSON string below
json = "{}"
# create an instance of TaskWrite from a JSON string
task_write_instance = TaskWrite.from_json(json)
# print the JSON string representation of the object
print(TaskWrite.to_json())

# convert the object into a dict
task_write_dict = task_write_instance.to_dict()
# create an instance of TaskWrite from a dict
task_write_from_dict = TaskWrite.from_dict(task_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


