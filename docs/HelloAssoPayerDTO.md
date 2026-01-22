# HelloAssoPayerDTO



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**country** | **str** |  | 
**first_name** | **str** |  | 
**last_name** | **str** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_payer_dto import HelloAssoPayerDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoPayerDTO from a JSON string
hello_asso_payer_dto_instance = HelloAssoPayerDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoPayerDTO.to_json())

# convert the object into a dict
hello_asso_payer_dto_dict = hello_asso_payer_dto_instance.to_dict()
# create an instance of HelloAssoPayerDTO from a dict
hello_asso_payer_dto_from_dict = HelloAssoPayerDTO.from_dict(hello_asso_payer_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


