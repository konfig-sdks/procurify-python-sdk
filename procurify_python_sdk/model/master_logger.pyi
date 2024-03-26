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


class MasterLogger(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "approval_delegation",
            "nextApprover",
            "next_approver",
            "user",
        }
        
        class properties:
        
            @staticmethod
            def user() -> typing.Type['UserSummary']:
                return UserSummary
        
            @staticmethod
            def next_approver() -> typing.Type['UserSummary']:
                return UserSummary
        
            @staticmethod
            def nextApprover() -> typing.Type['UserSummary']:
                return UserSummary
        
            @staticmethod
            def approval_delegation() -> typing.Type['ApprovalDelegationReadNullable']:
                return ApprovalDelegationReadNullable
            id = schemas.IntSchema
            dateTime = schemas.DateTimeSchema
            
            
            class action(
                schemas.ComposedBase,
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
                    
                    @classmethod
                    @functools.lru_cache()
                    def one_of(cls):
                        # we need this here to make our import statements work
                        # we must store _composed_schemas in here so the code is only run
                        # when we invoke this method. If we kept this at the class
                        # level we would get an error because the class level
                        # code would be run when this module is imported, and these composed
                        # classes don't exist yet because their module has not finished
                        # loading
                        return [
                            ActionEnum,
                            NullEnum,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'action':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class line_qty_pass(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'line_qty_pass':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class line_qty_fail(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'line_qty_fail':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class order(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'order':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class lineItem(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'lineItem':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class PO(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'PO':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class inventoryItem(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'inventoryItem':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class stocking_parent(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'stocking_parent':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "user": user,
                "next_approver": next_approver,
                "nextApprover": nextApprover,
                "approval_delegation": approval_delegation,
                "id": id,
                "dateTime": dateTime,
                "action": action,
                "line_qty_pass": line_qty_pass,
                "line_qty_fail": line_qty_fail,
                "order": order,
                "lineItem": lineItem,
                "PO": PO,
                "inventoryItem": inventoryItem,
                "stocking_parent": stocking_parent,
            }
    
    approval_delegation: 'ApprovalDelegationReadNullable'
    nextApprover: 'UserSummary'
    next_approver: 'UserSummary'
    user: 'UserSummary'
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> 'UserSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["next_approver"]) -> 'UserSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["nextApprover"]) -> 'UserSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval_delegation"]) -> 'ApprovalDelegationReadNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateTime"]) -> MetaOapg.properties.dateTime: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["action"]) -> MetaOapg.properties.action: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_qty_pass"]) -> MetaOapg.properties.line_qty_pass: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["line_qty_fail"]) -> MetaOapg.properties.line_qty_fail: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["order"]) -> MetaOapg.properties.order: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lineItem"]) -> MetaOapg.properties.lineItem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["PO"]) -> MetaOapg.properties.PO: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["inventoryItem"]) -> MetaOapg.properties.inventoryItem: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["stocking_parent"]) -> MetaOapg.properties.stocking_parent: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["user", "next_approver", "nextApprover", "approval_delegation", "id", "dateTime", "action", "line_qty_pass", "line_qty_fail", "order", "lineItem", "PO", "inventoryItem", "stocking_parent", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> 'UserSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["next_approver"]) -> 'UserSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["nextApprover"]) -> 'UserSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval_delegation"]) -> 'ApprovalDelegationReadNullable': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateTime"]) -> typing.Union[MetaOapg.properties.dateTime, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["action"]) -> typing.Union[MetaOapg.properties.action, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_qty_pass"]) -> typing.Union[MetaOapg.properties.line_qty_pass, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["line_qty_fail"]) -> typing.Union[MetaOapg.properties.line_qty_fail, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["order"]) -> typing.Union[MetaOapg.properties.order, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lineItem"]) -> typing.Union[MetaOapg.properties.lineItem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["PO"]) -> typing.Union[MetaOapg.properties.PO, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["inventoryItem"]) -> typing.Union[MetaOapg.properties.inventoryItem, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["stocking_parent"]) -> typing.Union[MetaOapg.properties.stocking_parent, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["user", "next_approver", "nextApprover", "approval_delegation", "id", "dateTime", "action", "line_qty_pass", "line_qty_fail", "order", "lineItem", "PO", "inventoryItem", "stocking_parent", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        approval_delegation: 'ApprovalDelegationReadNullable',
        nextApprover: 'UserSummary',
        next_approver: 'UserSummary',
        user: 'UserSummary',
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        dateTime: typing.Union[MetaOapg.properties.dateTime, str, datetime, schemas.Unset] = schemas.unset,
        action: typing.Union[MetaOapg.properties.action, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        line_qty_pass: typing.Union[MetaOapg.properties.line_qty_pass, None, str, schemas.Unset] = schemas.unset,
        line_qty_fail: typing.Union[MetaOapg.properties.line_qty_fail, None, str, schemas.Unset] = schemas.unset,
        order: typing.Union[MetaOapg.properties.order, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        lineItem: typing.Union[MetaOapg.properties.lineItem, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        PO: typing.Union[MetaOapg.properties.PO, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        inventoryItem: typing.Union[MetaOapg.properties.inventoryItem, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        stocking_parent: typing.Union[MetaOapg.properties.stocking_parent, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'MasterLogger':
        return super().__new__(
            cls,
            *args,
            approval_delegation=approval_delegation,
            nextApprover=nextApprover,
            next_approver=next_approver,
            user=user,
            id=id,
            dateTime=dateTime,
            action=action,
            line_qty_pass=line_qty_pass,
            line_qty_fail=line_qty_fail,
            order=order,
            lineItem=lineItem,
            PO=PO,
            inventoryItem=inventoryItem,
            stocking_parent=stocking_parent,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.action_enum import ActionEnum
from procurify_python_sdk.model.approval_delegation_read_nullable import ApprovalDelegationReadNullable
from procurify_python_sdk.model.null_enum import NullEnum
from procurify_python_sdk.model.user_summary import UserSummary
