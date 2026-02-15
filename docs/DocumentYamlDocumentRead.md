# DocumentYamlDocumentRead


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
from gec_api_sdk.models.document_yaml_document_read import DocumentYamlDocumentRead

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentYamlDocumentRead from a JSON string
document_yaml_document_read_instance = DocumentYamlDocumentRead.from_json(json)
# print the JSON string representation of the object
print(DocumentYamlDocumentRead.to_json())

# convert the object into a dict
document_yaml_document_read_dict = document_yaml_document_read_instance.to_dict()
# create an instance of DocumentYamlDocumentRead from a dict
document_yaml_document_read_from_dict = DocumentYamlDocumentRead.from_dict(document_yaml_document_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


