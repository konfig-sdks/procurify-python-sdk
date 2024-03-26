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


class OptimizedVendor(
    schemas.DictSchema
):
    """
    This class is auto generated by Konfig (https://konfigthis.com)
    """


    class MetaOapg:
        required = {
            "name",
            "type",
            "email",
            "overall_score",
        }
        
        class properties:
            
            
            class name(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 150
        
            @staticmethod
            def email() -> typing.Type['OptimizedVendorEmail']:
                return OptimizedVendorEmail
        
            @staticmethod
            def type() -> typing.Type['VendorTypeEnum']:
                return VendorTypeEnum
            
            
            class overall_score(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    format = 'decimal'
                    regex=[{
                        'pattern': r'^\d{0,2}(?:\.\d{0,3})?$',
                    }]
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'overall_score':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            id = schemas.IntSchema
            active = schemas.BoolSchema
            
            
            class addressLineOne(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 300
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressLineOne':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class addressLineTwo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 300
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'addressLineTwo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class postalCode(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'postalCode':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class city(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'city':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class state_province(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 40
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'state_province':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class country(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 80
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'country':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class phoneOne(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phoneOne':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class phoneTwo(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'phoneTwo':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class fax(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 20
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'fax':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class comments(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'comments':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class contact(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 50
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'contact':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class url(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 200
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'url':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class external_id(
                schemas.StrBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneStrMixin
            ):
            
            
                class MetaOapg:
                    max_length = 100
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, str, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'external_id':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            dateModified = schemas.DateTimeSchema
            
            
            class currency(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'currency':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
        
            @staticmethod
            def payment_term_ref() -> typing.Type['PaymentTermNullable']:
                return PaymentTermNullable
        
            @staticmethod
            def shipping_term_ref() -> typing.Type['ShippingTermNullable']:
                return ShippingTermNullable
        
            @staticmethod
            def payment_method_ref() -> typing.Type['PaymentMethodNullable']:
                return PaymentMethodNullable
        
            @staticmethod
            def shipping_method_ref() -> typing.Type['ShippingMethodNullable']:
                return ShippingMethodNullable
            
            
            class payment_methods(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['PaymentMethodRead']:
                        return PaymentMethodRead
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['PaymentMethodRead'], typing.List['PaymentMethodRead']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'payment_methods':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'PaymentMethodRead':
                    return super().__getitem__(i)
            
            
            class tax(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'tax':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class default_payment_method(
                schemas.IntBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneDecimalMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, decimal.Decimal, int, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'default_payment_method':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            
            
            class creditcards(
                schemas.ListSchema
            ):
            
            
                class MetaOapg:
                    
                    @staticmethod
                    def items() -> typing.Type['CreditCard']:
                        return CreditCard
            
                def __new__(
                    cls,
                    arg: typing.Union[typing.Tuple['CreditCard'], typing.List['CreditCard']],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'creditcards':
                    return super().__new__(
                        cls,
                        arg,
                        _configuration=_configuration,
                    )
            
                def __getitem__(self, i: int) -> 'CreditCard':
                    return super().__getitem__(i)
            
            
            class is_1099_eligible(
                schemas.BoolBase,
                schemas.NoneBase,
                schemas.Schema,
                schemas.NoneBoolMixin
            ):
            
            
                def __new__(
                    cls,
                    *args: typing.Union[None, bool, ],
                    _configuration: typing.Optional[schemas.Configuration] = None,
                ) -> 'is_1099_eligible':
                    return super().__new__(
                        cls,
                        *args,
                        _configuration=_configuration,
                    )
            is_auto_email_po_enabled = schemas.BoolSchema
            
            
            class po_pdf_labels(
                schemas.StrSchema
            ):
            
            
                class MetaOapg:
                    max_length = 200
        
            @staticmethod
            def vendor_request() -> typing.Type['NestedVendorRequest']:
                return NestedVendorRequest
            __annotations__ = {
                "name": name,
                "email": email,
                "type": type,
                "overall_score": overall_score,
                "id": id,
                "active": active,
                "addressLineOne": addressLineOne,
                "addressLineTwo": addressLineTwo,
                "postalCode": postalCode,
                "city": city,
                "state_province": state_province,
                "country": country,
                "phoneOne": phoneOne,
                "phoneTwo": phoneTwo,
                "fax": fax,
                "comments": comments,
                "contact": contact,
                "url": url,
                "external_id": external_id,
                "dateModified": dateModified,
                "currency": currency,
                "payment_term_ref": payment_term_ref,
                "shipping_term_ref": shipping_term_ref,
                "payment_method_ref": payment_method_ref,
                "shipping_method_ref": shipping_method_ref,
                "payment_methods": payment_methods,
                "tax": tax,
                "default_payment_method": default_payment_method,
                "creditcards": creditcards,
                "is_1099_eligible": is_1099_eligible,
                "is_auto_email_po_enabled": is_auto_email_po_enabled,
                "po_pdf_labels": po_pdf_labels,
                "vendor_request": vendor_request,
            }
    
    name: MetaOapg.properties.name
    type: 'VendorTypeEnum'
    email: 'OptimizedVendorEmail'
    overall_score: MetaOapg.properties.overall_score
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["email"]) -> 'OptimizedVendorEmail': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["type"]) -> 'VendorTypeEnum': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["overall_score"]) -> MetaOapg.properties.overall_score: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["id"]) -> MetaOapg.properties.id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["active"]) -> MetaOapg.properties.active: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLineOne"]) -> MetaOapg.properties.addressLineOne: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["addressLineTwo"]) -> MetaOapg.properties.addressLineTwo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["postalCode"]) -> MetaOapg.properties.postalCode: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["city"]) -> MetaOapg.properties.city: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["state_province"]) -> MetaOapg.properties.state_province: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["country"]) -> MetaOapg.properties.country: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneOne"]) -> MetaOapg.properties.phoneOne: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["phoneTwo"]) -> MetaOapg.properties.phoneTwo: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["fax"]) -> MetaOapg.properties.fax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["comments"]) -> MetaOapg.properties.comments: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["contact"]) -> MetaOapg.properties.contact: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["url"]) -> MetaOapg.properties.url: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["external_id"]) -> MetaOapg.properties.external_id: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["dateModified"]) -> MetaOapg.properties.dateModified: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["currency"]) -> MetaOapg.properties.currency: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_term_ref"]) -> 'PaymentTermNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_term_ref"]) -> 'ShippingTermNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_method_ref"]) -> 'PaymentMethodNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["shipping_method_ref"]) -> 'ShippingMethodNullable': ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["payment_methods"]) -> MetaOapg.properties.payment_methods: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["tax"]) -> MetaOapg.properties.tax: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["default_payment_method"]) -> MetaOapg.properties.default_payment_method: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["creditcards"]) -> MetaOapg.properties.creditcards: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_1099_eligible"]) -> MetaOapg.properties.is_1099_eligible: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["is_auto_email_po_enabled"]) -> MetaOapg.properties.is_auto_email_po_enabled: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["po_pdf_labels"]) -> MetaOapg.properties.po_pdf_labels: ...
    
    @typing.overload
    def __getitem__(self, name: typing_extensions.Literal["vendor_request"]) -> 'NestedVendorRequest': ...
    
    @typing.overload
    def __getitem__(self, name: str) -> schemas.UnsetAnyTypeSchema: ...
    
    def __getitem__(self, name: typing.Union[typing_extensions.Literal["name", "email", "type", "overall_score", "id", "active", "addressLineOne", "addressLineTwo", "postalCode", "city", "state_province", "country", "phoneOne", "phoneTwo", "fax", "comments", "contact", "url", "external_id", "dateModified", "currency", "payment_term_ref", "shipping_term_ref", "payment_method_ref", "shipping_method_ref", "payment_methods", "tax", "default_payment_method", "creditcards", "is_1099_eligible", "is_auto_email_po_enabled", "po_pdf_labels", "vendor_request", ], str]):
        # dict_instance[name] accessor
        return super().__getitem__(name)
    
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["name"]) -> MetaOapg.properties.name: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["email"]) -> 'OptimizedVendorEmail': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["type"]) -> 'VendorTypeEnum': ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["overall_score"]) -> MetaOapg.properties.overall_score: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["id"]) -> typing.Union[MetaOapg.properties.id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["active"]) -> typing.Union[MetaOapg.properties.active, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLineOne"]) -> typing.Union[MetaOapg.properties.addressLineOne, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["addressLineTwo"]) -> typing.Union[MetaOapg.properties.addressLineTwo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["postalCode"]) -> typing.Union[MetaOapg.properties.postalCode, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["city"]) -> typing.Union[MetaOapg.properties.city, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["state_province"]) -> typing.Union[MetaOapg.properties.state_province, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["country"]) -> typing.Union[MetaOapg.properties.country, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneOne"]) -> typing.Union[MetaOapg.properties.phoneOne, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["phoneTwo"]) -> typing.Union[MetaOapg.properties.phoneTwo, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["fax"]) -> typing.Union[MetaOapg.properties.fax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["comments"]) -> typing.Union[MetaOapg.properties.comments, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["contact"]) -> typing.Union[MetaOapg.properties.contact, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["url"]) -> typing.Union[MetaOapg.properties.url, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["external_id"]) -> typing.Union[MetaOapg.properties.external_id, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["dateModified"]) -> typing.Union[MetaOapg.properties.dateModified, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["currency"]) -> typing.Union[MetaOapg.properties.currency, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_term_ref"]) -> typing.Union['PaymentTermNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_term_ref"]) -> typing.Union['ShippingTermNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_method_ref"]) -> typing.Union['PaymentMethodNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["shipping_method_ref"]) -> typing.Union['ShippingMethodNullable', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["payment_methods"]) -> typing.Union[MetaOapg.properties.payment_methods, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["tax"]) -> typing.Union[MetaOapg.properties.tax, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["default_payment_method"]) -> typing.Union[MetaOapg.properties.default_payment_method, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["creditcards"]) -> typing.Union[MetaOapg.properties.creditcards, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_1099_eligible"]) -> typing.Union[MetaOapg.properties.is_1099_eligible, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["is_auto_email_po_enabled"]) -> typing.Union[MetaOapg.properties.is_auto_email_po_enabled, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["po_pdf_labels"]) -> typing.Union[MetaOapg.properties.po_pdf_labels, schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: typing_extensions.Literal["vendor_request"]) -> typing.Union['NestedVendorRequest', schemas.Unset]: ...
    
    @typing.overload
    def get_item_oapg(self, name: str) -> typing.Union[schemas.UnsetAnyTypeSchema, schemas.Unset]: ...
    
    def get_item_oapg(self, name: typing.Union[typing_extensions.Literal["name", "email", "type", "overall_score", "id", "active", "addressLineOne", "addressLineTwo", "postalCode", "city", "state_province", "country", "phoneOne", "phoneTwo", "fax", "comments", "contact", "url", "external_id", "dateModified", "currency", "payment_term_ref", "shipping_term_ref", "payment_method_ref", "shipping_method_ref", "payment_methods", "tax", "default_payment_method", "creditcards", "is_1099_eligible", "is_auto_email_po_enabled", "po_pdf_labels", "vendor_request", ], str]):
        return super().get_item_oapg(name)
    

    def __new__(
        cls,
        *args: typing.Union[dict, frozendict.frozendict, ],
        name: typing.Union[MetaOapg.properties.name, str, ],
        type: 'VendorTypeEnum',
        email: 'OptimizedVendorEmail',
        overall_score: typing.Union[MetaOapg.properties.overall_score, None, str, ],
        id: typing.Union[MetaOapg.properties.id, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        active: typing.Union[MetaOapg.properties.active, bool, schemas.Unset] = schemas.unset,
        addressLineOne: typing.Union[MetaOapg.properties.addressLineOne, None, str, schemas.Unset] = schemas.unset,
        addressLineTwo: typing.Union[MetaOapg.properties.addressLineTwo, None, str, schemas.Unset] = schemas.unset,
        postalCode: typing.Union[MetaOapg.properties.postalCode, None, str, schemas.Unset] = schemas.unset,
        city: typing.Union[MetaOapg.properties.city, None, str, schemas.Unset] = schemas.unset,
        state_province: typing.Union[MetaOapg.properties.state_province, None, str, schemas.Unset] = schemas.unset,
        country: typing.Union[MetaOapg.properties.country, None, str, schemas.Unset] = schemas.unset,
        phoneOne: typing.Union[MetaOapg.properties.phoneOne, None, str, schemas.Unset] = schemas.unset,
        phoneTwo: typing.Union[MetaOapg.properties.phoneTwo, None, str, schemas.Unset] = schemas.unset,
        fax: typing.Union[MetaOapg.properties.fax, None, str, schemas.Unset] = schemas.unset,
        comments: typing.Union[MetaOapg.properties.comments, None, str, schemas.Unset] = schemas.unset,
        contact: typing.Union[MetaOapg.properties.contact, None, str, schemas.Unset] = schemas.unset,
        url: typing.Union[MetaOapg.properties.url, None, str, schemas.Unset] = schemas.unset,
        external_id: typing.Union[MetaOapg.properties.external_id, None, str, schemas.Unset] = schemas.unset,
        dateModified: typing.Union[MetaOapg.properties.dateModified, str, datetime, schemas.Unset] = schemas.unset,
        currency: typing.Union[MetaOapg.properties.currency, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        payment_term_ref: typing.Union['PaymentTermNullable', schemas.Unset] = schemas.unset,
        shipping_term_ref: typing.Union['ShippingTermNullable', schemas.Unset] = schemas.unset,
        payment_method_ref: typing.Union['PaymentMethodNullable', schemas.Unset] = schemas.unset,
        shipping_method_ref: typing.Union['ShippingMethodNullable', schemas.Unset] = schemas.unset,
        payment_methods: typing.Union[MetaOapg.properties.payment_methods, list, tuple, schemas.Unset] = schemas.unset,
        tax: typing.Union[MetaOapg.properties.tax, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        default_payment_method: typing.Union[MetaOapg.properties.default_payment_method, None, decimal.Decimal, int, schemas.Unset] = schemas.unset,
        creditcards: typing.Union[MetaOapg.properties.creditcards, list, tuple, schemas.Unset] = schemas.unset,
        is_1099_eligible: typing.Union[MetaOapg.properties.is_1099_eligible, None, bool, schemas.Unset] = schemas.unset,
        is_auto_email_po_enabled: typing.Union[MetaOapg.properties.is_auto_email_po_enabled, bool, schemas.Unset] = schemas.unset,
        po_pdf_labels: typing.Union[MetaOapg.properties.po_pdf_labels, str, schemas.Unset] = schemas.unset,
        vendor_request: typing.Union['NestedVendorRequest', schemas.Unset] = schemas.unset,
        _configuration: typing.Optional[schemas.Configuration] = None,
        **kwargs: typing.Union[schemas.AnyTypeSchema, dict, frozendict.frozendict, str, date, datetime, uuid.UUID, int, float, decimal.Decimal, None, list, tuple, bytes],
    ) -> 'OptimizedVendor':
        return super().__new__(
            cls,
            *args,
            name=name,
            type=type,
            email=email,
            overall_score=overall_score,
            id=id,
            active=active,
            addressLineOne=addressLineOne,
            addressLineTwo=addressLineTwo,
            postalCode=postalCode,
            city=city,
            state_province=state_province,
            country=country,
            phoneOne=phoneOne,
            phoneTwo=phoneTwo,
            fax=fax,
            comments=comments,
            contact=contact,
            url=url,
            external_id=external_id,
            dateModified=dateModified,
            currency=currency,
            payment_term_ref=payment_term_ref,
            shipping_term_ref=shipping_term_ref,
            payment_method_ref=payment_method_ref,
            shipping_method_ref=shipping_method_ref,
            payment_methods=payment_methods,
            tax=tax,
            default_payment_method=default_payment_method,
            creditcards=creditcards,
            is_1099_eligible=is_1099_eligible,
            is_auto_email_po_enabled=is_auto_email_po_enabled,
            po_pdf_labels=po_pdf_labels,
            vendor_request=vendor_request,
            _configuration=_configuration,
            **kwargs,
        )

from procurify_python_sdk.model.credit_card import CreditCard
from procurify_python_sdk.model.nested_vendor_request import NestedVendorRequest
from procurify_python_sdk.model.optimized_vendor_email import OptimizedVendorEmail
from procurify_python_sdk.model.payment_method_nullable import PaymentMethodNullable
from procurify_python_sdk.model.payment_method_read import PaymentMethodRead
from procurify_python_sdk.model.payment_term_nullable import PaymentTermNullable
from procurify_python_sdk.model.shipping_method_nullable import ShippingMethodNullable
from procurify_python_sdk.model.shipping_term_nullable import ShippingTermNullable
from procurify_python_sdk.model.vendor_type_enum import VendorTypeEnum
