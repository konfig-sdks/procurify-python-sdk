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


class PurchaseOrderUpdate(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "buyer_country",
            "buyer_address",
            "promise_date",
            "receiver_city",
            "receiver_postalCode",
            "buyer_addressLineOne",
            "buyer_name",
            "discount",
            "tax",
            "receiver_contact",
            "version",
            "buyer_city",
            "receiver_address",
            "receiver_name",
            "buyer_postalCode",
            "receiver_addressLineOne",
            "receiver_country",
            "buyer_contact",
            "order_items",
        }
        
        class properties:
            version = schemas.IntSchema
            
            
            class order_items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['OrderItemPurchaseEdit']:
                        return OrderItemPurchaseEdit
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['OrderItemPurchaseEdit'], typing.List['OrderItemPurchaseEdit']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'order_items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'OrderItemPurchaseEdit':
                    return super().__getitem__(i)
            
            
            class buyer_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class buyer_contact(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class buyer_addressLineOne(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 300
            
            
            class buyer_postalCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
            class buyer_city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class buyer_country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 80
            buyer_address = schemas.IntSchema
            
            
            class receiver_name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class receiver_contact(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
            class receiver_addressLineOne(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 300
            
            
            class receiver_postalCode(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
            class receiver_city(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class receiver_country(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 80
            receiver_address = schemas.IntSchema
            promise_date = schemas.DateTimeSchema
        
            @staticmethod
            def discount() -> typing.Type['PurchaseOrderUpdateDiscount']:
                return PurchaseOrderUpdateDiscount
        
            @staticmethod
            def tax() -> typing.Type['PurchaseOrderUpdateTax']:
                return PurchaseOrderUpdateTax
            
            
            class PO_Num(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 30
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PO_Num':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class buyer_state_province(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
            
            
            class comment(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'comment':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class receiver_state_province(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 40
            
            
            class freight(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,13}(?:\.\d{0,6})?$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'freight':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class other(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,13}(?:\.\d{0,6})?$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'other':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class disclaimer_description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'disclaimer_description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class disclaimer_text(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'disclaimer_text':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payment_term_ref(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_term_ref':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class shipping_term_ref(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shipping_term_ref':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payment_method_ref(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_method_ref':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class shipping_method_ref(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shipping_method_ref':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class creditcard(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'creditcard':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class expiry_date(
                schemas.DateTimeBase,
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'date-time'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, datetime, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'expiry_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class contract(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contract':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "version": version,
                "order_items": order_items,
                "buyer_name": buyer_name,
                "buyer_contact": buyer_contact,
                "buyer_addressLineOne": buyer_addressLineOne,
                "buyer_postalCode": buyer_postalCode,
                "buyer_city": buyer_city,
                "buyer_country": buyer_country,
                "buyer_address": buyer_address,
                "receiver_name": receiver_name,
                "receiver_contact": receiver_contact,
                "receiver_addressLineOne": receiver_addressLineOne,
                "receiver_postalCode": receiver_postalCode,
                "receiver_city": receiver_city,
                "receiver_country": receiver_country,
                "receiver_address": receiver_address,
                "promise_date": promise_date,
                "discount": discount,
                "tax": tax,
                "PO_Num": PO_Num,
                "buyer_state_province": buyer_state_province,
                "comment": comment,
                "receiver_state_province": receiver_state_province,
                "freight": freight,
                "other": other,
                "disclaimer_description": disclaimer_description,
                "disclaimer_text": disclaimer_text,
                "payment_term_ref": payment_term_ref,
                "shipping_term_ref": shipping_term_ref,
                "payment_method_ref": payment_method_ref,
                "shipping_method_ref": shipping_method_ref,
                "creditcard": creditcard,
                "expiry_date": expiry_date,
                "contract": contract,
            }
    
    buyer_country: MetaOapg.properties.buyer_country
    buyer_address: MetaOapg.properties.buyer_address
    promise_date: MetaOapg.properties.promise_date
    receiver_city: MetaOapg.properties.receiver_city
    receiver_postalCode: MetaOapg.properties.receiver_postalCode
    buyer_addressLineOne: MetaOapg.properties.buyer_addressLineOne
    buyer_name: MetaOapg.properties.buyer_name
    discount: 'PurchaseOrderUpdateDiscount'
    tax: 'PurchaseOrderUpdateTax'
    receiver_contact: MetaOapg.properties.receiver_contact
    version: MetaOapg.properties.version
    buyer_city: MetaOapg.properties.buyer_city
    receiver_address: MetaOapg.properties.receiver_address
    receiver_name: MetaOapg.properties.receiver_name
    buyer_postalCode: MetaOapg.properties.buyer_postalCode
    receiver_addressLineOne: MetaOapg.properties.receiver_addressLineOne
    receiver_country: MetaOapg.properties.receiver_country
    buyer_contact: MetaOapg.properties.buyer_contact
    order_items: MetaOapg.properties.order_items
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order_items"]) -> MetaOapg.properties.order_items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_name"]) -> MetaOapg.properties.buyer_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_contact"]) -> MetaOapg.properties.buyer_contact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_addressLineOne"]) -> MetaOapg.properties.buyer_addressLineOne: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_postalCode"]) -> MetaOapg.properties.buyer_postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_city"]) -> MetaOapg.properties.buyer_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_country"]) -> MetaOapg.properties.buyer_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_name"]) -> MetaOapg.properties.receiver_name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_contact"]) -> MetaOapg.properties.receiver_contact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_addressLineOne"]) -> MetaOapg.properties.receiver_addressLineOne: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_postalCode"]) -> MetaOapg.properties.receiver_postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_city"]) -> MetaOapg.properties.receiver_city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_country"]) -> MetaOapg.properties.receiver_country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_address"]) -> MetaOapg.properties.receiver_address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["promise_date"]) -> MetaOapg.properties.promise_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["discount"]) -> 'PurchaseOrderUpdateDiscount': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax"]) -> 'PurchaseOrderUpdateTax': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PO_Num"]) -> MetaOapg.properties.PO_Num: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["buyer_state_province"]) -> MetaOapg.properties.buyer_state_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comment"]) -> MetaOapg.properties.comment: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["receiver_state_province"]) -> MetaOapg.properties.receiver_state_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["freight"]) -> MetaOapg.properties.freight: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["other"]) -> MetaOapg.properties.other: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disclaimer_description"]) -> MetaOapg.properties.disclaimer_description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["disclaimer_text"]) -> MetaOapg.properties.disclaimer_text: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_term_ref"]) -> MetaOapg.properties.payment_term_ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_term_ref"]) -> MetaOapg.properties.shipping_term_ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method_ref"]) -> MetaOapg.properties.payment_method_ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_method_ref"]) -> MetaOapg.properties.shipping_method_ref: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditcard"]) -> MetaOapg.properties.creditcard: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expiry_date"]) -> MetaOapg.properties.expiry_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contract"]) -> MetaOapg.properties.contract: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["version", "order_items", "buyer_name", "buyer_contact", "buyer_addressLineOne", "buyer_postalCode", "buyer_city", "buyer_country", "buyer_address", "receiver_name", "receiver_contact", "receiver_addressLineOne", "receiver_postalCode", "receiver_city", "receiver_country", "receiver_address", "promise_date", "discount", "tax", "PO_Num", "buyer_state_province", "comment", "receiver_state_province", "freight", "other", "disclaimer_description", "disclaimer_text", "payment_term_ref", "shipping_term_ref", "payment_method_ref", "shipping_method_ref", "creditcard", "expiry_date", "contract", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["version"]) -> MetaOapg.properties.version: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order_items"]) -> MetaOapg.properties.order_items: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_name"]) -> MetaOapg.properties.buyer_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_contact"]) -> MetaOapg.properties.buyer_contact: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_addressLineOne"]) -> MetaOapg.properties.buyer_addressLineOne: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_postalCode"]) -> MetaOapg.properties.buyer_postalCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_city"]) -> MetaOapg.properties.buyer_city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_country"]) -> MetaOapg.properties.buyer_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_address"]) -> MetaOapg.properties.buyer_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_name"]) -> MetaOapg.properties.receiver_name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_contact"]) -> MetaOapg.properties.receiver_contact: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_addressLineOne"]) -> MetaOapg.properties.receiver_addressLineOne: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_postalCode"]) -> MetaOapg.properties.receiver_postalCode: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_city"]) -> MetaOapg.properties.receiver_city: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_country"]) -> MetaOapg.properties.receiver_country: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_address"]) -> MetaOapg.properties.receiver_address: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["promise_date"]) -> MetaOapg.properties.promise_date: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["discount"]) -> 'PurchaseOrderUpdateDiscount': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax"]) -> 'PurchaseOrderUpdateTax': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PO_Num"]) -> typing.Union[MetaOapg.properties.PO_Num, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["buyer_state_province"]) -> typing.Union[MetaOapg.properties.buyer_state_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comment"]) -> typing.Union[MetaOapg.properties.comment, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["receiver_state_province"]) -> typing.Union[MetaOapg.properties.receiver_state_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["freight"]) -> typing.Union[MetaOapg.properties.freight, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["other"]) -> typing.Union[MetaOapg.properties.other, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disclaimer_description"]) -> typing.Union[MetaOapg.properties.disclaimer_description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["disclaimer_text"]) -> typing.Union[MetaOapg.properties.disclaimer_text, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_term_ref"]) -> typing.Union[MetaOapg.properties.payment_term_ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_term_ref"]) -> typing.Union[MetaOapg.properties.shipping_term_ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method_ref"]) -> typing.Union[MetaOapg.properties.payment_method_ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_method_ref"]) -> typing.Union[MetaOapg.properties.shipping_method_ref, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditcard"]) -> typing.Union[MetaOapg.properties.creditcard, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expiry_date"]) -> typing.Union[MetaOapg.properties.expiry_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contract"]) -> typing.Union[MetaOapg.properties.contract, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["version", "order_items", "buyer_name", "buyer_contact", "buyer_addressLineOne", "buyer_postalCode", "buyer_city", "buyer_country", "buyer_address", "receiver_name", "receiver_contact", "receiver_addressLineOne", "receiver_postalCode", "receiver_city", "receiver_country", "receiver_address", "promise_date", "discount", "tax", "PO_Num", "buyer_state_province", "comment", "receiver_state_province", "freight", "other", "disclaimer_description", "disclaimer_text", "payment_term_ref", "shipping_term_ref", "payment_method_ref", "shipping_method_ref", "creditcard", "expiry_date", "contract", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        buyer_country: typing.Union[MetaOapg.properties.buyer_country, str, ],
        buyer_address: typing.Union[MetaOapg.properties.buyer_address, decimal.Decimal, int, ],
        promise_date: typing.Union[MetaOapg.properties.promise_date, str, datetime, ],
        receiver_city: typing.Union[MetaOapg.properties.receiver_city, str, ],
        receiver_postalCode: typing.Union[MetaOapg.properties.receiver_postalCode, str, ],
        buyer_addressLineOne: typing.Union[MetaOapg.properties.buyer_addressLineOne, str, ],
        buyer_name: typing.Union[MetaOapg.properties.buyer_name, str, ],
        discount: 'PurchaseOrderUpdateDiscount',
        tax: 'PurchaseOrderUpdateTax',
        receiver_contact: typing.Union[MetaOapg.properties.receiver_contact, str, ],
        version: typing.Union[MetaOapg.properties.version, decimal.Decimal, int, ],
        buyer_city: typing.Union[MetaOapg.properties.buyer_city, str, ],
        receiver_address: typing.Union[MetaOapg.properties.receiver_address, decimal.Decimal, int, ],
        receiver_name: typing.Union[MetaOapg.properties.receiver_name, str, ],
        buyer_postalCode: typing.Union[MetaOapg.properties.buyer_postalCode, str, ],
        receiver_addressLineOne: typing.Union[MetaOapg.properties.receiver_addressLineOne, str, ],
        receiver_country: typing.Union[MetaOapg.properties.receiver_country, str, ],
        buyer_contact: typing.Union[MetaOapg.properties.buyer_contact, str, ],
        order_items: typing.Union[MetaOapg.properties.order_items, list, tuple, ],
        PO_Num: typing.Union[MetaOapg.properties.PO_Num, None, str, schemas.Unset] = schemas.unset,
        buyer_state_province: typing.Union[MetaOapg.properties.buyer_state_province, str, schemas.Unset] = schemas.unset,
        comment: typing.Union[MetaOapg.properties.comment, None, str, schemas.Unset] = schemas.unset,
        receiver_state_province: typing.Union[MetaOapg.properties.receiver_state_province, str, schemas.Unset] = schemas.unset,
        freight: typing.Union[MetaOapg.properties.freight, None, str, schemas.Unset] = schemas.unset,
        other: typing.Union[MetaOapg.properties.other, None, str, schemas.Unset] = schemas.unset,
        disclaimer_description: typing.Union[MetaOapg.properties.disclaimer_description, None, str, schemas.Unset] = schemas.unset,
        disclaimer_text: typing.Union[MetaOapg.properties.disclaimer_text, None, str, schemas.Unset] = schemas.unset,
        payment_term_ref: typing.Union[MetaOapg.properties.payment_term_ref, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        shipping_term_ref: typing.Union[MetaOapg.properties.shipping_term_ref, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_method_ref: typing.Union[MetaOapg.properties.payment_method_ref, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        shipping_method_ref: typing.Union[MetaOapg.properties.shipping_method_ref, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creditcard: typing.Union[MetaOapg.properties.creditcard, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        expiry_date: typing.Union[MetaOapg.properties.expiry_date, None, str, datetime, schemas.Unset] = schemas.unset,
        contract: typing.Union[MetaOapg.properties.contract, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PurchaseOrderUpdate':
        return super().__new__(
            cls,
            *args,
            buyer_country=buyer_country,
            buyer_address=buyer_address,
            promise_date=promise_date,
            receiver_city=receiver_city,
            receiver_postalCode=receiver_postalCode,
            buyer_addressLineOne=buyer_addressLineOne,
            buyer_name=buyer_name,
            discount=discount,
            tax=tax,
            receiver_contact=receiver_contact,
            version=version,
            buyer_city=buyer_city,
            receiver_address=receiver_address,
            receiver_name=receiver_name,
            buyer_postalCode=buyer_postalCode,
            receiver_addressLineOne=receiver_addressLineOne,
            receiver_country=receiver_country,
            buyer_contact=buyer_contact,
            order_items=order_items,
            PO_Num=PO_Num,
            buyer_state_province=buyer_state_province,
            comment=comment,
            receiver_state_province=receiver_state_province,
            freight=freight,
            other=other,
            disclaimer_description=disclaimer_description,
            disclaimer_text=disclaimer_text,
            payment_term_ref=payment_term_ref,
            shipping_term_ref=shipping_term_ref,
            payment_method_ref=payment_method_ref,
            shipping_method_ref=shipping_method_ref,
            creditcard=creditcard,
            expiry_date=expiry_date,
            contract=contract,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.order_item_purchase_edit import OrderItemPurchaseEdit
from procurify_python_sdk.model.purchase_order_update_discount import PurchaseOrderUpdateDiscount
from procurify_python_sdk.model.purchase_order_update_tax import PurchaseOrderUpdateTax
