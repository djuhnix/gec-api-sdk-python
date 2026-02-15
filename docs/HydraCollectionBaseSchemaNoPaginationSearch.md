# HydraCollectionBaseSchemaNoPaginationSearch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**template** | **str** |  | [optional] 
**variable_representation** | **str** |  | [optional] 
**mapping** | [**List[HydraCollectionBaseSchemaNoPaginationSearchMappingInner]**](HydraCollectionBaseSchemaNoPaginationSearchMappingInner.md) |  | [optional] 

## Example

```python
from gec_api_sdk.models.hydra_collection_base_schema_no_pagination_search import HydraCollectionBaseSchemaNoPaginationSearch

# TODO update the JSON string below
json = "{}"
# create an instance of HydraCollectionBaseSchemaNoPaginationSearch from a JSON string
hydra_collection_base_schema_no_pagination_search_instance = HydraCollectionBaseSchemaNoPaginationSearch.from_json(json)
# print the JSON string representation of the object
print(HydraCollectionBaseSchemaNoPaginationSearch.to_json())

# convert the object into a dict
hydra_collection_base_schema_no_pagination_search_dict = hydra_collection_base_schema_no_pagination_search_instance.to_dict()
# create an instance of HydraCollectionBaseSchemaNoPaginationSearch from a dict
hydra_collection_base_schema_no_pagination_search_from_dict = HydraCollectionBaseSchemaNoPaginationSearch.from_dict(hydra_collection_base_schema_no_pagination_search_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


