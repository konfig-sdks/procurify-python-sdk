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

from procurify_python_sdk.model.oauth_token_request_response import OauthTokenRequestResponse as OauthTokenRequestResponseSchema
from procurify_python_sdk.model.oauth_token_request_request import OauthTokenRequestRequest as OauthTokenRequestRequestSchema

from procurify_python_sdk.type.oauth_token_request_response import OauthTokenRequestResponse
from procurify_python_sdk.type.oauth_token_request_request import OauthTokenRequestRequest

from ...api_client import Dictionary
from procurify_python_sdk.pydantic.oauth_token_request_response import OauthTokenRequestResponse as OauthTokenRequestResponsePydantic
from procurify_python_sdk.pydantic.oauth_token_request_request import OauthTokenRequestRequest as OauthTokenRequestRequestPydantic

# body param
SchemaForRequestBodyApplicationJson = OauthTokenRequestRequestSchema


request_body_oauth_token_request_request = api_client.RequestBody(
    content={
        'application/json': api_client.MediaType(
            schema=SchemaForRequestBodyApplicationJson),
    },
)
SchemaFor200ResponseBodyApplicationJson = OauthTokenRequestResponseSchema


@dataclass
class ApiResponseFor200(api_client.ApiResponse):
    body: OauthTokenRequestResponse


@dataclass
class ApiResponseFor200Async(api_client.AsyncApiResponse):
    body: OauthTokenRequestResponse


_response_for_200 = api_client.OpenApiResponse(
    response_cls=ApiResponseFor200,
    response_cls_async=ApiResponseFor200Async,
    content={
        'application/json': api_client.MediaType(
            schema=SchemaFor200ResponseBodyApplicationJson),
    },
)
_all_accept_content_types = (
    'application/json',
)


class BaseApi(api_client.Api):

    def _token_request_mapped_args(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
    ) -> api_client.MappedArgs:
        args: api_client.MappedArgs = api_client.MappedArgs()
        _body = {}
        if client_id is not None:
            _body["client_id"] = client_id
        if client_secret is not None:
            _body["client_secret"] = client_secret
        if audience is not None:
            _body["audience"] = audience
        if grant_type is not None:
            _body["grant_type"] = grant_type
        args.body = _body
        return args

    async def _atoken_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        """
        Authenticate with OAuth
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/oauth/token',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_oauth_token_request_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('token_request', _servers, host_index)
    
        response = await self.api_client.async_call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            host=host,
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


    def _token_request_oapg(
        self,
        body: typing.Any = None,
        skip_deserialization: bool = True,
        timeout: typing.Optional[typing.Union[float, typing.Tuple]] = None,
        accept_content_types: typing.Tuple[str] = _all_accept_content_types,
        content_type: str = 'application/json',
        stream: bool = False,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        """
        Authenticate with OAuth
        :param skip_deserialization: If true then api_response.response will be set but
            api_response.body and api_response.headers will not be deserialized into schema
            class instances
        """
        used_path = path.value
    
        _headers = HTTPHeaderDict()
        # TODO add cookie handling
        if accept_content_types:
            for accept_content_type in accept_content_types:
                _headers.add('Accept', accept_content_type)
        method = 'post'.upper()
        _headers.add('Content-Type', content_type)
    
        _fields = None
        _body = None
        request_before_hook(
            resource_path=used_path,
            method=method,
            configuration=self.api_client.configuration,
            path_template='/oauth/token',
            body=body,
            headers=_headers,
        )
        if body is not schemas.unset:
            serialized_data = request_body_oauth_token_request_request.serialize(body, content_type)
            if 'fields' in serialized_data:
                _fields = serialized_data['fields']
            elif 'body' in serialized_data:
                _body = serialized_data['body']
    
        host = self._get_host_oapg('token_request', _servers, host_index)
    
        response = self.api_client.call_api(
            resource_path=used_path,
            method=method,
            headers=_headers,
            fields=_fields,
            serialized_body=_body,
            body=body,
            host=host,
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


class TokenRequestRaw(BaseApi):
    # this class is used by api classes that refer to endpoints with operationId fn names

    async def atoken_request(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._token_request_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )
        return await self._atoken_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def token_request(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._token_request_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )
        return self._token_request_oapg(
            body=args.body,
        )

class TokenRequest(BaseApi):

    async def atoken_request(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
        validate: bool = False,
        **kwargs,
    ) -> OauthTokenRequestResponsePydantic:
        raw_response = await self.raw.atoken_request(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
            **kwargs,
        )
        if validate:
            return OauthTokenRequestResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OauthTokenRequestResponsePydantic, raw_response.body)
    
    
    def token_request(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
        validate: bool = False,
    ) -> OauthTokenRequestResponsePydantic:
        raw_response = self.raw.token_request(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )
        if validate:
            return OauthTokenRequestResponsePydantic(**raw_response.body)
        return api_client.construct_model_instance(OauthTokenRequestResponsePydantic, raw_response.body)


class ApiForpost(BaseApi):
    # this class is used by api classes that refer to endpoints by path and http method names

    async def apost(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
        **kwargs,
    ) -> typing.Union[
        ApiResponseFor200Async,
        api_client.ApiResponseWithoutDeserializationAsync,
        AsyncGeneratorResponse,
    ]:
        args = self._token_request_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )
        return await self._atoken_request_oapg(
            body=args.body,
            **kwargs,
        )
    
    def post(
        self,
        client_id: typing.Optional[str] = None,
        client_secret: typing.Optional[str] = None,
        audience: typing.Optional[str] = None,
        grant_type: typing.Optional[str] = None,
    ) -> typing.Union[
        ApiResponseFor200,
        api_client.ApiResponseWithoutDeserialization,
    ]:
        args = self._token_request_mapped_args(
            client_id=client_id,
            client_secret=client_secret,
            audience=audience,
            grant_type=grant_type,
        )
        return self._token_request_oapg(
            body=args.body,
        )

