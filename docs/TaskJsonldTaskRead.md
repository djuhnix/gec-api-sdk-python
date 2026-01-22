# TaskJsonldTaskRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**title** | **str** |  | 
**description** | **str** |  | [optional] 
**status** | **str** |  | [optional] [default to 'pending']
**assignee** | **str** |  | [optional] 
**due_date** | **datetime** |  | [optional] 
**priority** | **str** |  | [optional] 
**related_event** | **str** |  | [optional] 
**related_member** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.task_jsonld_task_read import TaskJsonldTaskRead

# TODO update the JSON string below
json = "{}"
# create an instance of TaskJsonldTaskRead from a JSON string
task_jsonld_task_read_instance = TaskJsonldTaskRead.from_json(json)
# print the JSON string representation of the object
print(TaskJsonldTaskRead.to_json())

# convert the object into a dict
task_jsonld_task_read_dict = task_jsonld_task_read_instance.to_dict()
# create an instance of TaskJsonldTaskRead from a dict
task_jsonld_task_read_from_dict = TaskJsonldTaskRead.from_dict(task_jsonld_task_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


