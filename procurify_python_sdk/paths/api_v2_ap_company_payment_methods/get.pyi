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

from procurify_python_sdk.model.paginated_company_payment_method_read_list import PaginatedCompanyPaymentMethodReadList as PaginatedCompanyPaymentMethodReadListSchema

from procurify_python_sdk.type.paginated_company_payment_method_read_list import PaginatedCompanyPaymentMethodReadList

from ...api_client import Dictionary
from procurify_python_sdk.pydantic.paginated_company_payment_method_read_list import PaginatedCompanyPaymentMethodReadList as PaginatedCompanyPaymentMethodReadListPydantic

# Query params
CurrencySchema = schemas.IntSchema


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
OrderBySchema = schemas.StrSchema
PageSchema = schemas.IntSchema
PageSizeSchema = schemas.IntSchema
SearchSchema = schemas.StrSchema


class TypeSchema(
    schemas.EnumBase,
    schemas.IntSchema
):
    
    @schemas.classproperty
    def POSITIVE_0(cls):
        return cls(0)
    
    @schemas.classproperty
    def POSITIVE_1(cls):
        return cls(1)
    
    @schemas.classproperty
    def POSITIVE_2(cls):
        return cls(2)
    
    @schemas.classproperty
    def POSITIVE_3(cls):
        return cls(3)
    
    @schemas.classproperty
    def POSITIVE_4(cls):
        return cls(4)
RequestRequiredQueryParams = typing_extensions.TypedDict(
    'RequestRequiredQueryParams',
    {
    }
)
RequestOptionalQueryParams = typing_extensions.TypedDict(
    'RequestOptionalQueryParams',
    {
        'currency': typing.Union[CurrencySchema, decimal.Decimal, int, ],
        'format': typing.Union[FormatSchema, str, ],
        'order_by': typing.Union[OrderBySchema, str, ],
        'page': typing.Union[PageSchema, decimal.Decimal, int, ],
        'page_size': typing.Union[PageSizeSchema, decimal.Decimal, int, ],
        'search': typing.Union[SearchSchema, str, ],
        'type': typing.Union[TypeSchema, decimal.Decimal, int, ],
    },
    total=False
)


class RequestQueryParams(RequestRequiredQueryParams, RequestOptionalQueryParams):
    pass


request_query_currency = api_client.QueryParameter(
    name="currency",
    style=api_client.ParameterStyle.FORM,
    schema=CurrencySchema,
    explode=True,
)
request_query_format = api_client.QueryParameter(
    name="format",
    style=api_client.ParameterStyle.FORM,
    schema=FormatSchema,
    explode=True,
)
request_query_order_by = api_client.QueryParameter(
    name="order_by",
    style=api_client.ParameterStyle.FORM,
    schema=OrderBySchema,
    explode=True,
)
request_query_page = api_client.QueryParameter(
    name="page",
    style=api_client.ParameterStyle.FORM,
    schema=PageSchema,
    explode=True,
)
request_query_page_size = api_client.QueryParameter(
    name="page_size",
    style=api_client.ParameterStyle.FORM,
    schema=PageSizeSchema,
    explode=True,
)
request_query_search = api_client.QueryParameter(
    name="search",
    style=api_client.ParameterStyle.FORM,
    schema=SearchSchema,
    explode=True,
)
request_query_type = api_client.QueryParameter(
    name="type",
    style=api_client.ParameterStyle.FORM,
    schema=TypeSchema,
    explode=True,
)
SchemaFor200ResponseBodyApplicationJson = PaginatedCompanyPaymentMethodReadListSchema
SchemaFor200ResponseBodyTextCsv = PaginatedCompanyPaymentMethodReadListSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: PaginatedCompanyPaymentMethodReadList


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: PaginatedCompanyPaymentMethodReadList


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
        'text/csv': api_client.MediaType(
            schema=SchemaFor200ResponseBodyTextCsv),
    },
)
_all_accept_content_types = (
    'application/json',
    'text/csv',
)


class BaseApi(api_client.Api):

    def _company_payment_methods_list_mapped_args(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _query_params = {}
        if currency is not None:
            _query_params["currency"] = currency
        if format is not None:
            _query_params["format"] = format
        if order_by is not None:
            _query_params["order_by"] = order_by
        if page is not None:
            _query_params["page"] = page
        if page_size is not None:
            _query_params["page_size"] = page_size
        if search is not None:
            _query_params["search"] = search
        if type is not None:
            _query_params["type"] = type
        args.query = _query_params
        return args

    async def _acompany_payment_methods_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Get list of Company Payment Methods
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_currency,
            request_query_format,
            request_query_order_by,
            request_query_page,
            request_query_page_size,
            request_query_search,
            request_query_type,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/ap/company-payment-methods',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


    def _company_payment_methods_list_oapg(
        self,
            query_params: typing.Optional[dict] = {},
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Get list of Company Payment Methods
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        self._verify_typed_dict_inputs_oapg(RequestQueryParams, query_params)
        used_path = path.value
    
        prefix_separator_iterator = None
        for parameter in (
            request_query_currency,
            request_query_format,
            request_query_order_by,
            request_query_page,
            request_query_page_size,
            request_query_search,
            request_query_type,
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
        method = 'get'.upper()
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/api/v2/ap/company-payment-methods',
            auth_settings=_auth,
            headers=_headers,
        )
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
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


class CompanyPaymentMethodsListRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def acompany_payment_methods_list(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._company_payment_methods_list_mapped_args(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
        )
        return await self._acompany_payment_methods_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def company_payment_methods_list(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._company_payment_methods_list_mapped_args(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
        )
        return self._company_payment_methods_list_oapg(
            query_params=args.query,
        )

class CompanyPaymentMethodsList(BaseApi):

    async def acompany_payment_methods_list(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
        validate: bool = False,
        **kwargs,
    ) -> PaginatedCompanyPaymentMethodReadListPydantic:
        raw_response = await self.raw.acompany_payment_methods_list(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
            **kwargs,
        )
        if validate:
            return PaginatedCompanyPaymentMethodReadListPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedCompanyPaymentMethodReadListPydantic, raw_response.body)
    
    
    def company_payment_methods_list(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
        validate: bool = False,
    ) -> PaginatedCompanyPaymentMethodReadListPydantic:
        raw_response = self.raw.company_payment_methods_list(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
        )
        if validate:
            return PaginatedCompanyPaymentMethodReadListPydantic(**raw_response.body)
        return api_client.construct_model_instance(PaginatedCompanyPaymentMethodReadListPydantic, raw_response.body)


class ApiForget(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def aget(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._company_payment_methods_list_mapped_args(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
        )
        return await self._acompany_payment_methods_list_oapg(
            query_params=args.query,
            **kwargs,
        )
    
    def get(
        self,
        currency: typing.Optional[int] = None,
        format: typing.Optional[str] = None,
        order_by: typing.Optional[str] = None,
        page: typing.Optional[int] = None,
        page_size: typing.Optional[int] = None,
        search: typing.Optional[str] = None,
        type: typing.Optional[int] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._company_payment_methods_list_mapped_args(
            currency=currency,
            format=format,
            order_by=order_by,
            page=page,
            page_size=page_size,
            search=search,
            type=type,
        )
        return self._company_payment_methods_list_oapg(
            query_params=args.query,
        )

