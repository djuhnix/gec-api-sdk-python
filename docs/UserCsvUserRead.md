# UserCsvUserRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**email** | **str** |  | 
**roles** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 
**google_service_account** | **str** |  | [optional] 
**google_service_account_scopes** | **List[Optional[str]]** |  | [optional] 
**google_impersonated_user** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.user_csv_user_read import UserCsvUserRead

# TODO update the JSON string below
json = "{}"
# create an instance of UserCsvUserRead from a JSON string
user_csv_user_read_instance = UserCsvUserRead.from_json(json)
# print the JSON string representation of the object
print(UserCsvUserRead.to_json())

# convert the object into a dict
user_csv_user_read_dict = user_csv_user_read_instance.to_dict()
# create an instance of UserCsvUserRead from a dict
user_csv_user_read_from_dict = UserCsvUserRead.from_dict(user_csv_user_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


