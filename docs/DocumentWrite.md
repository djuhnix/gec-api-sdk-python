# DocumentWrite


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
from gec_api_sdk.models.document_write import DocumentWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentWrite from a JSON string
document_write_instance = DocumentWrite.from_json(json)
# print the JSON string representation of the object
print(DocumentWrite.to_json())

# convert the object into a dict
document_write_dict = document_write_instance.to_dict()
# create an instance of DocumentWrite from a dict
document_write_from_dict = DocumentWrite.from_dict(document_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


