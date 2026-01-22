# DonationDonationWrite



## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **str** |  | [optional] 
**amount** | **str** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] [default to 'pending']
**payment_method** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.donation_donation_write import DonationDonationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DonationDonationWrite from a JSON string
donation_donation_write_instance = DonationDonationWrite.from_json(json)
# print the JSON string representation of the object
print(DonationDonationWrite.to_json())

# convert the object into a dict
donation_donation_write_dict = donation_donation_write_instance.to_dict()
# create an instance of DonationDonationWrite from a dict
donation_donation_write_from_dict = DonationDonationWrite.from_dict(donation_donation_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


