# EmailTemplateJsonldEmailTemplateWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**subject** | **str** |  | 
**content** | **str** |  | 
**variables** | **List[str]** |  | [optional] 

## Example

```python
from gec_api_sdk.models.email_template_jsonld_email_template_write import EmailTemplateJsonldEmailTemplateWrite

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateJsonldEmailTemplateWrite from a JSON string
email_template_jsonld_email_template_write_instance = EmailTemplateJsonldEmailTemplateWrite.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateJsonldEmailTemplateWrite.to_json())

# convert the object into a dict
email_template_jsonld_email_template_write_dict = email_template_jsonld_email_template_write_instance.to_dict()
# create an instance of EmailTemplateJsonldEmailTemplateWrite from a dict
email_template_jsonld_email_template_write_from_dict = EmailTemplateJsonldEmailTemplateWrite.from_dict(email_template_jsonld_email_template_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


