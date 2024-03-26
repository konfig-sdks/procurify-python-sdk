# coding: utf-8

"""
    Procurify API Documentation

     # Disclaimer  - Procurify’s API is evolving and is subject to change at any time. Additionally, aspects of the API are undocumented, including certain methods, events, and properties. Given that both documented and undocumented aspects of the Procurify API may change at any time, the client relies on the API at their own risk. - Client (and/or client’s representative) is responsible for building, testing, and maintaining any API connection between Procurify and any other tool.  Procurify’s responsibility strictly involves providing support on clarifications in regards to the issued API document. - Procurify’s API is offered on an “as is” and “as available” basis, without warranties of any kind. By accepting this agreement, you agree that you have read the current API documentation, and accept the API functionality in its current state including current limitations. For questions and clarification around the documentation, please contact support@procurify.com. - In accordance with Section 2.(b) of our Subscription Services Agreement, Procurify reserves the right to deny access to our API at any time. If your API requests are too large and time out, contact us immediately to avoid possible suspension of access. - You may not attempt to reverse engineer or otherwise derive source code, trade secrets, or know-how in the Procurify API or portion thereof. You may not use the Procurify API to replicate or compete with core products or services offered by Procurify. 

    Generated by: https://konfigthis.com
"""

from dataclasses import dataclass
import typing_extensions
import urllib3
from pydantic import RootModel
from procurify_python_sdk.request_before_hook import request_before_hook
import json
from urllib3._collections import HTTPHeaderDict

from procurify_python_sdk.api_response import AsyncGeneratorResponse
from procurify_python_sdk import api_client, exceptions
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

from procurify_python_sdk.model.company_payment_method_request_data import CompanyPaymentMethodRequestData as CompanyPaymentMethodRequestDataSchema
from procurify_python_sdk.model.company_payment_method_request import CompanyPaymentMethodRequest as CompanyPaymentMethodRequestSchema
from procurify_python_sdk.model.company_payment_method import CompanyPaymentMethod as CompanyPaymentMethodSchema
from procurify_python_sdk.model.payment_method_type_enum import PaymentMethodTypeEnum as PaymentMethodTypeEnumSchema

from procurify_python_sdk.type.payment_method_type_enum import PaymentMethodTypeEnum
from procurify_python_sdk.type.company_payment_method_request_data import CompanyPaymentMethodRequestData
from procurify_python_sdk.type.company_payment_method_request import CompanyPaymentMethodRequest
from procurify_python_sdk.type.company_payment_method import CompanyPaymentMethod

from ...api_client import Dictionary
from procurify_python_sdk.pydantic.company_payment_method import CompanyPaymentMethod as CompanyPaymentMethodPydantic
from procurify_python_sdk.pydantic.company_payment_method_request import CompanyPaymentMethodRequest as CompanyPaymentMethodRequestPydantic
from procurify_python_sdk.pydantic.company_payment_method_request_data import CompanyPaymentMethodRequestData as CompanyPaymentMethodRequestDataPydantic
from procurify_python_sdk.pydantic.payment_method_type_enum import PaymentMethodTypeEnum as PaymentMethodTypeEnumPydantic

# Query params


class FormatSchema(
    schemas.EnumBase,
    schemas.StrSchema
):
    
    @schemas.classproperty
    def CSV(cls):
        return cls("csv")
    
    @schemas.classproperty
    def JSON(cls):
        return cls("json")
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'format': typing.Union[FormatSchema, str, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
# body param
SchemaForRequestBodyApplicationJson = CompanyPaymentMethodRequestSchema
SchemaForRequestBodyApplicationXWwwFormUrlencoded = CompanyPaymentMethodRequestSchema
SchemaForRequestBody = CompanyPaymentMethodRequestSchema
SchemaForRequestBodyApplicationXml = CompanyPaymentMethodRequestSchema
SchemaForRequestBodyMultipartFormData = CompanyPaymentMethodRequestSchema


request_body_company_payment_method_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
        'application/x-www-form-urlencoded': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXWwwFormUrlencoded),
        '': api_client.MediaType(
            schema=SchemaForRequestBody),
        'application/xml': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationXml),
        'multipart/form-data': api_client.MediaType(
            schema=SchemaForRequestBodyMultipartFormData),
    },
    required=True,
)
SchemaFor201ResponseBodyApplicationJson = CompanyPaymentMethodSchema
SchemaFor201ResponseBodyTextCsv = CompanyPaymentMethodSchema


@dataclass
class ApiResponseFor201(api_client.ApiResponse):
    body: CompanyPaymentMethod


@dataclass
class ApiResponseFor201Async(api_client.AsyncApiResponse):
    body: CompanyPaymentMethod


_response_for_201 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor201,
    response_cls_async=ApiResponseFor201Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor201ResponseBodyApplicationJson),
        'text/csv': api_client.MediaType(
            schema=SchemaFor201ResponseBodyTextCsv),
    },
)
_all_accept_content_types = (
    'application/json',
    'text/csv',
)


class BaseApi(api_client.Api):

    def _create_company_payment_method_mapped_args(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        _body = {}
        if name is not None:
            _body["name"] = name
        if type is not None:
            _body["type"] = type
        if data is not None:
            _body["data"] = data
        if currency is not None:
            _body["currency"] = currency
        if gl_code is not None:
            _body["gl_code"] = gl_code
        args.body = _body
        if format is not None:
            _query_params["format"] = format
        args.query = _query_params
        return args

    async def _acreate_company_payment_method_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Create Company Payment Method
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/ap/company-payment-methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_company_payment_method_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
            **kwargs
        )
    
        if stream:
            if not 200 <= response.http_response.status <= 299:
                body = (await response.http_response.content.read()).decode("utf-8")
                raise exceptions.ApiStreamingException(
                    status=response.http_response.status,
                    reason=response.http_response.reason,
                    body=body,
                )
    
            async def stream_iterator():
                """
                iterates over response.http_response.content and closes connection once iteration has finished
                """
                async for line in response.http_response.content:
                    if line == b'\r\n':
                        continue
                    yield line
                response.http_response.close()
                await response.session.close()
            return AsyncGeneratorResponse(
                content=stream_iterator(),
                headers=response.http_response.headers,
                status=response.http_response.status,
                response=response.http_response
            )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = await response_for_status.deserialize_async(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserializationAsync(
                body=await response.http_response.json() if is_json else await response.http_response.text(),
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        # cleanup session / response
        response.http_response.close()
        await response.session.close()
    
        return api_response


    def _create_company_payment_method_oapg(
        self,
        body: typing.Any = None,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Create Company Payment Method
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_format,
        ):
            parameter_data = query_params.get(parameter.name, schemas.unset)
            if parameter_data is schemas.unset:
                continue
            if prefix_separator_iterator is None:
                prefix_separator_iterator = parameter.get_prefix_separator_iterator()
            serialized_data = parameter.serialize(parameter_data, prefix_separator_iterator)
            for serialized_value in serialized_data.values():
                used_path += serialized_value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        if body is schemas.unset:
            raise exceptions.ApiValueError(
                'The required body parameter has an invalid value of: unset. Set a valid value instead')
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/ap/company-payment-methods',
            body=body,
            auth_settings=_auth,
            headers=_headers,
        )
        serialized_data = request_body_company_payment_method_request.serialize(body, content_type)
        if 'fields' in serialized_data:
            _fields = serialized_data['fields']
        elif 'body' in serialized_data:
            _body = serialized_data['body']
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            auth_settings=_auth,
            prefix_separator_iterator=prefix_separator_iterator,
            timeout=timeout,
        )
    
        response_for_status = _status_code_to_response.get(str(response.http_response.status))
        if response_for_status:
            api_response = response_for_status.deserialize(
                                                    response,
                                                    self.api_client.configuration,
                                                    skip_deserialization=skip_deserialization
                                                )
        else:
            # If response data is JSON then deserialize for SDK consumer convenience
            is_json = api_client.JSONDetector._content_type_is_json(response.http_response.headers.get('Content-Type', ''))
            api_response = api_client.ApiResponseWithoutDeserialization(
                body=json.loads(response.http_response.data) if is_json else response.http_response.data,
                response=response.http_response,
                round_trip_time=response.round_trip_time,
                status=response.http_response.status,
                headers=response.http_response.headers,
            )
    
        if not 200 <= api_response.status <= 299:
            raise exceptions.ApiException(api_response=api_response)
    
        return api_response


class CreateCompanyPaymentMethodRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acreate_company_payment_method(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_company_payment_method_mapped_args(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
        )
        return await self._acreate_company_payment_method_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def create_company_payment_method(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_company_payment_method_mapped_args(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
        )
        return self._create_company_payment_method_oapg(
            body=args.body,
            query_params=args.query,
        )

class CreateCompanyPaymentMethod(BaseApi):

    async def acreate_company_payment_method(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> CompanyPaymentMethodPydantic:
        raw_response = await self.raw.acreate_company_payment_method(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
            **kwargs,
        )
        if validate:
            return CompanyPaymentMethodPydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyPaymentMethodPydantic, raw_response.body)
    
    
    def create_company_payment_method(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        validate: bool = False,
    ) -> CompanyPaymentMethodPydantic:
        raw_response = self.raw.create_company_payment_method(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
        )
        if validate:
            return CompanyPaymentMethodPydantic(**raw_response.body)
        return api_client.construct_model_instance(CompanyPaymentMethodPydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor201Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._create_company_payment_method_mapped_args(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
        )
        return await self._acreate_company_payment_method_oapg(
            body=args.body,
            query_params=args.query,
            **kwargs,
        )
    
    def post(
        self,
        data: CompanyPaymentMethodRequestData,
        name: typing.Optional[str] = None,
        type: typing.Optional[PaymentMethodTypeEnum] = None,
        currency: typing.Optional[int] = None,
        gl_code: typing.Optional[str] = None,
        format: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor201,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._create_company_payment_method_mapped_args(
            data=data,
            name=name,
            type=type,
            currency=currency,
            gl_code=gl_code,
            format=format,
        )
        return self._create_company_payment_method_oapg(
            body=args.body,
            query_params=args.query,
        )

