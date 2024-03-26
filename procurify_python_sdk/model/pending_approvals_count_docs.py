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


class PendingApprovalsCountDocs(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "bill",
            "payment",
            "expense",
            "travel",
            "order",
        }
        
        class properties:
            order = schemas.IntSchema
            expense = schemas.IntSchema
            travel = schemas.IntSchema
            bill = schemas.IntSchema
            payment = schemas.IntSchema
            __annotations__ = {
                "order": order,
                "expense": expense,
                "travel": travel,
                "bill": bill,
                "payment": payment,
            }
    
    bill: MetaOapg.properties.bill
    payment: MetaOapg.properties.payment
    expense: MetaOapg.properties.expense
    travel: MetaOapg.properties.travel
    order: MetaOapg.properties.order
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expense"]) -> MetaOapg.properties.expense: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["travel"]) -> MetaOapg.properties.travel: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["bill"]) -> MetaOapg.properties.bill: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment"]) -> MetaOapg.properties.payment: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["order", "expense", "travel", "bill", "payment", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expense"]) -> MetaOapg.properties.expense: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["travel"]) -> MetaOapg.properties.travel: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["bill"]) -> MetaOapg.properties.bill: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment"]) -> MetaOapg.properties.payment: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["order", "expense", "travel", "bill", "payment", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        bill: typing.Union[MetaOapg.properties.bill, decimal.Decimal, int, ],
        payment: typing.Union[MetaOapg.properties.payment, decimal.Decimal, int, ],
        expense: typing.Union[MetaOapg.properties.expense, decimal.Decimal, int, ],
        travel: typing.Union[MetaOapg.properties.travel, decimal.Decimal, int, ],
        order: typing.Union[MetaOapg.properties.order, decimal.Decimal, int, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PendingApprovalsCountDocs':
        return super().__new__(
            cls,
            *args,
            bill=bill,
            payment=payment,
            expense=expense,
            travel=travel,
            order=order,
            _configuration=_configuration,
            **kwargs,
        )
