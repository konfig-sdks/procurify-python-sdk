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


class LocationCreateUpsertRequest(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "primary_billing_address",
            "primary_shipping_address",
            "name",
            "currency",
            "phoneOne",
            "shipping_addresses",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 150
                    min_length = 1
            
            
            class currency(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    min_length = 1
            
            
            class phoneOne(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 20
                    min_length = 1
        
            @staticmethod
            def primary_billing_address() -> typing.Type['AddressRequest']:
                return AddressRequest
        
            @staticmethod
            def primary_shipping_address() -> typing.Type['AddressRequest']:
                return AddressRequest
            
            
            class shipping_addresses(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['AddressRequest']:
                        return AddressRequest
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['AddressRequest'], typing.List['AddressRequest']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'shipping_addresses':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'AddressRequest':
                    return super().__getitem__(i)
            
            
            class url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class logo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'logo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class fax(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fax':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class email(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'email'
                    max_length = 254
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'email':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def language() -> typing.Type['LanguageEnum']:
                return LanguageEnum
            
            
            class locationTimezone(
                schemas.ComposedBase,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            LocationTimezoneEnum,
                            BlankEnum,
                            NullEnum,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'locationTimezone':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            active = schemas.BoolSchema
            
            
            class external_id(
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
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "name": name,
                "currency": currency,
                "phoneOne": phoneOne,
                "primary_billing_address": primary_billing_address,
                "primary_shipping_address": primary_shipping_address,
                "shipping_addresses": shipping_addresses,
                "url": url,
                "logo": logo,
                "fax": fax,
                "email": email,
                "language": language,
                "locationTimezone": locationTimezone,
                "active": active,
                "external_id": external_id,
            }
    
    primary_billing_address: 'AddressRequest'
    primary_shipping_address: 'AddressRequest'
    name: MetaOapg.properties.name
    currency: MetaOapg.properties.currency
    phoneOne: MetaOapg.properties.phoneOne
    shipping_addresses: MetaOapg.properties.shipping_addresses
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneOne"]) -> MetaOapg.properties.phoneOne: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_billing_address"]) -> 'AddressRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["primary_shipping_address"]) -> 'AddressRequest': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_addresses"]) -> MetaOapg.properties.shipping_addresses: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["logo"]) -> MetaOapg.properties.logo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fax"]) -> MetaOapg.properties.fax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["language"]) -> 'LanguageEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["locationTimezone"]) -> MetaOapg.properties.locationTimezone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "currency", "phoneOne", "primary_billing_address", "primary_shipping_address", "shipping_addresses", "url", "logo", "fax", "email", "language", "locationTimezone", "active", "external_id", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneOne"]) -> MetaOapg.properties.phoneOne: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_billing_address"]) -> 'AddressRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["primary_shipping_address"]) -> 'AddressRequest': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_addresses"]) -> MetaOapg.properties.shipping_addresses: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["logo"]) -> typing.Union[MetaOapg.properties.logo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fax"]) -> typing.Union[MetaOapg.properties.fax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> typing.Union[MetaOapg.properties.email, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["language"]) -> typing.Union['LanguageEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["locationTimezone"]) -> typing.Union[MetaOapg.properties.locationTimezone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "currency", "phoneOne", "primary_billing_address", "primary_shipping_address", "shipping_addresses", "url", "logo", "fax", "email", "language", "locationTimezone", "active", "external_id", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        primary_billing_address: 'AddressRequest',
        primary_shipping_address: 'AddressRequest',
        name: typing.Union[MetaOapg.properties.name, str, ],
        currency: typing.Union[MetaOapg.properties.currency, str, ],
        phoneOne: typing.Union[MetaOapg.properties.phoneOne, str, ],
        shipping_addresses: typing.Union[MetaOapg.properties.shipping_addresses, list, tuple, ],
        url: typing.Union[MetaOapg.properties.url, None, str, schemas.Unset] = schemas.unset,
        logo: typing.Union[MetaOapg.properties.logo, None, str, schemas.Unset] = schemas.unset,
        fax: typing.Union[MetaOapg.properties.fax, None, str, schemas.Unset] = schemas.unset,
        email: typing.Union[MetaOapg.properties.email, None, str, schemas.Unset] = schemas.unset,
        language: typing.Union['LanguageEnum', schemas.Unset] = schemas.unset,
        locationTimezone: typing.Union[MetaOapg.properties.locationTimezone, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'LocationCreateUpsertRequest':
        return super().__new__(
            cls,
            *args,
            primary_billing_address=primary_billing_address,
            primary_shipping_address=primary_shipping_address,
            name=name,
            currency=currency,
            phoneOne=phoneOne,
            shipping_addresses=shipping_addresses,
            url=url,
            logo=logo,
            fax=fax,
            email=email,
            language=language,
            locationTimezone=locationTimezone,
            active=active,
            external_id=external_id,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.address_request import AddressRequest
from procurify_python_sdk.model.blank_enum import BlankEnum
from procurify_python_sdk.model.language_enum import LanguageEnum
from procurify_python_sdk.model.location_timezone_enum import LocationTimezoneEnum
from procurify_python_sdk.model.null_enum import NullEnum
