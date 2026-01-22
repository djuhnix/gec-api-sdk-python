# UserJsonldUserRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**email** | **str** |  | 
**roles** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**google_service_account** | **str** |  | [optional] 
**google_service_account_scopes** | **List[str]** |  | [optional] 
**google_impersonated_user** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.user_jsonld_user_read import UserJsonldUserRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserRead from a JSON string
user_jsonld_user_read_instance = UserJsonldUserRead.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserRead.to_json())

# convert the object into a dict
user_jsonld_user_read_dict = user_jsonld_user_read_instance.to_dict()
# create an instance of UserJsonldUserRead from a dict
user_jsonld_user_read_from_dict = UserJsonldUserRead.from_dict(user_jsonld_user_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


