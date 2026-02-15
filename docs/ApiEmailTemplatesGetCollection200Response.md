# ApiEmailTemplatesGetCollection200Response

EmailTemplate.jsonld-email_template.read collection.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total_items** | **int** |  | [optional] 
**search** | [**HydraCollectionBaseSchemaNoPaginationSearch**](HydraCollectionBaseSchemaNoPaginationSearch.md) |  | [optional] 
**view** | [**HydraCollectionBaseSchemaAllOfView**](HydraCollectionBaseSchemaAllOfView.md) |  | [optional] 
**member** | [**List[EmailTemplateJsonldEmailTemplateRead]**](EmailTemplateJsonldEmailTemplateRead.md) |  | 

## Example

```python
from gec_api_sdk.models.api_email_templates_get_collection200_response import ApiEmailTemplatesGetCollection200Response

# TODO update the JSON string below
json = "{}"
# create an instance of ApiEmailTemplatesGetCollection200Response from a JSON string
api_email_templates_get_collection200_response_instance = ApiEmailTemplatesGetCollection200Response.from_json(json)
# print the JSON string representation of the object
print(ApiEmailTemplatesGetCollection200Response.to_json())

# convert the object into a dict
api_email_templates_get_collection200_response_dict = api_email_templates_get_collection200_response_instance.to_dict()
# create an instance of ApiEmailTemplatesGetCollection200Response from a dict
api_email_templates_get_collection200_response_from_dict = ApiEmailTemplatesGetCollection200Response.from_dict(api_email_templates_get_collection200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


