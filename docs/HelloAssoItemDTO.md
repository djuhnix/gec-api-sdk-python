# HelloAssoItemDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payments** | **List[Optional[str]]** |  | 
**name** | **str** |  | 
**user** | **List[Optional[str]]** |  | [optional] 
**price_category** | **str** |  | 
**custom_fields** | [**List[HelloAssoCustomFieldDTO]**](HelloAssoCustomFieldDTO.md) |  | 
**qr_code** | **str** |  | [optional] 
**tier_description** | **str** |  | [optional] 
**tier_id** | **int** |  | [optional] 
**id** | **int** |  | 
**amount** | **int** |  | 
**type** | **str** |  | 
**initial_amount** | **int** |  | 
**state** | **str** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_item_dto import HelloAssoItemDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoItemDTO from a JSON string
hello_asso_item_dto_instance = HelloAssoItemDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoItemDTO.to_json())

# convert the object into a dict
hello_asso_item_dto_dict = hello_asso_item_dto_instance.to_dict()
# create an instance of HelloAssoItemDTO from a dict
hello_asso_item_dto_from_dict = HelloAssoItemDTO.from_dict(hello_asso_item_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


