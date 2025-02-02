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

from procurify_python_sdk.type.blank_enum import BlankEnum
from procurify_python_sdk.type.credit_card_status_enum import CreditCardStatusEnum
from procurify_python_sdk.type.credit_card_type_enum import CreditCardTypeEnum
from procurify_python_sdk.type.null_enum import NullEnum
from procurify_python_sdk.type.zero_one_enum import ZeroOneEnum

class RequiredCreditCard(TypedDict):
    uuid: str

    vendor: int

    currency: int

class OptionalCreditCard(TypedDict, total=False):
    id: int

    is_active: bool

    created_at: datetime

    updated_at: datetime

    name: str

    number: str

    balance: typing.Optional[int]

    gl_code: str

    type: CreditCardTypeEnum

    category: typing.Union[ZeroOneEnum, NullEnum]

    # External id of the Credit Card
    external_id: str

    # The status of the Credit Card
    status: typing.Union[CreditCardStatusEnum, BlankEnum, NullEnum]

    # Does this card require new activation?
    require_activation: bool

    last_changed_by: typing.Optional[int]

    payment_method: typing.Optional[int]

    creator: typing.Optional[int]

class CreditCard(RequiredCreditCard, OptionalCreditCard):
    pass
