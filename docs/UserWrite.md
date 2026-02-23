# UserWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**plain_password** | **str** |  | 
**roles** | **List[str]** |  | [optional] 
**google_service_account** | **str** |  | [optional] 
**google_service_account_scopes** | **List[Optional[str]]** |  | [optional] 
**google_impersonated_user** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.user_write import UserWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserWrite from a JSON string
user_write_instance = UserWrite.from_json(json)
# print the JSON string representation of the object
print(UserWrite.to_json())

# convert the object into a dict
user_write_dict = user_write_instance.to_dict()
# create an instance of UserWrite from a dict
user_write_from_dict = UserWrite.from_dict(user_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


