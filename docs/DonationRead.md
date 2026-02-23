# DonationRead


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] [readonly] 
**member** | **str** |  | [optional] 
**amount** | **float** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] [default to 'pending']
**payment_method** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.donation_read import DonationRead

# TODO update the JSON string below
json = "{}"
# create an instance of DonationRead from a JSON string
donation_read_instance = DonationRead.from_json(json)
# print the JSON string representation of the object
print(DonationRead.to_json())

# convert the object into a dict
donation_read_dict = donation_read_instance.to_dict()
# create an instance of DonationRead from a dict
donation_read_from_dict = DonationRead.from_dict(donation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


