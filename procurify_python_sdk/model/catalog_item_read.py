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


class CatalogItemRead(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "account_code",
            "currency",
            "pref_vendor",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 255
        
            @staticmethod
            def pref_vendor() -> typing.Type['VendorRead']:
                return VendorRead
        
            @staticmethod
            def account_code() -> typing.Type['AccountCodeRead']:
                return AccountCodeRead
        
            @staticmethod
            def currency() -> typing.Type['CurrencySummary']:
                return CurrencySummary
            
            
            class description(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'description':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            id = schemas.IntSchema
            image = schemas.StrSchema
            
            
            class unitType(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 30
            
            
            class internalSKU(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
            class product_url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'product_url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class price(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,13}(?:\.\d{0,8})?$',
                    }]
            rfo_lock = schemas.BoolSchema
        
            @staticmethod
            def departments() -> typing.Type['CatalogItemReadDepartments']:
                return CatalogItemReadDepartments
            
            
            class custom_fields(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CustomFieldValueRead']:
                        return CustomFieldValueRead
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CustomFieldValueRead'], typing.List['CustomFieldValueRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'custom_fields':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CustomFieldValueRead':
                    return super().__getitem__(i)
            
            
            class requested_count(
                schemas.IntSchema
            ):
            
            
                class MetaOapg:
                    inclusive_maximum = 2147483647
                    inclusive_minimum = -2147483648
            
            
            class last_requested_date(
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
                ) -> 'last_requested_date':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def selected_account() -> typing.Type['CatalogItemReadSelectedAccount']:
                return CatalogItemReadSelectedAccount
            __annotations__ = {
                "name": name,
                "pref_vendor": pref_vendor,
                "account_code": account_code,
                "currency": currency,
                "description": description,
                "id": id,
                "image": image,
                "unitType": unitType,
                "internalSKU": internalSKU,
                "product_url": product_url,
                "price": price,
                "rfo_lock": rfo_lock,
                "departments": departments,
                "custom_fields": custom_fields,
                "requested_count": requested_count,
                "last_requested_date": last_requested_date,
                "selected_account": selected_account,
            }
    
    name: MetaOapg.properties.name
    account_code: 'AccountCodeRead'
    currency: 'CurrencySummary'
    pref_vendor: 'VendorRead'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pref_vendor"]) -> 'VendorRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_code"]) -> 'AccountCodeRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> 'CurrencySummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unitType"]) -> MetaOapg.properties.unitType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalSKU"]) -> MetaOapg.properties.internalSKU: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_url"]) -> MetaOapg.properties.product_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rfo_lock"]) -> MetaOapg.properties.rfo_lock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departments"]) -> 'CatalogItemReadDepartments': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> MetaOapg.properties.custom_fields: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["requested_count"]) -> MetaOapg.properties.requested_count: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_requested_date"]) -> MetaOapg.properties.last_requested_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["selected_account"]) -> 'CatalogItemReadSelectedAccount': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "pref_vendor", "account_code", "currency", "description", "id", "image", "unitType", "internalSKU", "product_url", "price", "rfo_lock", "departments", "custom_fields", "requested_count", "last_requested_date", "selected_account", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pref_vendor"]) -> 'VendorRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_code"]) -> 'AccountCodeRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> 'CurrencySummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unitType"]) -> typing.Union[MetaOapg.properties.unitType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalSKU"]) -> typing.Union[MetaOapg.properties.internalSKU, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_url"]) -> typing.Union[MetaOapg.properties.product_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rfo_lock"]) -> typing.Union[MetaOapg.properties.rfo_lock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departments"]) -> typing.Union['CatalogItemReadDepartments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> typing.Union[MetaOapg.properties.custom_fields, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["requested_count"]) -> typing.Union[MetaOapg.properties.requested_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_requested_date"]) -> typing.Union[MetaOapg.properties.last_requested_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["selected_account"]) -> typing.Union['CatalogItemReadSelectedAccount', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "pref_vendor", "account_code", "currency", "description", "id", "image", "unitType", "internalSKU", "product_url", "price", "rfo_lock", "departments", "custom_fields", "requested_count", "last_requested_date", "selected_account", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        account_code: 'AccountCodeRead',
        currency: 'CurrencySummary',
        pref_vendor: 'VendorRead',
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        unitType: typing.Union[MetaOapg.properties.unitType, str, schemas.Unset] = schemas.unset,
        internalSKU: typing.Union[MetaOapg.properties.internalSKU, str, schemas.Unset] = schemas.unset,
        product_url: typing.Union[MetaOapg.properties.product_url, None, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, str, schemas.Unset] = schemas.unset,
        rfo_lock: typing.Union[MetaOapg.properties.rfo_lock, bool, schemas.Unset] = schemas.unset,
        departments: typing.Union['CatalogItemReadDepartments', schemas.Unset] = schemas.unset,
        custom_fields: typing.Union[MetaOapg.properties.custom_fields, list, tuple, schemas.Unset] = schemas.unset,
        requested_count: typing.Union[MetaOapg.properties.requested_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        last_requested_date: typing.Union[MetaOapg.properties.last_requested_date, None, str, datetime, schemas.Unset] = schemas.unset,
        selected_account: typing.Union['CatalogItemReadSelectedAccount', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CatalogItemRead':
        return super().__new__(
            cls,
            *args,
            name=name,
            account_code=account_code,
            currency=currency,
            pref_vendor=pref_vendor,
            description=description,
            id=id,
            image=image,
            unitType=unitType,
            internalSKU=internalSKU,
            product_url=product_url,
            price=price,
            rfo_lock=rfo_lock,
            departments=departments,
            custom_fields=custom_fields,
            requested_count=requested_count,
            last_requested_date=last_requested_date,
            selected_account=selected_account,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.account_code_read import AccountCodeRead
from procurify_python_sdk.model.catalog_item_read_departments import CatalogItemReadDepartments
from procurify_python_sdk.model.catalog_item_read_selected_account import CatalogItemReadSelectedAccount
from procurify_python_sdk.model.currency_summary import CurrencySummary
from procurify_python_sdk.model.custom_field_value_read import CustomFieldValueRead
from procurify_python_sdk.model.vendor_read import VendorRead
