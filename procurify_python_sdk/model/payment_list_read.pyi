# coding: utf-8

"""
    Procurify API Documentation

     # Disclaimer  - Procurify’s API is evolving and is subject to change at any time. Additionally, aspects of the API are undocumented, including certain methods, events, and properties. Given that both documented and undocumented aspects of the Procurify API may change at any time, the client relies on the API at their own risk. - Client (and/or client’s representative) is responsible for building, testing, and maintaining any API connection between Procurify and any other tool.  Procurify’s responsibility strictly involves providing support on clarifications in regards to the issued API document. - Procurify’s API is offered on an “as is” and “as available” basis, without warranties of any kind. By accepting this agreement, you agree that you have read the current API documentation, and accept the API functionality in its current state including current limitations. For questions and clarification around the documentation, please contact support@procurify.com. - In accordance with Section 2.(b) of our Subscription Services Agreement, Procurify reserves the right to deny access to our API at any time. If your API requests are too large and time out, contact us immediately to avoid possible suspension of access. - You may not attempt to reverse engineer or otherwise derive source code, trade secrets, or know-how in the Procurify API or portion thereof. You may not use the Procurify API to replicate or compete with core products or services offered by Procurify. 

    Generated by: https://konfigthis.com
"""

from datetime import date, datetime  # noqa: F401
import decimal  # noqa: F401
import functools  # noqa: F401
import io  # noqa: F401
import re  # noqa: F401
import typing  # noqa: F401
import typing_extensions  # noqa: F401
import uuid  # noqa: F401

import frozendict  # noqa: F401

from procurify_python_sdk import schemas  # noqa: F401


class PaymentListRead(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "currency",
            "payment_method",
        }
        
        class properties:
        
            @staticmethod
            def payment_method() -> typing.Type['CompanyPaymentMethodReadNullable']:
                return CompanyPaymentMethodReadNullable
        
            @staticmethod
            def currency() -> typing.Type['Currency']:
                return Currency
            id = schemas.IntSchema
            
            
            class bill_payments(
                schemas.ListBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneTupleMixin
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['BillPaymentDocs']:
                        return BillPaymentDocs
            
            
                def __new__(
                    cls,
                    *args: typing.Union[list, tuple, None, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'bill_payments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            payment_method_type = schemas.IntSchema
            
            
            class payment_date(
                schemas.DateBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, date, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class amount(
                schemas.StrSchema
            ):
                pass
            total_amount_with_tax = schemas.StrSchema
            tax_amount = schemas.StrSchema
            inclusive_tax_amount = schemas.StrSchema
            exclusive_tax_amount = schemas.StrSchema
        
            @staticmethod
            def status() -> typing.Type['PaymentStatusEnum']:
                return PaymentStatusEnum
            ach_number = schemas.IntSchema
            
            
            class next_approver_choices(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['ApproverRead']:
                        return ApproverRead
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['ApproverRead'], typing.List['ApproverRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'next_approver_choices':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'ApproverRead':
                    return super().__getitem__(i)
            __annotations__ = {
                "payment_method": payment_method,
                "currency": currency,
                "id": id,
                "bill_payments": bill_payments,
                "payment_method_type": payment_method_type,
                "payment_date": payment_date,
                "amount": amount,
                "total_amount_with_tax": total_amount_with_tax,
                "tax_amount": tax_amount,
                "inclusive_tax_amount": inclusive_tax_amount,
                "exclusive_tax_amount": exclusive_tax_amount,
                "status": status,
                "ach_number": ach_number,
                "next_approver_choices": next_approver_choices,
            }
    
    currency: 'Currency'
    payment_method: 'CompanyPaymentMethodReadNullable'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method"]) -> 'CompanyPaymentMethodReadNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bill_payments"]) -> MetaOapg.properties.bill_payments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method_type"]) -> MetaOapg.properties.payment_method_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_date"]) -> MetaOapg.properties.payment_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["amount"]) -> MetaOapg.properties.amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["total_amount_with_tax"]) -> MetaOapg.properties.total_amount_with_tax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax_amount"]) -> MetaOapg.properties.tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inclusive_tax_amount"]) -> MetaOapg.properties.inclusive_tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["exclusive_tax_amount"]) -> MetaOapg.properties.exclusive_tax_amount: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> 'PaymentStatusEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["ach_number"]) -> MetaOapg.properties.ach_number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_approver_choices"]) -> MetaOapg.properties.next_approver_choices: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["payment_method", "currency", "id", "bill_payments", "payment_method_type", "payment_date", "amount", "total_amount_with_tax", "tax_amount", "inclusive_tax_amount", "exclusive_tax_amount", "status", "ach_number", "next_approver_choices", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method"]) -> 'CompanyPaymentMethodReadNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'Currency': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bill_payments"]) -> typing.Union[MetaOapg.properties.bill_payments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method_type"]) -> typing.Union[MetaOapg.properties.payment_method_type, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_date"]) -> typing.Union[MetaOapg.properties.payment_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["amount"]) -> typing.Union[MetaOapg.properties.amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["total_amount_with_tax"]) -> typing.Union[MetaOapg.properties.total_amount_with_tax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax_amount"]) -> typing.Union[MetaOapg.properties.tax_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inclusive_tax_amount"]) -> typing.Union[MetaOapg.properties.inclusive_tax_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["exclusive_tax_amount"]) -> typing.Union[MetaOapg.properties.exclusive_tax_amount, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union['PaymentStatusEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["ach_number"]) -> typing.Union[MetaOapg.properties.ach_number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_approver_choices"]) -> typing.Union[MetaOapg.properties.next_approver_choices, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["payment_method", "currency", "id", "bill_payments", "payment_method_type", "payment_date", "amount", "total_amount_with_tax", "tax_amount", "inclusive_tax_amount", "exclusive_tax_amount", "status", "ach_number", "next_approver_choices", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        currency: 'Currency',
        payment_method: 'CompanyPaymentMethodReadNullable',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        bill_payments: typing.Union[MetaOapg.properties.bill_payments, list, tuple, None, schemas.Unset] = schemas.unset,
        payment_method_type: typing.Union[MetaOapg.properties.payment_method_type, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_date: typing.Union[MetaOapg.properties.payment_date, None, str, date, schemas.Unset] = schemas.unset,
        amount: typing.Union[MetaOapg.properties.amount, str, schemas.Unset] = schemas.unset,
        total_amount_with_tax: typing.Union[MetaOapg.properties.total_amount_with_tax, str, schemas.Unset] = schemas.unset,
        tax_amount: typing.Union[MetaOapg.properties.tax_amount, str, schemas.Unset] = schemas.unset,
        inclusive_tax_amount: typing.Union[MetaOapg.properties.inclusive_tax_amount, str, schemas.Unset] = schemas.unset,
        exclusive_tax_amount: typing.Union[MetaOapg.properties.exclusive_tax_amount, str, schemas.Unset] = schemas.unset,
        status: typing.Union['PaymentStatusEnum', schemas.Unset] = schemas.unset,
        ach_number: typing.Union[MetaOapg.properties.ach_number, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        next_approver_choices: typing.Union[MetaOapg.properties.next_approver_choices, list, tuple, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PaymentListRead':
        return super().__new__(
            cls,
            *args,
            currency=currency,
            payment_method=payment_method,
            id=id,
            bill_payments=bill_payments,
            payment_method_type=payment_method_type,
            payment_date=payment_date,
            amount=amount,
            total_amount_with_tax=total_amount_with_tax,
            tax_amount=tax_amount,
            inclusive_tax_amount=inclusive_tax_amount,
            exclusive_tax_amount=exclusive_tax_amount,
            status=status,
            ach_number=ach_number,
            next_approver_choices=next_approver_choices,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.approver_read import ApproverRead
from procurify_python_sdk.model.bill_payment_docs import BillPaymentDocs
from procurify_python_sdk.model.company_payment_method_read_nullable import CompanyPaymentMethodReadNullable
from procurify_python_sdk.model.currency import Currency
from procurify_python_sdk.model.payment_status_enum import PaymentStatusEnum
