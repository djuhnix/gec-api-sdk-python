# ApiEventsGetCollection200Response

Event.jsonld-event.read collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 
**view** | [**HydraCollectionBaseSchemaAllOfView**](HydraCollectionBaseSchemaAllOfView.md) |  | [optional] 
**member** | [**List[EventJsonldEventRead]**](EventJsonldEventRead.md) |  | 

## Example

```python
from gec_api_sdk.models.api_events_get_collection200_response import ApiEventsGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEventsGetCollection200Response from a JSON string
api_events_get_collection200_response_instance = ApiEventsGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiEventsGetCollection200Response.to_json())

# convert the object into a dict
api_events_get_collection200_response_dict = api_events_get_collection200_response_instance.to_dict()
# create an instance of ApiEventsGetCollection200Response from a dict
api_events_get_collection200_response_from_dict = ApiEventsGetCollection200Response.from_dict(api_events_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


