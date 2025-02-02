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


class UserSummary(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "department",
            "user",
            "email",
        }
        
        class properties:
        
            @staticmethod
            def department() -> typing.Type['DepartmentSummary']:
                return DepartmentSummary
            
            
            class email(
                schemas.StrSchema
            ):
                pass
            user = schemas.IntSchema
            id = schemas.IntSchema
            created_at = schemas.DateTimeSchema
            updated_at = schemas.DateTimeSchema
            
            
            class firstName(
                schemas.StrSchema
            ):
                pass
            
            
            class lastName(
                schemas.StrSchema
            ):
                pass
            
            
            class position(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'position':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class phone(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phone':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class address(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'address':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            notifications = schemas.BoolSchema
            is_active = schemas.BoolSchema
            mobile = schemas.BoolSchema
            
            
            class profile_image(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'profile_image':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class slack_user_id(
                schemas.StrSchema
            ):
                pass
            is_sso_enabled = schemas.BoolSchema
            
            
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
        
            @staticmethod
            def approval_delegatee() -> typing.Type['UserSummaryApprovalDelegatee']:
                return UserSummaryApprovalDelegatee
            expected_return_date = schemas.DateSchema
            __annotations__ = {
                "department": department,
                "email": email,
                "user": user,
                "id": id,
                "created_at": created_at,
                "updated_at": updated_at,
                "firstName": firstName,
                "lastName": lastName,
                "position": position,
                "phone": phone,
                "address": address,
                "notifications": notifications,
                "is_active": is_active,
                "mobile": mobile,
                "profile_image": profile_image,
                "slack_user_id": slack_user_id,
                "is_sso_enabled": is_sso_enabled,
                "last_changed_by": last_changed_by,
                "approval_delegatee": approval_delegatee,
                "expected_return_date": expected_return_date,
            }
    
    department: 'DepartmentSummary'
    user: MetaOapg.properties.user
    email: MetaOapg.properties.email
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["department"]) -> 'DepartmentSummary': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["created_at"]) -> MetaOapg.properties.created_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["updated_at"]) -> MetaOapg.properties.updated_at: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["firstName"]) -> MetaOapg.properties.firstName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["lastName"]) -> MetaOapg.properties.lastName: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["position"]) -> MetaOapg.properties.position: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phone"]) -> MetaOapg.properties.phone: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["address"]) -> MetaOapg.properties.address: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["notifications"]) -> MetaOapg.properties.notifications: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_active"]) -> MetaOapg.properties.is_active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["mobile"]) -> MetaOapg.properties.mobile: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["profile_image"]) -> MetaOapg.properties.profile_image: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["slack_user_id"]) -> MetaOapg.properties.slack_user_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_sso_enabled"]) -> MetaOapg.properties.is_sso_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["last_changed_by"]) -> MetaOapg.properties.last_changed_by: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["approval_delegatee"]) -> 'UserSummaryApprovalDelegatee': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["expected_return_date"]) -> MetaOapg.properties.expected_return_date: ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["department", "email", "user", "id", "created_at", "updated_at", "firstName", "lastName", "position", "phone", "address", "notifications", "is_active", "mobile", "profile_image", "slack_user_id", "is_sso_enabled", "last_changed_by", "approval_delegatee", "expected_return_date", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["department"]) -> 'DepartmentSummary': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> MetaOapg.properties.email: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["user"]) -> MetaOapg.properties.user: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["created_at"]) -> typing.Union[MetaOapg.properties.created_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["updated_at"]) -> typing.Union[MetaOapg.properties.updated_at, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["firstName"]) -> typing.Union[MetaOapg.properties.firstName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["lastName"]) -> typing.Union[MetaOapg.properties.lastName, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["position"]) -> typing.Union[MetaOapg.properties.position, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phone"]) -> typing.Union[MetaOapg.properties.phone, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["address"]) -> typing.Union[MetaOapg.properties.address, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["notifications"]) -> typing.Union[MetaOapg.properties.notifications, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_active"]) -> typing.Union[MetaOapg.properties.is_active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["mobile"]) -> typing.Union[MetaOapg.properties.mobile, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["profile_image"]) -> typing.Union[MetaOapg.properties.profile_image, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["slack_user_id"]) -> typing.Union[MetaOapg.properties.slack_user_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_sso_enabled"]) -> typing.Union[MetaOapg.properties.is_sso_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["last_changed_by"]) -> typing.Union[MetaOapg.properties.last_changed_by, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["approval_delegatee"]) -> typing.Union['UserSummaryApprovalDelegatee', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["expected_return_date"]) -> typing.Union[MetaOapg.properties.expected_return_date, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["department", "email", "user", "id", "created_at", "updated_at", "firstName", "lastName", "position", "phone", "address", "notifications", "is_active", "mobile", "profile_image", "slack_user_id", "is_sso_enabled", "last_changed_by", "approval_delegatee", "expected_return_date", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        department: 'DepartmentSummary',
        user: typing.Union[MetaOapg.properties.user, decimal.Decimal, int, ],
        email: typing.Union[MetaOapg.properties.email, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        created_at: typing.Union[MetaOapg.properties.created_at, str, datetime, schemas.Unset] = schemas.unset,
        updated_at: typing.Union[MetaOapg.properties.updated_at, str, datetime, schemas.Unset] = schemas.unset,
        firstName: typing.Union[MetaOapg.properties.firstName, str, schemas.Unset] = schemas.unset,
        lastName: typing.Union[MetaOapg.properties.lastName, str, schemas.Unset] = schemas.unset,
        position: typing.Union[MetaOapg.properties.position, None, str, schemas.Unset] = schemas.unset,
        phone: typing.Union[MetaOapg.properties.phone, None, str, schemas.Unset] = schemas.unset,
        address: typing.Union[MetaOapg.properties.address, None, str, schemas.Unset] = schemas.unset,
        notifications: typing.Union[MetaOapg.properties.notifications, bool, schemas.Unset] = schemas.unset,
        is_active: typing.Union[MetaOapg.properties.is_active, bool, schemas.Unset] = schemas.unset,
        mobile: typing.Union[MetaOapg.properties.mobile, bool, schemas.Unset] = schemas.unset,
        profile_image: typing.Union[MetaOapg.properties.profile_image, None, str, schemas.Unset] = schemas.unset,
        slack_user_id: typing.Union[MetaOapg.properties.slack_user_id, str, schemas.Unset] = schemas.unset,
        is_sso_enabled: typing.Union[MetaOapg.properties.is_sso_enabled, bool, schemas.Unset] = schemas.unset,
        last_changed_by: typing.Union[MetaOapg.properties.last_changed_by, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        approval_delegatee: typing.Union['UserSummaryApprovalDelegatee', schemas.Unset] = schemas.unset,
        expected_return_date: typing.Union[MetaOapg.properties.expected_return_date, str, date, schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'UserSummary':
        return super().__new__(
            cls,
            *args,
            department=department,
            user=user,
            email=email,
            id=id,
            created_at=created_at,
            updated_at=updated_at,
            firstName=firstName,
            lastName=lastName,
            position=position,
            phone=phone,
            address=address,
            notifications=notifications,
            is_active=is_active,
            mobile=mobile,
            profile_image=profile_image,
            slack_user_id=slack_user_id,
            is_sso_enabled=is_sso_enabled,
            last_changed_by=last_changed_by,
            approval_delegatee=approval_delegatee,
            expected_return_date=expected_return_date,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.department_summary import DepartmentSummary
from procurify_python_sdk.model.user_summary_approval_delegatee import UserSummaryApprovalDelegatee
