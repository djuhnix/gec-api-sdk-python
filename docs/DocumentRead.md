# DocumentRead


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
from gec_api_sdk.models.document_read import DocumentRead

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentRead from a JSON string
document_read_instance = DocumentRead.from_json(json)
# print the JSON string representation of the object
print(DocumentRead.to_json())

# convert the object into a dict
document_read_dict = document_read_instance.to_dict()
# create an instance of DocumentRead from a dict
document_read_from_dict = DocumentRead.from_dict(document_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


