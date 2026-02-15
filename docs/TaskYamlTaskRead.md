# TaskYamlTaskRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from gec_api_sdk.models.task_yaml_task_read import TaskYamlTaskRead

# TODO update the JSON string below
json = "{}"
# create an instance of TaskYamlTaskRead from a JSON string
task_yaml_task_read_instance = TaskYamlTaskRead.from_json(json)
# print the JSON string representation of the object
print(TaskYamlTaskRead.to_json())

# convert the object into a dict
task_yaml_task_read_dict = task_yaml_task_read_instance.to_dict()
# create an instance of TaskYamlTaskRead from a dict
task_yaml_task_read_from_dict = TaskYamlTaskRead.from_dict(task_yaml_task_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


