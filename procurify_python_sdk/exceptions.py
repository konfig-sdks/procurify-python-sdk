# coding: utf-8

"""
    Procurify API Documentation

     # Disclaimer  - Procurify’s API is evolving and is subject to change at any time. Additionally, aspects of the API are undocumented, including certain methods, events, and properties. Given that both documented and undocumented aspects of the Procurify API may change at any time, the client relies on the API at their own risk. - Client (and/or client’s representative) is responsible for building, testing, and maintaining any API connection between Procurify and any other tool.  Procurify’s responsibility strictly involves providing support on clarifications in regards to the issued API document. - Procurify’s API is offered on an “as is” and “as available” basis, without warranties of any kind. By accepting this agreement, you agree that you have read the current API documentation, and accept the API functionality in its current state including current limitations. For questions and clarification around the documentation, please contact support@procurify.com. - In accordance with Section 2.(b) of our Subscription Services Agreement, Procurify reserves the right to deny access to our API at any time. If your API requests are too large and time out, contact us immediately to avoid possible suspension of access. - You may not attempt to reverse engineer or otherwise derive source code, trade secrets, or know-how in the Procurify API or portion thereof. You may not use the Procurify API to replicate or compete with core products or services offered by Procurify. 

    Generated by: https://konfigthis.com
"""


import typing
from procurify_python_sdk.api_response import ApiResponse, AsyncApiResponse
from procurify_python_sdk.exceptions_base import OpenApiException, ApiTypeError, ApiValueError, render_path

class ClientConfigurationError(OpenApiException):
    def __init__(self, msg):
        super(ClientConfigurationError, self).__init__(msg)


class ApiAttributeError(OpenApiException, AttributeError):
    def __init__(self, msg, path_to_item=None):
        """
        Raised when an attribute reference or assignment fails.

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiAttributeError, self).__init__(full_msg)


class ApiKeyError(OpenApiException, KeyError):
    def __init__(self, msg, path_to_item=None):
        """
        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (None/list) the path to the exception in the
                received_data dict
        """
        self.path_to_item = path_to_item
        full_msg = msg
        if path_to_item:
            full_msg = "{0} at {1}".format(msg, render_path(path_to_item))
        super(ApiKeyError, self).__init__(full_msg)


class ApiStreamingException(OpenApiException):

    def __init__(self, status=None, reason=None, body=None):
        self.status = status
        self.reason = reason
        self.body = body

    def __str__(self):
        """Custom error messages for exception"""
        return "({0})\n Reason: {1}\n Body: {2}".format(self.status, self.reason, self.body)


class ApiException(OpenApiException):

    def __init__(self, status=None, reason=None, api_response: typing.Optional[typing.Union[ApiResponse, AsyncApiResponse]] = None):
        if api_response:
            self.status = api_response.status
            self.reason = api_response.response.reason
            self.body = api_response.body
            self.headers = api_response.response.headers
            self.round_trip_time = api_response.round_trip_time
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None
            self.round_trip_time = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n"\
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message


class AnyOfValidationError(OpenApiException):
    def __init__(self, error_list: typing.List[typing.Union[ApiTypeError, ApiValueError]]):
        self.error_list = error_list
        sub_msgs: typing.List[str] = []
        for type_error in error_list:
            sub_msgs.append(str(type_error))
        num_validation_errors = len(self.error_list)
        if num_validation_errors == 1:
            super().__init__(sub_msgs[0])
        else:
            # create a string that says how many validation errors there were and
            # prints each sub_msg out using a bulleted list of messages
            msg = "{} validation error{} detected: \n".format(num_validation_errors, "s" if num_validation_errors > 1 else "")
            for i, sub_msg in enumerate(sub_msgs):
                msg += " {}. {}\n".format(i+1, sub_msg)
            super().__init__(msg)


class InvalidHostConfigurationError(ClientConfigurationError):
    def __init__(self, host: str, reason: str):
        self.host = host
        self.reason = reason
        super().__init__('Invalid host: "{}", {}'.format(self.host, self.reason))


class MissingRequiredPropertiesError(ApiTypeError):
    def __init__(self, msg: str):
        super().__init__(msg)


class MissingRequiredParametersError(ApiTypeError):
    def __init__(self, error: TypeError):
        self.error = error
        error_str = str(error)
        self.msg = error_str
        if "__new__()" in error_str:
            # parse error to reformat
            missing_parameters = error_str.split(":")[1].strip()
            number_of_parameters = error_str.split("missing")[1].split("required")[0].strip()
            self.msg = "Missing {} required parameter{}: {}".format(number_of_parameters, "s" if int(number_of_parameters) > 1 else "", missing_parameters)
        super().__init__(self.msg)

class SchemaValidationError(OpenApiException):
    def __init__(self, validation_errors: typing.List[typing.Union[ApiValueError, ApiTypeError]]):
        """ Aggregates schema validation errors

        Args:
            msg (str): the exception message

        Keyword Args:
            path_to_item (list): a list of keys an indices to get to the
                                 current_item
                                 None if unset
            valid_classes (tuple): the primitive classes that current item
                                   should be an instance of
                                   None if unset
            key_type (bool): False if our value is a value in a dict
                             True if it is a key in a dict
                             False if our item is an item in a list
                             None if unset
        """
        self.validation_errors = validation_errors
        self.type_errors: typing.List[ApiTypeError] = []
        self.value_errors: typing.List[ApiValueError] = []
        self.missing_required_properties_errors: typing.List[MissingRequiredPropertiesError] = []
        for error in validation_errors:
            if isinstance(error, ApiTypeError):
                self.type_errors.append(error)
            elif isinstance(error, ApiValueError):
                self.value_errors.append(error)
            elif isinstance(error, MissingRequiredPropertiesError):
                self.missing_required_properties_errors.append(error)
        sub_msgs: typing.List[str] = []
        if len(self.missing_required_properties_errors) > 0:
            for error in self.missing_required_properties_errors:
                sub_msgs.append(str(error))
        if len(self.type_errors) > 0:
            for type_error in self.type_errors:
                if isinstance(type_error, MissingRequiredPropertiesError) or isinstance(type_error, MissingRequiredParametersError):
                    sub_msgs.append(str(type_error))
                else:
                    classes = ", ".join([cls.__name__ for cls in type_error.valid_classes])
                    msg = 'Got {}({}) for required type {} at {}'.format(
                        type(type_error.invalid_value).__name__, type_error.invalid_value, classes, render_path(type_error.path_to_item))
                    sub_msgs.append(msg)
        if len(self.value_errors) > 0:
            for value_error in self.value_errors:
                sub_msgs.append(value_error.full_msg)
        sub_msg = ". ".join(sub_msgs)
        num_validation_errors = len(self.validation_errors)
        self.msg = "{} invalid argument{}. {}".format(num_validation_errors, "s" if num_validation_errors > 1 else "", sub_msg)
        super().__init__(self.msg)
