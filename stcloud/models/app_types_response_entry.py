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

class AppTypesResponseEntry(object):
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
        'app_types': 'list[str]'
    }

    attribute_map = {
        'app_types': 'appTypes'
    }

    def __init__(self, app_types=None):  # noqa: E501
        """AppTypesResponseEntry - a model defined in Swagger"""  # noqa: E501
        self._app_types = None
        self.discriminator = None
        if app_types is not None:
            self.app_types = app_types

    @property
    def app_types(self):
        """Gets the app_types of this AppTypesResponseEntry.  # noqa: E501


        :return: The app_types of this AppTypesResponseEntry.  # noqa: E501
        :rtype: list[str]
        """
        return self._app_types

    @app_types.setter
    def app_types(self, app_types):
        """Sets the app_types of this AppTypesResponseEntry.


        :param app_types: The app_types of this AppTypesResponseEntry.  # noqa: E501
        :type: list[str]
        """

        self._app_types = app_types

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
        if issubclass(AppTypesResponseEntry, dict):
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
        if not isinstance(other, AppTypesResponseEntry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
