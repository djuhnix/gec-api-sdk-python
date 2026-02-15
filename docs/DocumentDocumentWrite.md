# DocumentDocumentWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **str** |  | [optional] 
**url** | **str** |  | 
**type** | **str** |  | 
**expires_at** | **datetime** |  | [optional] 
**verified** | **bool** |  | [optional] [default to False]

## Example

```python
from gec_api_sdk.models.document_document_write import DocumentDocumentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentDocumentWrite from a JSON string
document_document_write_instance = DocumentDocumentWrite.from_json(json)
# print the JSON string representation of the object
print(DocumentDocumentWrite.to_json())

# convert the object into a dict
document_document_write_dict = document_document_write_instance.to_dict()
# create an instance of DocumentDocumentWrite from a dict
document_document_write_from_dict = DocumentDocumentWrite.from_dict(document_document_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


