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

from procurify_python_sdk.pydantic.address_association_enum import AddressAssociationEnum

class AddressSummary(BaseModel):
    name: str = Field(alias='name')

    address_line_one: str = Field(alias='addressLineOne')

    postal_code: str = Field(alias='postalCode')

    city: str = Field(alias='city')

    country: str = Field(alias='country')

    id: typing.Optional[int] = Field(None, alias='id')

    is_active: typing.Optional[bool] = Field(None, alias='is_active')

    created_at: typing.Optional[datetime] = Field(None, alias='created_at')

    updated_at: typing.Optional[datetime] = Field(None, alias='updated_at')

    address_association: typing.Optional[AddressAssociationEnum] = Field(None, alias='addressAssociation')

    address_line_two: typing.Optional[str] = Field(None, alias='addressLineTwo')

    state_province: typing.Optional[str] = Field(None, alias='state_province')

    last_changed_by: typing.Optional[typing.Optional[int]] = Field(None, alias='last_changed_by')

    model_config = ConfigDict(
        protected_namespaces=(),
        arbitrary_types_allowed=True
    )
