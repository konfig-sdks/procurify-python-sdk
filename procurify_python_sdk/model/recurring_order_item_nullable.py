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


class RecurringOrderItemNullable(
    schemas.DictBase,
    schemas.NoneBase,
    schemas.Schema,
    schemas.NoneFrozenDictMixin
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "duration",
            "duration_quantity",
            "recurring_price",
            "frequency",
        }
        
        class properties:
        
            @staticmethod
            def frequency() -> typing.Type['ZeroOneEnum']:
                return ZeroOneEnum
        
            @staticmethod
            def duration() -> typing.Type['ZeroOneEnum']:
                return ZeroOneEnum
            
            
            class duration_quantity(
                schemas.Int64Schema
            ):
            
            
                class MetaOapg:
                    format = 'int64'
                    inclusive_maximum = 4294967295
                    inclusive_minimum = 1
            
            
            class recurring_price(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,13}(?:\.\d{0,8})?$',
                    }]
            id = schemas.IntSchema
            start_date = schemas.DateSchema
            periods_count = schemas.IntSchema
            __annotations__ = {
                "frequency": frequency,
                "duration": duration,
                "duration_quantity": duration_quantity,
                "recurring_price": recurring_price,
                "id": id,
                "start_date": start_date,
                "periods_count": periods_count,
            }

    
    duration: 'ZeroOneEnum'
    duration_quantity: MetaOapg.properties.duration_quantity
    recurring_price: MetaOapg.properties.recurring_price
    frequency: 'ZeroOneEnum'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["frequency"]) -> 'ZeroOneEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration"]) -> 'ZeroOneEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["duration_quantity"]) -> MetaOapg.properties.duration_quantity: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["recurring_price"]) -> MetaOapg.properties.recurring_price: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["start_date"]) -> MetaOapg.properties.start_date: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["periods_count"]) -> MetaOapg.properties.periods_count: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["frequency", "duration", "duration_quantity", "recurring_price", "id", "start_date", "periods_count", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["frequency"]) -> 'ZeroOneEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration"]) -> 'ZeroOneEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["duration_quantity"]) -> MetaOapg.properties.duration_quantity: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["recurring_price"]) -> MetaOapg.properties.recurring_price: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["start_date"]) -> typing.Union[MetaOapg.properties.start_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["periods_count"]) -> typing.Union[MetaOapg.properties.periods_count, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["frequency", "duration", "duration_quantity", "recurring_price", "id", "start_date", "periods_count", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, None, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        start_date: typing.Union[MetaOapg.properties.start_date, str, date, schemas.Unset] = schemas.unset,
        periods_count: typing.Union[MetaOapg.properties.periods_count, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'RecurringOrderItemNullable':
        return super().__new__(
            cls,
            *args,
            id=id,
            start_date=start_date,
            periods_count=periods_count,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.zero_one_enum import ZeroOneEnum
