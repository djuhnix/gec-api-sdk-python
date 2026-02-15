# HydraCollectionBaseSchemaNoPagination


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 

## Example

```python
from gec_api_sdk.models.hydra_collection_base_schema_no_pagination import HydraCollectionBaseSchemaNoPagination

# TODO update the JSON string below
json = "{}"
# create an instance of HydraCollectionBaseSchemaNoPagination from a JSON string
hydra_collection_base_schema_no_pagination_instance = HydraCollectionBaseSchemaNoPagination.from_json(json)
# print the JSON string representation of the object
print(HydraCollectionBaseSchemaNoPagination.to_json())

# convert the object into a dict
hydra_collection_base_schema_no_pagination_dict = hydra_collection_base_schema_no_pagination_instance.to_dict()
# create an instance of HydraCollectionBaseSchemaNoPagination from a dict
hydra_collection_base_schema_no_pagination_from_dict = HydraCollectionBaseSchemaNoPagination.from_dict(hydra_collection_base_schema_no_pagination_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


