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


class SpendAccountRead(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "account_code",
            "department",
        }
        
        class properties:
        
            @staticmethod
            def account_code() -> typing.Type['UnoptimizedAccountCodeserializer']:
                return UnoptimizedAccountCodeserializer
        
            @staticmethod
            def department() -> typing.Type['UnoptimizedDepartmentRead']:
                return UnoptimizedDepartmentRead
            id = schemas.IntSchema
            active = schemas.BoolSchema
            __annotations__ = {
                "account_code": account_code,
                "department": department,
                "id": id,
                "active": active,
            }
    
    account_code: 'UnoptimizedAccountCodeserializer'
    department: 'UnoptimizedDepartmentRead'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["account_code"]) -> 'UnoptimizedAccountCodeserializer': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> 'UnoptimizedDepartmentRead': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["account_code", "department", "id", "active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["account_code"]) -> 'UnoptimizedAccountCodeserializer': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> 'UnoptimizedDepartmentRead': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["account_code", "department", "id", "active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        account_code: 'UnoptimizedAccountCodeserializer',
        department: 'UnoptimizedDepartmentRead',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'SpendAccountRead':
        return super().__new__(
            cls,
            *args,
            account_code=account_code,
            department=department,
            id=id,
            active=active,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.unoptimized_account_codeserializer import UnoptimizedAccountCodeserializer
from procurify_python_sdk.model.unoptimized_department_read import UnoptimizedDepartmentRead
