# HelloAssoPaymentDTO


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**items** | **List[Optional[str]]** |  | 
**cash_out_state** | **str** |  | 
**payment_receipt_url** | **str** |  | 
**id** | **int** |  | 
**amount** | **int** |  | 
**var_date** | **str** |  | 
**payment_means** | **str** |  | 
**installment_number** | **int** |  | 
**state** | **str** |  | 
**meta** | [**HelloAssoMetaDTO**](HelloAssoMetaDTO.md) |  | 
**refund_operations** | **List[Optional[str]]** |  | 

## Example

```python
from gec_api_sdk.models.hello_asso_payment_dto import HelloAssoPaymentDTO

# TODO update the JSON string below
json = "{}"
# create an instance of HelloAssoPaymentDTO from a JSON string
hello_asso_payment_dto_instance = HelloAssoPaymentDTO.from_json(json)
# print the JSON string representation of the object
print(HelloAssoPaymentDTO.to_json())

# convert the object into a dict
hello_asso_payment_dto_dict = hello_asso_payment_dto_instance.to_dict()
# create an instance of HelloAssoPaymentDTO from a dict
hello_asso_payment_dto_from_dict = HelloAssoPaymentDTO.from_dict(hello_asso_payment_dto_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


