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

from procurify_python_sdk.type.account_code_read import AccountCodeRead
from procurify_python_sdk.type.catalog_item_read_departments import CatalogItemReadDepartments
from procurify_python_sdk.type.catalog_item_read_selected_account import CatalogItemReadSelectedAccount
from procurify_python_sdk.type.currency_summary import CurrencySummary
from procurify_python_sdk.type.custom_field_value_read import CustomFieldValueRead
from procurify_python_sdk.type.vendor_read import VendorRead

class RequiredCatalogItemReadNullable(TypedDict):
    name: str

    pref_vendor: VendorRead

    account_code: AccountCodeRead

    currency: CurrencySummary

class OptionalCatalogItemReadNullable(TypedDict, total=False):
    description: typing.Optional[str]

    id: int

    image: str

    unitType: str

    internalSKU: str

    product_url: typing.Optional[str]

    price: str

    rfo_lock: bool

    departments: CatalogItemReadDepartments

    custom_fields: typing.List[CustomFieldValueRead]

    requested_count: int

    last_requested_date: typing.Optional[datetime]

    selected_account: CatalogItemReadSelectedAccount

class CatalogItemReadNullable(RequiredCatalogItemReadNullable, OptionalCatalogItemReadNullable):
    pass
