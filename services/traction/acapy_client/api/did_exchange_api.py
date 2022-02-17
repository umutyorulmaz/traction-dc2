"""
    Aries Cloud Agent

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

    The version of the OpenAPI document: v0.7.2
    Generated by: https://openapi-generator.tech
"""


import re  # noqa: F401
import sys  # noqa: F401

from acapy_client.api_client import ApiClient, Endpoint as _Endpoint
from acapy_client.model_utils import (  # noqa: F401
    check_allowed_values,
    check_validations,
    date,
    datetime,
    file_type,
    none_type,
    validate_and_convert_types,
)
from acapy_client.model.conn_record import ConnRecord
from acapy_client.model.didx_request import DIDXRequest


class DidExchangeApi(object):
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client
        self.didexchange_conn_id_accept_invitation_post_endpoint = _Endpoint(
            settings={
                "response_type": (ConnRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/didexchange/{conn_id}/accept-invitation",
                "operation_id": "didexchange_conn_id_accept_invitation_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "conn_id",
                    "my_endpoint",
                    "my_label",
                ],
                "required": [
                    "conn_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "my_endpoint",
                ],
            },
            root_map={
                "validations": {
                    ("my_endpoint",): {
                        "regex": {
                            "pattern": r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "conn_id": (str,),
                    "my_endpoint": (str,),
                    "my_label": (str,),
                },
                "attribute_map": {
                    "conn_id": "conn_id",
                    "my_endpoint": "my_endpoint",
                    "my_label": "my_label",
                },
                "location_map": {
                    "conn_id": "path",
                    "my_endpoint": "query",
                    "my_label": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.didexchange_conn_id_accept_request_post_endpoint = _Endpoint(
            settings={
                "response_type": (ConnRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/didexchange/{conn_id}/accept-request",
                "operation_id": "didexchange_conn_id_accept_request_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "conn_id",
                    "mediation_id",
                    "my_endpoint",
                ],
                "required": [
                    "conn_id",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "my_endpoint",
                ],
            },
            root_map={
                "validations": {
                    ("my_endpoint",): {
                        "regex": {
                            "pattern": r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "conn_id": (str,),
                    "mediation_id": (str,),
                    "my_endpoint": (str,),
                },
                "attribute_map": {
                    "conn_id": "conn_id",
                    "mediation_id": "mediation_id",
                    "my_endpoint": "my_endpoint",
                },
                "location_map": {
                    "conn_id": "path",
                    "mediation_id": "query",
                    "my_endpoint": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.didexchange_create_request_post_endpoint = _Endpoint(
            settings={
                "response_type": (ConnRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/didexchange/create-request",
                "operation_id": "didexchange_create_request_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "their_public_did",
                    "alias",
                    "mediation_id",
                    "my_endpoint",
                    "my_label",
                    "use_public_did",
                ],
                "required": [
                    "their_public_did",
                ],
                "nullable": [],
                "enum": [],
                "validation": [
                    "their_public_did",
                    "my_endpoint",
                ],
            },
            root_map={
                "validations": {
                    ("their_public_did",): {
                        "regex": {
                            "pattern": r"^(did:sov:)?[123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz]{21,22}$|^did:([a-zA-Z0-9_]+):([a-zA-Z0-9_.%-]+(:[a-zA-Z0-9_.%-]+)*)((;[a-zA-Z0-9_.:%-]+=[a-zA-Z0-9_.:%-]*)*)(\/[^#?]*)?([?][^#]*)?(\#.*)?$$",  # noqa: E501
                        },
                    },
                    ("my_endpoint",): {
                        "regex": {
                            "pattern": r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "their_public_did": (str,),
                    "alias": (str,),
                    "mediation_id": (str,),
                    "my_endpoint": (str,),
                    "my_label": (str,),
                    "use_public_did": (bool,),
                },
                "attribute_map": {
                    "their_public_did": "their_public_did",
                    "alias": "alias",
                    "mediation_id": "mediation_id",
                    "my_endpoint": "my_endpoint",
                    "my_label": "my_label",
                    "use_public_did": "use_public_did",
                },
                "location_map": {
                    "their_public_did": "query",
                    "alias": "query",
                    "mediation_id": "query",
                    "my_endpoint": "query",
                    "my_label": "query",
                    "use_public_did": "query",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )
        self.didexchange_receive_request_post_endpoint = _Endpoint(
            settings={
                "response_type": (ConnRecord,),
                "auth": ["AuthorizationHeader"],
                "endpoint_path": "/didexchange/receive-request",
                "operation_id": "didexchange_receive_request_post",
                "http_method": "POST",
                "servers": None,
            },
            params_map={
                "all": [
                    "alias",
                    "auto_accept",
                    "mediation_id",
                    "my_endpoint",
                    "body",
                ],
                "required": [],
                "nullable": [],
                "enum": [],
                "validation": [
                    "my_endpoint",
                ],
            },
            root_map={
                "validations": {
                    ("my_endpoint",): {
                        "regex": {
                            "pattern": r"^[A-Za-z0-9\.\-\+]+:\/\/([A-Za-z0-9][.A-Za-z0-9-_]+[A-Za-z0-9])+(:[1-9][0-9]*)?(\/[^?&#]+)?$",  # noqa: E501
                        },
                    },
                },
                "allowed_values": {},
                "openapi_types": {
                    "alias": (str,),
                    "auto_accept": (bool,),
                    "mediation_id": (str,),
                    "my_endpoint": (str,),
                    "body": (DIDXRequest,),
                },
                "attribute_map": {
                    "alias": "alias",
                    "auto_accept": "auto_accept",
                    "mediation_id": "mediation_id",
                    "my_endpoint": "my_endpoint",
                },
                "location_map": {
                    "alias": "query",
                    "auto_accept": "query",
                    "mediation_id": "query",
                    "my_endpoint": "query",
                    "body": "body",
                },
                "collection_format_map": {},
            },
            headers_map={
                "accept": ["application/json"],
                "content_type": [],
            },
            api_client=api_client,
        )

    def didexchange_conn_id_accept_invitation_post(self, conn_id, **kwargs):
        """Accept a stored connection invitation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.didexchange_conn_id_accept_invitation_post(conn_id, async_req=True)
        >>> result = thread.get()

        Args:
            conn_id (str): Connection identifier

        Keyword Args:
            my_endpoint (str): My URL endpoint. [optional]
            my_label (str): Label for connection request. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConnRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["conn_id"] = conn_id
        return self.didexchange_conn_id_accept_invitation_post_endpoint.call_with_http_info(
            **kwargs
        )

    def didexchange_conn_id_accept_request_post(self, conn_id, **kwargs):
        """Accept a stored connection request  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.didexchange_conn_id_accept_request_post(conn_id, async_req=True)
        >>> result = thread.get()

        Args:
            conn_id (str): Connection identifier

        Keyword Args:
            mediation_id (str): Identifier for active mediation record to be used. [optional]
            my_endpoint (str): My URL endpoint. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConnRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["conn_id"] = conn_id
        return (
            self.didexchange_conn_id_accept_request_post_endpoint.call_with_http_info(
                **kwargs
            )
        )

    def didexchange_create_request_post(self, their_public_did, **kwargs):
        """Create and send a request against public DID's implicit invitation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.didexchange_create_request_post(their_public_did, async_req=True)
        >>> result = thread.get()

        Args:
            their_public_did (str): Qualified public DID to which to request connection

        Keyword Args:
            alias (atr): Alias to apply to this connection [optional]
            mediation_id (str): Identifier for active mediation record to be used. [optional]
            my_endpoint (str): My URL endpoint. [optional]
            my_label (str): Label for connection request. [optional]
            use_public_did (bool): Use public DID for this connection. [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConnRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        kwargs["their_public_did"] = their_public_did
        return self.didexchange_create_request_post_endpoint.call_with_http_info(
            **kwargs
        )

    def didexchange_receive_request_post(self, **kwargs):
        """Receive request against public DID's implicit invitation  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True

        >>> thread = api.didexchange_receive_request_post(async_req=True)
        >>> result = thread.get()


        Keyword Args:
            alias (str): Alias for connection. [optional]
            auto_accept (bool): Auto-accept connection (defaults to configuration). [optional]
            mediation_id (str): Identifier for active mediation record to be used. [optional]
            my_endpoint (str): My URL endpoint. [optional]
            body (DIDXRequest): [optional]
            _return_http_data_only (bool): response data without head status
                code and headers. Default is True.
            _preload_content (bool): if False, the urllib3.HTTPResponse object
                will be returned without reading/decoding response data.
                Default is True.
            _request_timeout (int/float/tuple): timeout setting for this request. If
                one number provided, it will be total request timeout. It can also
                be a pair (tuple) of (connection, read) timeouts.
                Default is None.
            _check_input_type (bool): specifies if type checking
                should be done one the data sent to the server.
                Default is True.
            _check_return_type (bool): specifies if type checking
                should be done one the data received from the server.
                Default is True.
            _spec_property_naming (bool): True if the variable names in the input data
                are serialized names, as specified in the OpenAPI document.
                False if the variable names in the input data
                are pythonic names, e.g. snake case (default)
            _content_type (str/None): force body content-type.
                Default is None and content-type will be predicted by allowed
                content-types and body.
            _host_index (int/None): specifies the index of the server
                that we want to use.
                Default is read from the configuration.
            async_req (bool): execute request asynchronously

        Returns:
            ConnRecord
                If the method is called asynchronously, returns the request
                thread.
        """
        kwargs["async_req"] = kwargs.get("async_req", False)
        kwargs["_return_http_data_only"] = kwargs.get("_return_http_data_only", True)
        kwargs["_preload_content"] = kwargs.get("_preload_content", True)
        kwargs["_request_timeout"] = kwargs.get("_request_timeout", None)
        kwargs["_check_input_type"] = kwargs.get("_check_input_type", True)
        kwargs["_check_return_type"] = kwargs.get("_check_return_type", True)
        kwargs["_spec_property_naming"] = kwargs.get("_spec_property_naming", False)
        kwargs["_content_type"] = kwargs.get("_content_type")
        kwargs["_host_index"] = kwargs.get("_host_index")
        return self.didexchange_receive_request_post_endpoint.call_with_http_info(
            **kwargs
        )