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

from procurify_python_sdk.pydantic.address_docs_nullable import AddressDocsNullable
from procurify_python_sdk.pydantic.branch import Branch
from procurify_python_sdk.pydantic.currency_summary import CurrencySummary
from procurify_python_sdk.pydantic.department_summary import DepartmentSummary
from procurify_python_sdk.pydantic.master_logger import MasterLogger
from procurify_python_sdk.pydantic.order_status_enum import OrderStatusEnum
from procurify_python_sdk.pydantic.punch_out_read_docs_nullable import PunchOutReadDocsNullable
from procurify_python_sdk.pydantic.user_summary import UserSummary

class OrderRead(BaseModel):
    uuid: str = Field(alias='uuid')

    branch: Branch = Field(alias='branch')

    user: UserSummary = Field(alias='user')

    department: DepartmentSummary = Field(alias='department')

    logs: typing.List[MasterLogger] = Field(alias='logs')

    date_required: datetime = Field(alias='dateRequired')

    next_approver: UserSummary = Field(alias='next_approver')

    description: typing.Optional[typing.Optional[str]] = Field(None, alias='description')

    num: typing.Optional[int] = Field(None, alias='num')

    currency: typing.Optional[CurrencySummary] = Field(None, alias='currency')

    total_cost_in_base_currency: typing.Optional[typing.Union[int, float]] = Field(None, alias='total_cost_in_base_currency')

    item_count: typing.Optional[int] = Field(None, alias='item_count')

    ip_address: typing.Optional[typing.Optional[str]] = Field(None, alias='ip_address')

    date: typing.Optional[datetime] = Field(None, alias='date')

    date_modified: typing.Optional[datetime] = Field(None, alias='dateModified')

    line_count: typing.Optional[typing.Optional[int]] = Field(None, alias='lineCount')

    purchased_count: typing.Optional[int] = Field(None, alias='purchasedCount')

    total_price: typing.Optional[typing.Optional[str]] = Field(None, alias='totalPrice')

    status: typing.Optional[OrderStatusEnum] = Field(None, alias='status')

    approval_delegatee: typing.Optional[typing.Optional[int]] = Field(None, alias='approval_delegatee')

    punchout_group: typing.Optional[PunchOutReadDocsNullable] = Field(None, alias='punchout_group')

    punchout_shipping_address: typing.Optional[AddressDocsNullable] = Field(None, alias='punchout_shipping_address')

    punchout_items_rejected: typing.Optional[bool] = Field(None, alias='punchout_items_rejected')

    punchout_supplier_name: typing.Optional[typing.Optional[str]] = Field(None, alias='punchout_supplier_name')

    punchout_supplier_icon: typing.Optional[typing.Optional[str]] = Field(None, alias='punchout_supplier_icon')

    punchout_vendor_reference: typing.Optional[typing.Optional[int]] = Field(None, alias='punchout_vendor_reference')

    has_blanket_order_items: typing.Optional[bool] = Field(None, alias='has_blanket_order_items')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
