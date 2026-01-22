# HelloAssoDataDTO



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payer** | [**HelloAssoPayerDTO**](HelloAssoPayerDTO.md) |  | 
**items** | **List[str]** |  | 
**payments** | **List[str]** |  | 
**amount** | [**HelloAssoAmountDTO**](HelloAssoAmountDTO.md) |  | 
**id** | **int** |  | 
**var_date** | **str** |  | 
**form_slug** | **str** |  | 
**form_type** | **str** |  | 
**organization_name** | **str** |  | 
**organization_slug** | **str** |  | 
**organization_type** | **str** |  | 
**organization_is_under_coluche_law** | **bool** |  | [optional] 
**meta** | [**HelloAssoMetaDTO**](HelloAssoMetaDTO.md) |  | 
**is_anonymous** | **bool** |  | [optional] 
**is_amount_hidden** | **bool** |  | [optional] 

## Example

```python
from gec_api_sdk.models.hello_asso_data_dto import HelloAssoDataDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoDataDTO from a JSON string
hello_asso_data_dto_instance = HelloAssoDataDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoDataDTO.to_json())

# convert the object into a dict
hello_asso_data_dto_dict = hello_asso_data_dto_instance.to_dict()
# create an instance of HelloAssoDataDTO from a dict
hello_asso_data_dto_from_dict = HelloAssoDataDTO.from_dict(hello_asso_data_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


