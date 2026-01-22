# LoginCheckPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from gec_api_sdk.models.login_check_post_request import LoginCheckPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of LoginCheckPostRequest from a JSON string
login_check_post_request_instance = LoginCheckPostRequest.from_json(json)
# print the JSON string representation of the object
print(LoginCheckPostRequest.to_json())

# convert the object into a dict
login_check_post_request_dict = login_check_post_request_instance.to_dict()
# create an instance of LoginCheckPostRequest from a dict
login_check_post_request_from_dict = LoginCheckPostRequest.from_dict(login_check_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


