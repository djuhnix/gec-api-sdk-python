# ApiDocumentsGetCollection200ResponseView


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**first** | **str** |  | [optional] 
**last** | **str** |  | [optional] 
**previous** | **str** |  | [optional] 
**next** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.api_documents_get_collection200_response_view import ApiDocumentsGetCollection200ResponseView

# TODO update the JSON string below
json = "{}"
# create an instance of ApiDocumentsGetCollection200ResponseView from a JSON string
api_documents_get_collection200_response_view_instance = ApiDocumentsGetCollection200ResponseView.from_json(json)
# print the JSON string representation of the object
print(ApiDocumentsGetCollection200ResponseView.to_json())

# convert the object into a dict
api_documents_get_collection200_response_view_dict = api_documents_get_collection200_response_view_instance.to_dict()
# create an instance of ApiDocumentsGetCollection200ResponseView from a dict
api_documents_get_collection200_response_view_from_dict = ApiDocumentsGetCollection200ResponseView.from_dict(api_documents_get_collection200_response_view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


