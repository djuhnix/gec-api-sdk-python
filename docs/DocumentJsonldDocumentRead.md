# DocumentJsonldDocumentRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**member** | **str** |  | [optional] 
**url** | **str** |  | 
**type** | **str** |  | 
**uploaded_at** | **datetime** |  | [optional] [readonly] 
**expires_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | [optional] [default to False]
**verified_at** | **datetime** |  | [optional] [readonly] 

## Example

```python
from gec_api_sdk.models.document_jsonld_document_read import DocumentJsonldDocumentRead

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentJsonldDocumentRead from a JSON string
document_jsonld_document_read_instance = DocumentJsonldDocumentRead.from_json(json)
# print the JSON string representation of the object
print(DocumentJsonldDocumentRead.to_json())

# convert the object into a dict
document_jsonld_document_read_dict = document_jsonld_document_read_instance.to_dict()
# create an instance of DocumentJsonldDocumentRead from a dict
document_jsonld_document_read_from_dict = DocumentJsonldDocumentRead.from_dict(document_jsonld_document_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


