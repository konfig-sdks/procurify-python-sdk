# coding: utf-8

"""
    Procurify API Documentation

     # Disclaimer  - Procurify’s API is evolving and is subject to change at any time. Additionally, aspects of the API are undocumented, including certain methods, events, and properties. Given that both documented and undocumented aspects of the Procurify API may change at any time, the client relies on the API at their own risk. - Client (and/or client’s representative) is responsible for building, testing, and maintaining any API connection between Procurify and any other tool.  Procurify’s responsibility strictly involves providing support on clarifications in regards to the issued API document. - Procurify’s API is offered on an “as is” and “as available” basis, without warranties of any kind. By accepting this agreement, you agree that you have read the current API documentation, and accept the API functionality in its current state including current limitations. For questions and clarification around the documentation, please contact support@procurify.com. - In accordance with Section 2.(b) of our Subscription Services Agreement, Procurify reserves the right to deny access to our API at any time. If your API requests are too large and time out, contact us immediately to avoid possible suspension of access. - You may not attempt to reverse engineer or otherwise derive source code, trade secrets, or know-how in the Procurify API or portion thereof. You may not use the Procurify API to replicate or compete with core products or services offered by Procurify. 

    Generated by: https://konfigthis.com
"""

from datetime import datetime, date
import typing
from enum import Enum
from typing_extensions import TypedDict, Literal, TYPE_CHECKING
from pydantic import BaseModel, Field, RootModel, ConfigDict

from procurify_python_sdk.pydantic.order_item_purchase_edit import OrderItemPurchaseEdit
from procurify_python_sdk.pydantic.purchase_order_update_discount import PurchaseOrderUpdateDiscount
from procurify_python_sdk.pydantic.purchase_order_update_tax import PurchaseOrderUpdateTax

class PurchaseOrderUpdate(BaseModel):
    version: int = Field(alias='version')

    order_items: typing.List[OrderItemPurchaseEdit] = Field(alias='order_items')

    buyer_name: str = Field(alias='buyer_name')

    buyer_contact: str = Field(alias='buyer_contact')

    buyer_address_line_one: str = Field(alias='buyer_addressLineOne')

    buyer_postal_code: str = Field(alias='buyer_postalCode')

    buyer_city: str = Field(alias='buyer_city')

    buyer_country: str = Field(alias='buyer_country')

    buyer_address: int = Field(alias='buyer_address')

    receiver_name: str = Field(alias='receiver_name')

    receiver_contact: str = Field(alias='receiver_contact')

    receiver_address_line_one: str = Field(alias='receiver_addressLineOne')

    receiver_postal_code: str = Field(alias='receiver_postalCode')

    receiver_city: str = Field(alias='receiver_city')

    receiver_country: str = Field(alias='receiver_country')

    receiver_address: int = Field(alias='receiver_address')

    promise_date: datetime = Field(alias='promise_date')

    discount: PurchaseOrderUpdateDiscount = Field(alias='discount')

    tax: PurchaseOrderUpdateTax = Field(alias='tax')

    p_o__num: typing.Optional[typing.Optional[str]] = Field(None, alias='PO_Num')

    buyer_state_province: typing.Optional[str] = Field(None, alias='buyer_state_province')

    comment: typing.Optional[typing.Optional[str]] = Field(None, alias='comment')

    receiver_state_province: typing.Optional[str] = Field(None, alias='receiver_state_province')

    freight: typing.Optional[typing.Optional[str]] = Field(None, alias='freight')

    other: typing.Optional[typing.Optional[str]] = Field(None, alias='other')

    disclaimer_description: typing.Optional[typing.Optional[str]] = Field(None, alias='disclaimer_description')

    disclaimer_text: typing.Optional[typing.Optional[str]] = Field(None, alias='disclaimer_text')

    payment_term_ref: typing.Optional[typing.Optional[int]] = Field(None, alias='payment_term_ref')

    shipping_term_ref: typing.Optional[typing.Optional[int]] = Field(None, alias='shipping_term_ref')

    payment_method_ref: typing.Optional[typing.Optional[int]] = Field(None, alias='payment_method_ref')

    shipping_method_ref: typing.Optional[typing.Optional[int]] = Field(None, alias='shipping_method_ref')

    creditcard: typing.Optional[typing.Optional[int]] = Field(None, alias='creditcard')

    expiry_date: typing.Optional[typing.Optional[datetime]] = Field(None, alias='expiry_date')

    contract: typing.Optional[typing.Optional[int]] = Field(None, alias='contract')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
