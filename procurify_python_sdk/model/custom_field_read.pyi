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


class CustomFieldRead(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "content_type",
            "name",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
                pass
            content_type = schemas.IntSchema
            id = schemas.IntSchema
            
            
            class default_value(
                schemas.StrSchema
            ):
                pass
            is_required = schemas.BoolSchema
        
            @staticmethod
            def field_choices() -> typing.Type['CustomFieldReadFieldChoices']:
                return CustomFieldReadFieldChoices
        
            @staticmethod
            def field_type() -> typing.Type['FieldTypeEnum']:
                return FieldTypeEnum
            field_label = schemas.StrSchema
            is_active = schemas.BoolSchema
            __annotations__ = {
                "name": name,
                "content_type": content_type,
                "id": id,
                "default_value": default_value,
                "is_required": is_required,
                "field_choices": field_choices,
                "field_type": field_type,
                "field_label": field_label,
                "is_active": is_active,
            }
    
    content_type: MetaOapg.properties.content_type
    name: MetaOapg.properties.name
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_value"]) -> MetaOapg.properties.default_value: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_required"]) -> MetaOapg.properties.is_required: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_choices"]) -> 'CustomFieldReadFieldChoices': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_type"]) -> 'FieldTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["field_label"]) -> MetaOapg.properties.field_label: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "content_type", "id", "default_value", "is_required", "field_choices", "field_type", "field_label", "is_active", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["content_type"]) -> MetaOapg.properties.content_type: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_value"]) -> typing.Union[MetaOapg.properties.default_value, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_required"]) -> typing.Union[MetaOapg.properties.is_required, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_choices"]) -> typing.Union['CustomFieldReadFieldChoices', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_type"]) -> typing.Union['FieldTypeEnum', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["field_label"]) -> typing.Union[MetaOapg.properties.field_label, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "content_type", "id", "default_value", "is_required", "field_choices", "field_type", "field_label", "is_active", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        content_type: typing.Union[MetaOapg.properties.content_type, decimal.Decimal, int, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        default_value: typing.Union[MetaOapg.properties.default_value, str, schemas.Unset] = schemas.unset,
        is_required: typing.Union[MetaOapg.properties.is_required, bool, schemas.Unset] = schemas.unset,
        field_choices: typing.Union['CustomFieldReadFieldChoices', schemas.Unset] = schemas.unset,
        field_type: typing.Union['FieldTypeEnum', schemas.Unset] = schemas.unset,
        field_label: typing.Union[MetaOapg.properties.field_label, str, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'CustomFieldRead':
        return super().__new__(
            cls,
            *args,
            content_type=content_type,
            name=name,
            id=id,
            default_value=default_value,
            is_required=is_required,
            field_choices=field_choices,
            field_type=field_type,
            field_label=field_label,
            is_active=is_active,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.custom_field_read_field_choices import CustomFieldReadFieldChoices
from procurify_python_sdk.model.field_type_enum import FieldTypeEnum
