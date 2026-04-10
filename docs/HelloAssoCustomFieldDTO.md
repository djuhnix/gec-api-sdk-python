# HelloAssoCustomFieldDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | 
**name** | **str** |  | 
**type** | **str** |  | 
**answer** | **str** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_custom_field_dto import HelloAssoCustomFieldDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoCustomFieldDTO from a JSON string
hello_asso_custom_field_dto_instance = HelloAssoCustomFieldDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoCustomFieldDTO.to_json())

# convert the object into a dict
hello_asso_custom_field_dto_dict = hello_asso_custom_field_dto_instance.to_dict()
# create an instance of HelloAssoCustomFieldDTO from a dict
hello_asso_custom_field_dto_from_dict = HelloAssoCustomFieldDTO.from_dict(hello_asso_custom_field_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


