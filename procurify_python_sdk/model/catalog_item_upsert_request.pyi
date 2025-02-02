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


class CatalogItemUpsertRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "custom_fields",
            "name",
            "currency",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            currency = schemas.IntSchema
        
            @staticmethod
            def custom_fields() -> typing.Type['CatalogItemUpsertRequestCustomFields']:
                return CatalogItemUpsertRequestCustomFields
            
            
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
                pass
            
            
            class pref_vendor(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'pref_vendor':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class account_code(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'account_code':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class internalSKU(
                schemas.StrSchema
            ):
                pass
            
            
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
                pass
            rfo_lock = schemas.BoolSchema
        
            @staticmethod
            def departments() -> typing.Type['CatalogItemUpsertRequestDepartments']:
                return CatalogItemUpsertRequestDepartments
            __annotations__ = {
                "name": name,
                "currency": currency,
                "custom_fields": custom_fields,
                "description": description,
                "id": id,
                "image": image,
                "unitType": unitType,
                "pref_vendor": pref_vendor,
                "account_code": account_code,
                "internalSKU": internalSKU,
                "product_url": product_url,
                "price": price,
                "rfo_lock": rfo_lock,
                "departments": departments,
            }
    
    custom_fields: 'CatalogItemUpsertRequestCustomFields'
    name: MetaOapg.properties.name
    currency: MetaOapg.properties.currency
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["custom_fields"]) -> 'CatalogItemUpsertRequestCustomFields': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["description"]) -> MetaOapg.properties.description: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["image"]) -> MetaOapg.properties.image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["unitType"]) -> MetaOapg.properties.unitType: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["pref_vendor"]) -> MetaOapg.properties.pref_vendor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_code"]) -> MetaOapg.properties.account_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["internalSKU"]) -> MetaOapg.properties.internalSKU: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["product_url"]) -> MetaOapg.properties.product_url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["price"]) -> MetaOapg.properties.price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["rfo_lock"]) -> MetaOapg.properties.rfo_lock: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["departments"]) -> 'CatalogItemUpsertRequestDepartments': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "currency", "custom_fields", "description", "id", "image", "unitType", "pref_vendor", "account_code", "internalSKU", "product_url", "price", "rfo_lock", "departments", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["custom_fields"]) -> 'CatalogItemUpsertRequestCustomFields': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["description"]) -> typing.Union[MetaOapg.properties.description, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["image"]) -> typing.Union[MetaOapg.properties.image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["unitType"]) -> typing.Union[MetaOapg.properties.unitType, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["pref_vendor"]) -> typing.Union[MetaOapg.properties.pref_vendor, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_code"]) -> typing.Union[MetaOapg.properties.account_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["internalSKU"]) -> typing.Union[MetaOapg.properties.internalSKU, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["product_url"]) -> typing.Union[MetaOapg.properties.product_url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["price"]) -> typing.Union[MetaOapg.properties.price, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["rfo_lock"]) -> typing.Union[MetaOapg.properties.rfo_lock, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["departments"]) -> typing.Union['CatalogItemUpsertRequestDepartments', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "currency", "custom_fields", "description", "id", "image", "unitType", "pref_vendor", "account_code", "internalSKU", "product_url", "price", "rfo_lock", "departments", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        custom_fields: 'CatalogItemUpsertRequestCustomFields',
        name: typing.Union[MetaOapg.properties.name, str, ],
        currency: typing.Union[MetaOapg.properties.currency, decimal.Decimal, int, ],
        description: typing.Union[MetaOapg.properties.description, None, str, schemas.Unset] = schemas.unset,
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        image: typing.Union[MetaOapg.properties.image, str, schemas.Unset] = schemas.unset,
        unitType: typing.Union[MetaOapg.properties.unitType, str, schemas.Unset] = schemas.unset,
        pref_vendor: typing.Union[MetaOapg.properties.pref_vendor, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        account_code: typing.Union[MetaOapg.properties.account_code, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        internalSKU: typing.Union[MetaOapg.properties.internalSKU, str, schemas.Unset] = schemas.unset,
        product_url: typing.Union[MetaOapg.properties.product_url, None, str, schemas.Unset] = schemas.unset,
        price: typing.Union[MetaOapg.properties.price, str, schemas.Unset] = schemas.unset,
        rfo_lock: typing.Union[MetaOapg.properties.rfo_lock, bool, schemas.Unset] = schemas.unset,
        departments: typing.Union['CatalogItemUpsertRequestDepartments', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CatalogItemUpsertRequest':
        return super().__new__(
            cls,
            *args,
            custom_fields=custom_fields,
            name=name,
            currency=currency,
            description=description,
            id=id,
            image=image,
            unitType=unitType,
            pref_vendor=pref_vendor,
            account_code=account_code,
            internalSKU=internalSKU,
            product_url=product_url,
            price=price,
            rfo_lock=rfo_lock,
            departments=departments,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.catalog_item_upsert_request_custom_fields import CatalogItemUpsertRequestCustomFields
from procurify_python_sdk.model.catalog_item_upsert_request_departments import CatalogItemUpsertRequestDepartments
