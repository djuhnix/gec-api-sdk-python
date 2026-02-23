# ApiMembersGetCollection200Response

Member.jsonld-member.read collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 
**context** | [**HydraItemBaseSchemaContext**](HydraItemBaseSchemaContext.md) |  | [optional] 
**id** | **str** |  | 
**type** | **str** |  | 
**view** | [**HydraCollectionBaseSchemaAllOfView**](HydraCollectionBaseSchemaAllOfView.md) |  | [optional] 
**member** | [**List[MemberJsonldMemberRead]**](MemberJsonldMemberRead.md) |  | 

## Example

```python
from gec_api_sdk.models.api_members_get_collection200_response import ApiMembersGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiMembersGetCollection200Response from a JSON string
api_members_get_collection200_response_instance = ApiMembersGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiMembersGetCollection200Response.to_json())

# convert the object into a dict
api_members_get_collection200_response_dict = api_members_get_collection200_response_instance.to_dict()
# create an instance of ApiMembersGetCollection200Response from a dict
api_members_get_collection200_response_from_dict = ApiMembersGetCollection200Response.from_dict(api_members_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


