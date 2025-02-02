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


class CreditCard(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "vendor",
            "currency",
            "uuid",
        }
        
        class properties:
            uuid = schemas.UUIDSchema
            vendor = schemas.IntSchema
            currency = schemas.IntSchema
            id = schemas.IntSchema
            is_active = schemas.BoolSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            
            
            class number(
                schemas.StrSchema
            ):
                pass
            
            
            class balance(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'balance':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class gl_code(
                schemas.StrSchema
            ):
                pass
        
            @staticmethod
            def type() -> typing.Type['CreditCardTypeEnum']:
                return CreditCardTypeEnum
            
            
            class category(
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
                            ZeroOneEnum,
                            NullEnum,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'category':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class external_id(
                schemas.StrSchema
            ):
                pass
            
            
            class status(
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
                            CreditCardStatusEnum,
                            BlankEnum,
                            NullEnum,
                        ]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'status':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            require_activation = schemas.BoolSchema
            
            
            class last_changed_by(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'last_changed_by':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class payment_method(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_method':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class creator(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'creator':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            __annotations__ = {
                "uuid": uuid,
                "vendor": vendor,
                "currency": currency,
                "id": id,
                "is_active": is_active,
                "created_at": created_at,
                "updated_at": updated_at,
                "name": name,
                "number": number,
                "balance": balance,
                "gl_code": gl_code,
                "type": type,
                "category": category,
                "external_id": external_id,
                "status": status,
                "require_activation": require_activation,
                "last_changed_by": last_changed_by,
                "payment_method": payment_method,
                "creator": creator,
            }
    
    vendor: MetaOapg.properties.vendor
    currency: MetaOapg.properties.currency
    uuid: MetaOapg.properties.uuid
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["number"]) -> MetaOapg.properties.number: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["balance"]) -> MetaOapg.properties.balance: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["gl_code"]) -> MetaOapg.properties.gl_code: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'CreditCardTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["category"]) -> MetaOapg.properties.category: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["status"]) -> MetaOapg.properties.status: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["require_activation"]) -> MetaOapg.properties.require_activation: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_changed_by"]) -> MetaOapg.properties.last_changed_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method"]) -> MetaOapg.properties.payment_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creator"]) -> MetaOapg.properties.creator: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["uuid", "vendor", "currency", "id", "is_active", "created_at", "updated_at", "name", "number", "balance", "gl_code", "type", "category", "external_id", "status", "require_activation", "last_changed_by", "payment_method", "creator", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["uuid"]) -> MetaOapg.properties.uuid: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor"]) -> MetaOapg.properties.vendor: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> typing.Union[MetaOapg.properties.name, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["number"]) -> typing.Union[MetaOapg.properties.number, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["balance"]) -> typing.Union[MetaOapg.properties.balance, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["gl_code"]) -> typing.Union[MetaOapg.properties.gl_code, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> typing.Union['CreditCardTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["category"]) -> typing.Union[MetaOapg.properties.category, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["status"]) -> typing.Union[MetaOapg.properties.status, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["require_activation"]) -> typing.Union[MetaOapg.properties.require_activation, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_changed_by"]) -> typing.Union[MetaOapg.properties.last_changed_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method"]) -> typing.Union[MetaOapg.properties.payment_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creator"]) -> typing.Union[MetaOapg.properties.creator, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["uuid", "vendor", "currency", "id", "is_active", "created_at", "updated_at", "name", "number", "balance", "gl_code", "type", "category", "external_id", "status", "require_activation", "last_changed_by", "payment_method", "creator", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        vendor: typing.Union[MetaOapg.properties.vendor, decimal.Decimal, int, ],
        currency: typing.Union[MetaOapg.properties.currency, decimal.Decimal, int, ],
        uuid: typing.Union[MetaOapg.properties.uuid, str, uuid.UUID, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        name: typing.Union[MetaOapg.properties.name, str, schemas.Unset] = schemas.unset,
        number: typing.Union[MetaOapg.properties.number, str, schemas.Unset] = schemas.unset,
        balance: typing.Union[MetaOapg.properties.balance, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        gl_code: typing.Union[MetaOapg.properties.gl_code, str, schemas.Unset] = schemas.unset,
        type: typing.Union['CreditCardTypeEnum', schemas.Unset] = schemas.unset,
        category: typing.Union[MetaOapg.properties.category, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, str, schemas.Unset] = schemas.unset,
        status: typing.Union[MetaOapg.properties.status, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        require_activation: typing.Union[MetaOapg.properties.require_activation, bool, schemas.Unset] = schemas.unset,
        last_changed_by: typing.Union[MetaOapg.properties.last_changed_by, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_method: typing.Union[MetaOapg.properties.payment_method, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creator: typing.Union[MetaOapg.properties.creator, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CreditCard':
        return super().__new__(
            cls,
            *args,
            vendor=vendor,
            currency=currency,
            uuid=uuid,
            id=id,
            is_active=is_active,
            created_at=created_at,
            updated_at=updated_at,
            name=name,
            number=number,
            balance=balance,
            gl_code=gl_code,
            type=type,
            category=category,
            external_id=external_id,
            status=status,
            require_activation=require_activation,
            last_changed_by=last_changed_by,
            payment_method=payment_method,
            creator=creator,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.blank_enum import BlankEnum
from procurify_python_sdk.model.credit_card_status_enum import CreditCardStatusEnum
from procurify_python_sdk.model.credit_card_type_enum import CreditCardTypeEnum
from procurify_python_sdk.model.null_enum import NullEnum
from procurify_python_sdk.model.zero_one_enum import ZeroOneEnum
