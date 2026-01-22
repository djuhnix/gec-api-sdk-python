# HelloAssoAmountDTO



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **int** |  | 
**vat** | **int** |  | 
**discount** | **int** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_amount_dto import HelloAssoAmountDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoAmountDTO from a JSON string
hello_asso_amount_dto_instance = HelloAssoAmountDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoAmountDTO.to_json())

# convert the object into a dict
hello_asso_amount_dto_dict = hello_asso_amount_dto_instance.to_dict()
# create an instance of HelloAssoAmountDTO from a dict
hello_asso_amount_dto_from_dict = HelloAssoAmountDTO.from_dict(hello_asso_amount_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


