# UserJsonldUserWrite



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
from gec_api_sdk.models.user_jsonld_user_write import UserJsonldUserWrite

# TODO update the JSON string below
json = "{}"
# create an instance of UserJsonldUserWrite from a JSON string
user_jsonld_user_write_instance = UserJsonldUserWrite.from_json(json)
# print the JSON string representation of the object
print(UserJsonldUserWrite.to_json())

# convert the object into a dict
user_jsonld_user_write_dict = user_jsonld_user_write_instance.to_dict()
# create an instance of UserJsonldUserWrite from a dict
user_jsonld_user_write_from_dict = UserJsonldUserWrite.from_dict(user_jsonld_user_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


