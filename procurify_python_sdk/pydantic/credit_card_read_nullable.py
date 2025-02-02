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

from procurify_python_sdk.pydantic.credit_card_type_enum import CreditCardTypeEnum
from procurify_python_sdk.pydantic.currency import Currency
from procurify_python_sdk.pydantic.session_create import SessionCreate
from procurify_python_sdk.pydantic.simple_user_summary import SimpleUserSummary
from procurify_python_sdk.pydantic.simple_vendor import SimpleVendor

class CreditCardReadNullable(BaseModel):
    vendor: SimpleVendor = Field(alias='vendor')

    currency: Currency = Field(alias='currency')

    assignees: typing.List[SimpleUserSummary] = Field(alias='assignees')

    id: typing.Optional[int] = Field(None, alias='id')

    name: typing.Optional[str] = Field(None, alias='name')

    number: typing.Optional[str] = Field(None, alias='number')

    type: typing.Optional[CreditCardTypeEnum] = Field(None, alias='type')

    balance: typing.Optional[typing.Optional[int]] = Field(None, alias='balance')

    last_reconciliation_date: typing.Optional[datetime] = Field(None, alias='last_reconciliation_date')

    last_reconciliation_balance: typing.Optional[typing.Union[int, float]] = Field(None, alias='last_reconciliation_balance')

    session: typing.Optional[SessionCreate] = Field(None, alias='session')

    gl_code: typing.Optional[str] = Field(None, alias='gl_code')

    last_statement_date: typing.Optional[datetime] = Field(None, alias='last_statement_date')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
