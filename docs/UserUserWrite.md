# UserUserWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**plain_password** | **str** |  | 
**roles** | **List[str]** |  | [optional] 
**google_service_account** | **str** |  | [optional] 
**google_service_account_scopes** | **List[str]** |  | [optional] 
**google_impersonated_user** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.user_user_write import UserUserWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserUserWrite from a JSON string
user_user_write_instance = UserUserWrite.from_json(json)
# print the JSON string representation of the object
print(UserUserWrite.to_json())

# convert the object into a dict
user_user_write_dict = user_user_write_instance.to_dict()
# create an instance of UserUserWrite from a dict
user_user_write_from_dict = UserUserWrite.from_dict(user_user_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


