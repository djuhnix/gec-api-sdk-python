# EmailTemplateEmailTemplateRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**name** | **str** |  | 
**subject** | **str** |  | 
**content** | **str** |  | 
**variables** | **List[str]** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.email_template_email_template_read import EmailTemplateEmailTemplateRead

# TODO update the JSON string below
json = "{}"
# create an instance of EmailTemplateEmailTemplateRead from a JSON string
email_template_email_template_read_instance = EmailTemplateEmailTemplateRead.from_json(json)
# print the JSON string representation of the object
print(EmailTemplateEmailTemplateRead.to_json())

# convert the object into a dict
email_template_email_template_read_dict = email_template_email_template_read_instance.to_dict()
# create an instance of EmailTemplateEmailTemplateRead from a dict
email_template_email_template_read_from_dict = EmailTemplateEmailTemplateRead.from_dict(email_template_email_template_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


