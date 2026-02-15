# ApiDocumentsGetCollection200Response

Document.jsonld-document.read collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 
**view** | [**HydraCollectionBaseSchemaAllOfView**](HydraCollectionBaseSchemaAllOfView.md) |  | [optional] 
**member** | [**List[DocumentJsonldDocumentRead]**](DocumentJsonldDocumentRead.md) |  | 

## Example

```python
from gec_api_sdk.models.api_documents_get_collection200_response import ApiDocumentsGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsGetCollection200Response from a JSON string
api_documents_get_collection200_response_instance = ApiDocumentsGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsGetCollection200Response.to_json())

# convert the object into a dict
api_documents_get_collection200_response_dict = api_documents_get_collection200_response_instance.to_dict()
# create an instance of ApiDocumentsGetCollection200Response from a dict
api_documents_get_collection200_response_from_dict = ApiDocumentsGetCollection200Response.from_dict(api_documents_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


