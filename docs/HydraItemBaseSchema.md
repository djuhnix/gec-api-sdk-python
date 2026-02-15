# HydraItemBaseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**HydraItemBaseSchemaContext**](HydraItemBaseSchemaContext.md) |  | [optional] 
**id** | **str** |  | 
**type** | **str** |  | 

## Example

```python
from gec_api_sdk.models.hydra_item_base_schema import HydraItemBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HydraItemBaseSchema from a JSON string
hydra_item_base_schema_instance = HydraItemBaseSchema.from_json(json)
# print the JSON string representation of the object
print(HydraItemBaseSchema.to_json())

# convert the object into a dict
hydra_item_base_schema_dict = hydra_item_base_schema_instance.to_dict()
# create an instance of HydraItemBaseSchema from a dict
hydra_item_base_schema_from_dict = HydraItemBaseSchema.from_dict(hydra_item_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


