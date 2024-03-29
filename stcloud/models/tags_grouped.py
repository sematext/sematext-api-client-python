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

class TagsGrouped(object):
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
        'app_id': 'int',
        'tags': 'dict(str, Dimension)'
    }

    attribute_map = {
        'app_id': 'appId',
        'tags': 'tags'
    }

    def __init__(self, app_id=None, tags=None):  # noqa: E501
        """TagsGrouped - a model defined in Swagger"""  # noqa: E501
        self._app_id = None
        self._tags = None
        self.discriminator = None
        self.app_id = app_id
        self.tags = tags

    @property
    def app_id(self):
        """Gets the app_id of this TagsGrouped.  # noqa: E501


        :return: The app_id of this TagsGrouped.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this TagsGrouped.


        :param app_id: The app_id of this TagsGrouped.  # noqa: E501
        :type: int
        """
        if app_id is None:
            raise ValueError("Invalid value for `app_id`, must not be `None`")  # noqa: E501

        self._app_id = app_id

    @property
    def tags(self):
        """Gets the tags of this TagsGrouped.  # noqa: E501


        :return: The tags of this TagsGrouped.  # noqa: E501
        :rtype: dict(str, Dimension)
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TagsGrouped.


        :param tags: The tags of this TagsGrouped.  # noqa: E501
        :type: dict(str, Dimension)
        """
        if tags is None:
            raise ValueError("Invalid value for `tags`, must not be `None`")  # noqa: E501

        self._tags = tags

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
        if issubclass(TagsGrouped, dict):
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
        if not isinstance(other, TagsGrouped):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
