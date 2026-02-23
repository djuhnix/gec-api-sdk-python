# DonationWrite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | **str** |  | [optional] 
**amount** | **float** |  | 
**currency** | **str** |  | [optional] [default to 'EUR']
**status** | **str** |  | [optional] [default to 'pending']
**payment_method** | **str** |  | [optional] 
**notes** | **str** |  | [optional] 

## Example

```python
from gec_api_sdk.models.donation_write import DonationWrite

# TODO update the JSON string below
json = "{}"
# create an instance of DonationWrite from a JSON string
donation_write_instance = DonationWrite.from_json(json)
# print the JSON string representation of the object
print(DonationWrite.to_json())

# convert the object into a dict
donation_write_dict = donation_write_instance.to_dict()
# create an instance of DonationWrite from a dict
donation_write_from_dict = DonationWrite.from_dict(donation_write_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


