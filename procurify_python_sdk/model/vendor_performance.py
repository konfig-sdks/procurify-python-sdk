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


class VendorPerformance(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        
        class properties:
            overall_score = schemas.Float32Schema
            
            
            class average_delivery_time(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,3}(?:\.\d{0,3})?$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'average_delivery_time':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def breakdown() -> typing.Type['VendorBreakdownDocs']:
                return VendorBreakdownDocs
            __annotations__ = {
                "overall_score": overall_score,
                "average_delivery_time": average_delivery_time,
                "breakdown": breakdown,
            }
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overall_score"]) -> MetaOapg.properties.overall_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["average_delivery_time"]) -> MetaOapg.properties.average_delivery_time: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["breakdown"]) -> 'VendorBreakdownDocs': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["overall_score", "average_delivery_time", "breakdown", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overall_score"]) -> typing.Union[MetaOapg.properties.overall_score, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["average_delivery_time"]) -> typing.Union[MetaOapg.properties.average_delivery_time, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["breakdown"]) -> typing.Union['VendorBreakdownDocs', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["overall_score", "average_delivery_time", "breakdown", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        overall_score: typing.Union[MetaOapg.properties.overall_score, decimal.Decimal, int, float, schemas.Unset] = schemas.unset,
        average_delivery_time: typing.Union[MetaOapg.properties.average_delivery_time, None, str, schemas.Unset] = schemas.unset,
        breakdown: typing.Union['VendorBreakdownDocs', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'VendorPerformance':
        return super().__new__(
            cls,
            *args,
            overall_score=overall_score,
            average_delivery_time=average_delivery_time,
            breakdown=breakdown,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.vendor_breakdown_docs import VendorBreakdownDocs
