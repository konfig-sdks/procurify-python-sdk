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


class PurchaseOrderStateEnum(
    schemas.EnumBase,
    schemas.IntSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        enum_value_to_name = {
            0: "POSITIVE_0",
            1: "POSITIVE_1",
            3: "POSITIVE_3",
            4: "POSITIVE_4",
            5: "POSITIVE_5",
        }
    
    @schemas.classproperty
    def POSITIVE_0(cls):
        return cls(0)
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def POSITIVE_3(cls):
        return cls(3)
    
    @schemas.classproperty
    def POSITIVE_4(cls):
        return cls(4)
    
    @schemas.classproperty
    def POSITIVE_5(cls):
        return cls(5)
