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

from procurify_python_sdk.type.account import Account
from procurify_python_sdk.type.currency_summary import CurrencySummary
from procurify_python_sdk.type.expense_read_expense_type_fields import ExpenseReadExpenseTypeFields
from procurify_python_sdk.type.expense_type_enum import ExpenseTypeEnum
from procurify_python_sdk.type.payment_method_type_enum import PaymentMethodTypeEnum
from procurify_python_sdk.type.simple_expense_report import SimpleExpenseReport
from procurify_python_sdk.type.simple_user_summary import SimpleUserSummary

class RequiredExpenseReadNullable(TypedDict):
    account: Account

    localCurrency: CurrencySummary

    expense_type_fields: ExpenseReadExpenseTypeFields

    expenseReport: SimpleExpenseReport

    merchant: str

    transDate: datetime

    currency_rate_final: str

    tax_percentage: str

class OptionalExpenseReadNullable(TypedDict, total=False):
    id: int

    requester: SimpleUserSummary

    approver: SimpleUserSummary

    approved_date: datetime

    is_active: bool

    created_at: datetime

    updated_at: datetime

    reimburse: bool

    expense_type: ExpenseTypeEnum

    paymentType: PaymentMethodTypeEnum

    amount: typing.Optional[str]

    exchange_rate_override: bool

    tax_name: str

    tax_amount: typing.Optional[str]

    tax_is_inclusive: bool

    notes: typing.Optional[str]

    attachment: str

    active: bool

    last_changed_by: typing.Optional[int]

    creditcard: typing.Optional[int]

    tax: typing.Optional[int]

class ExpenseReadNullable(RequiredExpenseReadNullable, OptionalExpenseReadNullable):
    pass
