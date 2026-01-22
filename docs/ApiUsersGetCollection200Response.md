# ApiUsersGetCollection200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**List[UserJsonldUserRead]**](UserJsonldUserRead.md) |  | 
**total_items** | **int** |  | [optional] 
**view** | [**ApiDocumentsGetCollection200ResponseView**](ApiDocumentsGetCollection200ResponseView.md) |  | [optional] 
**search** | [**ApiDocumentsGetCollection200ResponseSearch**](ApiDocumentsGetCollection200ResponseSearch.md) |  | [optional] 

## Example

```python
from gec_api_sdk.models.api_users_get_collection200_response import ApiUsersGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiUsersGetCollection200Response from a JSON string
api_users_get_collection200_response_instance = ApiUsersGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiUsersGetCollection200Response.to_json())

# convert the object into a dict
api_users_get_collection200_response_dict = api_users_get_collection200_response_instance.to_dict()
# create an instance of ApiUsersGetCollection200Response from a dict
api_users_get_collection200_response_from_dict = ApiUsersGetCollection200Response.from_dict(api_users_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


