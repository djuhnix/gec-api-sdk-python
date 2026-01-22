# ApiDocumentsGetCollection200ResponseSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**variable_representation** | **str** |  | [optional] 
**mapping** | [**List[ApiDocumentsGetCollection200ResponseSearchMappingInner]**](ApiDocumentsGetCollection200ResponseSearchMappingInner.md) |  | [optional] 

## Example

```python
from gec_api_sdk.models.api_documents_get_collection200_response_search import ApiDocumentsGetCollection200ResponseSearch

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsGetCollection200ResponseSearch from a JSON string
api_documents_get_collection200_response_search_instance = ApiDocumentsGetCollection200ResponseSearch.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsGetCollection200ResponseSearch.to_json())

# convert the object into a dict
api_documents_get_collection200_response_search_dict = api_documents_get_collection200_response_search_instance.to_dict()
# create an instance of ApiDocumentsGetCollection200ResponseSearch from a dict
api_documents_get_collection200_response_search_from_dict = ApiDocumentsGetCollection200ResponseSearch.from_dict(api_documents_get_collection200_response_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


