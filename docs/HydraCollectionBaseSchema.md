# HydraCollectionBaseSchema


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 
**view** | [**HydraCollectionBaseSchemaAllOfView**](HydraCollectionBaseSchemaAllOfView.md) |  | [optional] 

## Example

```python
from gec_api_sdk.models.hydra_collection_base_schema import HydraCollectionBaseSchema

# TODO update the JSON string below
json = "{}"
# create an instance of HydraCollectionBaseSchema from a JSON string
hydra_collection_base_schema_instance = HydraCollectionBaseSchema.from_json(json)
# print the JSON string representation of the object
print(HydraCollectionBaseSchema.to_json())

# convert the object into a dict
hydra_collection_base_schema_dict = hydra_collection_base_schema_instance.to_dict()
# create an instance of HydraCollectionBaseSchema from a dict
hydra_collection_base_schema_from_dict = HydraCollectionBaseSchema.from_dict(hydra_collection_base_schema_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


