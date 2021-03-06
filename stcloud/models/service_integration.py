# coding: utf-8

"""
    Sematext Cloud API

    API Explorer provides access and documentation for Sematext REST API. The REST API requires the API Key to be sent as part of `Authorization` header. E.g.: `Authorization : apiKey e5f18450-205a-48eb-8589-7d49edaea813`.  # noqa: E501

    OpenAPI spec version: v3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class ServiceIntegration(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'app_type_id': 'int',
        'app_type_name': 'str',
        'display_name': 'str',
        'enabled': 'bool',
        'external_product_id': 'int',
        'external_product_name': 'str',
        'id': 'int',
        'integration_type': 'str',
        'ordinal': 'int',
        'parent_integration_id': 'int',
        'sematext_service': 'str',
        'visible': 'bool'
    }

    attribute_map = {
        'app_type_id': 'appTypeId',
        'app_type_name': 'appTypeName',
        'display_name': 'displayName',
        'enabled': 'enabled',
        'external_product_id': 'externalProductId',
        'external_product_name': 'externalProductName',
        'id': 'id',
        'integration_type': 'integrationType',
        'ordinal': 'ordinal',
        'parent_integration_id': 'parentIntegrationId',
        'sematext_service': 'sematextService',
        'visible': 'visible'
    }

    def __init__(self, app_type_id=None, app_type_name=None, display_name=None, enabled=None, external_product_id=None, external_product_name=None, id=None, integration_type=None, ordinal=None, parent_integration_id=None, sematext_service=None, visible=None):  # noqa: E501
        """ServiceIntegration - a model defined in Swagger"""  # noqa: E501
        self._app_type_id = None
        self._app_type_name = None
        self._display_name = None
        self._enabled = None
        self._external_product_id = None
        self._external_product_name = None
        self._id = None
        self._integration_type = None
        self._ordinal = None
        self._parent_integration_id = None
        self._sematext_service = None
        self._visible = None
        self.discriminator = None
        if app_type_id is not None:
            self.app_type_id = app_type_id
        if app_type_name is not None:
            self.app_type_name = app_type_name
        if display_name is not None:
            self.display_name = display_name
        if enabled is not None:
            self.enabled = enabled
        if external_product_id is not None:
            self.external_product_id = external_product_id
        if external_product_name is not None:
            self.external_product_name = external_product_name
        if id is not None:
            self.id = id
        if integration_type is not None:
            self.integration_type = integration_type
        if ordinal is not None:
            self.ordinal = ordinal
        if parent_integration_id is not None:
            self.parent_integration_id = parent_integration_id
        if sematext_service is not None:
            self.sematext_service = sematext_service
        if visible is not None:
            self.visible = visible

    @property
    def app_type_id(self):
        """Gets the app_type_id of this ServiceIntegration.  # noqa: E501


        :return: The app_type_id of this ServiceIntegration.  # noqa: E501
        :rtype: int
        """
        return self._app_type_id

    @app_type_id.setter
    def app_type_id(self, app_type_id):
        """Sets the app_type_id of this ServiceIntegration.


        :param app_type_id: The app_type_id of this ServiceIntegration.  # noqa: E501
        :type: int
        """

        self._app_type_id = app_type_id

    @property
    def app_type_name(self):
        """Gets the app_type_name of this ServiceIntegration.  # noqa: E501


        :return: The app_type_name of this ServiceIntegration.  # noqa: E501
        :rtype: str
        """
        return self._app_type_name

    @app_type_name.setter
    def app_type_name(self, app_type_name):
        """Sets the app_type_name of this ServiceIntegration.


        :param app_type_name: The app_type_name of this ServiceIntegration.  # noqa: E501
        :type: str
        """

        self._app_type_name = app_type_name

    @property
    def display_name(self):
        """Gets the display_name of this ServiceIntegration.  # noqa: E501


        :return: The display_name of this ServiceIntegration.  # noqa: E501
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this ServiceIntegration.


        :param display_name: The display_name of this ServiceIntegration.  # noqa: E501
        :type: str
        """

        self._display_name = display_name

    @property
    def enabled(self):
        """Gets the enabled of this ServiceIntegration.  # noqa: E501


        :return: The enabled of this ServiceIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._enabled

    @enabled.setter
    def enabled(self, enabled):
        """Sets the enabled of this ServiceIntegration.


        :param enabled: The enabled of this ServiceIntegration.  # noqa: E501
        :type: bool
        """

        self._enabled = enabled

    @property
    def external_product_id(self):
        """Gets the external_product_id of this ServiceIntegration.  # noqa: E501


        :return: The external_product_id of this ServiceIntegration.  # noqa: E501
        :rtype: int
        """
        return self._external_product_id

    @external_product_id.setter
    def external_product_id(self, external_product_id):
        """Sets the external_product_id of this ServiceIntegration.


        :param external_product_id: The external_product_id of this ServiceIntegration.  # noqa: E501
        :type: int
        """

        self._external_product_id = external_product_id

    @property
    def external_product_name(self):
        """Gets the external_product_name of this ServiceIntegration.  # noqa: E501


        :return: The external_product_name of this ServiceIntegration.  # noqa: E501
        :rtype: str
        """
        return self._external_product_name

    @external_product_name.setter
    def external_product_name(self, external_product_name):
        """Sets the external_product_name of this ServiceIntegration.


        :param external_product_name: The external_product_name of this ServiceIntegration.  # noqa: E501
        :type: str
        """

        self._external_product_name = external_product_name

    @property
    def id(self):
        """Gets the id of this ServiceIntegration.  # noqa: E501


        :return: The id of this ServiceIntegration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServiceIntegration.


        :param id: The id of this ServiceIntegration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def integration_type(self):
        """Gets the integration_type of this ServiceIntegration.  # noqa: E501


        :return: The integration_type of this ServiceIntegration.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this ServiceIntegration.


        :param integration_type: The integration_type of this ServiceIntegration.  # noqa: E501
        :type: str
        """

        self._integration_type = integration_type

    @property
    def ordinal(self):
        """Gets the ordinal of this ServiceIntegration.  # noqa: E501


        :return: The ordinal of this ServiceIntegration.  # noqa: E501
        :rtype: int
        """
        return self._ordinal

    @ordinal.setter
    def ordinal(self, ordinal):
        """Sets the ordinal of this ServiceIntegration.


        :param ordinal: The ordinal of this ServiceIntegration.  # noqa: E501
        :type: int
        """

        self._ordinal = ordinal

    @property
    def parent_integration_id(self):
        """Gets the parent_integration_id of this ServiceIntegration.  # noqa: E501


        :return: The parent_integration_id of this ServiceIntegration.  # noqa: E501
        :rtype: int
        """
        return self._parent_integration_id

    @parent_integration_id.setter
    def parent_integration_id(self, parent_integration_id):
        """Sets the parent_integration_id of this ServiceIntegration.


        :param parent_integration_id: The parent_integration_id of this ServiceIntegration.  # noqa: E501
        :type: int
        """

        self._parent_integration_id = parent_integration_id

    @property
    def sematext_service(self):
        """Gets the sematext_service of this ServiceIntegration.  # noqa: E501


        :return: The sematext_service of this ServiceIntegration.  # noqa: E501
        :rtype: str
        """
        return self._sematext_service

    @sematext_service.setter
    def sematext_service(self, sematext_service):
        """Sets the sematext_service of this ServiceIntegration.


        :param sematext_service: The sematext_service of this ServiceIntegration.  # noqa: E501
        :type: str
        """

        self._sematext_service = sematext_service

    @property
    def visible(self):
        """Gets the visible of this ServiceIntegration.  # noqa: E501


        :return: The visible of this ServiceIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this ServiceIntegration.


        :param visible: The visible of this ServiceIntegration.  # noqa: E501
        :type: bool
        """

        self._visible = visible

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(ServiceIntegration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ServiceIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
