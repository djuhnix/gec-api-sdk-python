# DonationJsonldDonationRead



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | [**ConstraintViolationJsonldJsonldContext**](ConstraintViolationJsonldJsonldContext.md) |  | [optional] 
**id** | **str** |  | [optional] [readonly] 
**type** | **str** |  | [optional] [readonly] 
**id** | **str** |  | [optional] [readonly] 
**member** | **str** |  | [optional] 
**amount** | **str** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] [default to 'pending']
**payment_method** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] [readonly] 
**updated_at** | **datetime** |  | [optional] 

## Example

```python
from gec_api_sdk.models.donation_jsonld_donation_read import DonationJsonldDonationRead

# TODO update the JSON string below
json = "{}"
# create an instance of DonationJsonldDonationRead from a JSON string
donation_jsonld_donation_read_instance = DonationJsonldDonationRead.from_json(json)
# print the JSON string representation of the object
print(DonationJsonldDonationRead.to_json())

# convert the object into a dict
donation_jsonld_donation_read_dict = donation_jsonld_donation_read_instance.to_dict()
# create an instance of DonationJsonldDonationRead from a dict
donation_jsonld_donation_read_from_dict = DonationJsonldDonationRead.from_dict(donation_jsonld_donation_read_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


