# DocumentCsvDocumentRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from gec_api_sdk.models.document_csv_document_read import DocumentCsvDocumentRead

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentCsvDocumentRead from a JSON string
document_csv_document_read_instance = DocumentCsvDocumentRead.from_json(json)
# print the JSON string representation of the object
print(DocumentCsvDocumentRead.to_json())

# convert the object into a dict
document_csv_document_read_dict = document_csv_document_read_instance.to_dict()
# create an instance of DocumentCsvDocumentRead from a dict
document_csv_document_read_from_dict = DocumentCsvDocumentRead.from_dict(document_csv_document_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


