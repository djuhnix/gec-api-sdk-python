# UserUserWriteJsonMergePatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | [optional] 
**plain_password** | **str** |  | [optional] 
**roles** | **List[str]** |  | [optional] 
**google_service_account** | **str** |  | [optional] 
**google_service_account_scopes** | **List[Optional[str]]** |  | [optional] 
**google_impersonated_user** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.user_user_write_json_merge_patch import UserUserWriteJsonMergePatch

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserWriteJsonMergePatch from a JSON string
user_user_write_json_merge_patch_instance = UserUserWriteJsonMergePatch.from_json(json)
# print the JSON string representation of the object
print(UserUserWriteJsonMergePatch.to_json())

# convert the object into a dict
user_user_write_json_merge_patch_dict = user_user_write_json_merge_patch_instance.to_dict()
# create an instance of UserUserWriteJsonMergePatch from a dict
user_user_write_json_merge_patch_from_dict = UserUserWriteJsonMergePatch.from_dict(user_user_write_json_merge_patch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


