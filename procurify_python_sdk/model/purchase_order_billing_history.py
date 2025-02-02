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


class PurchaseOrderBillingHistory(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "number",
            "id",
            "items",
            "has_unbilled_unreceived_items",
        }
        
        class properties:
            id = schemas.IntSchema
            number = schemas.StrSchema
            has_unbilled_unreceived_items = schemas.BoolSchema
            
            
            class items(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PurchaseOrderBillingHistoryItem']:
                        return PurchaseOrderBillingHistoryItem
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PurchaseOrderBillingHistoryItem'], typing.List['PurchaseOrderBillingHistoryItem']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'items':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PurchaseOrderBillingHistoryItem':
                    return super().__getitem__(i)
            __annotations__ = {
                "id": id,
                "number": number,
                "has_unbilled_unreceived_items": has_unbilled_unreceived_items,
                "items": items,
            }
    
    number: MetaOapg.properties.number
    id: MetaOapg.properties.id
    items: MetaOapg.properties.items
    has_unbilled_unreceived_items: MetaOapg.properties.has_unbilled_unreceived_items
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["has_unbilled_unreceived_items"]) -> MetaOapg.properties.has_unbilled_unreceived_items: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["id", "number", "has_unbilled_unreceived_items", "items", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["has_unbilled_unreceived_items"]) -> MetaOapg.properties.has_unbilled_unreceived_items: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["items"]) -> MetaOapg.properties.items: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["id", "number", "has_unbilled_unreceived_items", "items", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        number: typing.Union[MetaOapg.properties.number, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, ],
        items: typing.Union[MetaOapg.properties.items, list, tuple, ],
        has_unbilled_unreceived_items: typing.Union[MetaOapg.properties.has_unbilled_unreceived_items, bool, ],
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'PurchaseOrderBillingHistory':
        return super().__new__(
            cls,
            *args,
            number=number,
            id=id,
            items=items,
            has_unbilled_unreceived_items=has_unbilled_unreceived_items,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.purchase_order_billing_history_item import PurchaseOrderBillingHistoryItem
