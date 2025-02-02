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

from procurify_python_sdk.pydantic.account import Account
from procurify_python_sdk.pydantic.currency_summary import CurrencySummary
from procurify_python_sdk.pydantic.expense_read_expense_type_fields import ExpenseReadExpenseTypeFields
from procurify_python_sdk.pydantic.expense_type_enum import ExpenseTypeEnum
from procurify_python_sdk.pydantic.payment_method_type_enum import PaymentMethodTypeEnum
from procurify_python_sdk.pydantic.simple_expense_report import SimpleExpenseReport
from procurify_python_sdk.pydantic.simple_user_summary import SimpleUserSummary

class ExpenseRead(BaseModel):
    account: Account = Field(alias='account')

    local_currency: CurrencySummary = Field(alias='localCurrency')

    expense_type_fields: ExpenseReadExpenseTypeFields = Field(alias='expense_type_fields')

    expense_report: SimpleExpenseReport = Field(alias='expenseReport')

    merchant: str = Field(alias='merchant')

    trans_date: datetime = Field(alias='transDate')

    currency_rate_final: str = Field(alias='currency_rate_final')

    tax_percentage: str = Field(alias='tax_percentage')

    id: typing.Optional[int] = Field(None, alias='id')

    requester: typing.Optional[SimpleUserSummary] = Field(None, alias='requester')

    approver: typing.Optional[SimpleUserSummary] = Field(None, alias='approver')

    approved_date: typing.Optional[datetime] = Field(None, alias='approved_date')

    is_active: typing.Optional[bool] = Field(None, alias='is_active')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    reimburse: typing.Optional[bool] = Field(None, alias='reimburse')

    expense_type: typing.Optional[ExpenseTypeEnum] = Field(None, alias='expense_type')

    payment_type: typing.Optional[PaymentMethodTypeEnum] = Field(None, alias='paymentType')

    amount: typing.Optional[typing.Optional[str]] = Field(None, alias='amount')

    exchange_rate_override: typing.Optional[bool] = Field(None, alias='exchange_rate_override')

    tax_name: typing.Optional[str] = Field(None, alias='tax_name')

    tax_amount: typing.Optional[typing.Optional[str]] = Field(None, alias='tax_amount')

    tax_is_inclusive: typing.Optional[bool] = Field(None, alias='tax_is_inclusive')

    notes: typing.Optional[typing.Optional[str]] = Field(None, alias='notes')

    attachment: typing.Optional[str] = Field(None, alias='attachment')

    active: typing.Optional[bool] = Field(None, alias='active')

    last_changed_by: typing.Optional[typing.Optional[int]] = Field(None, alias='last_changed_by')

    creditcard: typing.Optional[typing.Optional[int]] = Field(None, alias='creditcard')

    tax: typing.Optional[typing.Optional[int]] = Field(None, alias='tax')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
