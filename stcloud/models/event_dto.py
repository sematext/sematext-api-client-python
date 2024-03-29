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

class EventDto(object):
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
        '_from': 'object',
        'to': 'object',
        'type': 'str'
    }

    attribute_map = {
        '_from': 'from',
        'to': 'to',
        'type': 'type'
    }

    def __init__(self, _from=None, to=None, type=None):  # noqa: E501
        """EventDto - a model defined in Swagger"""  # noqa: E501
        self.__from = None
        self._to = None
        self._type = None
        self.discriminator = None
        if _from is not None:
            self._from = _from
        if to is not None:
            self.to = to
        if type is not None:
            self.type = type

    @property
    def _from(self):
        """Gets the _from of this EventDto.  # noqa: E501


        :return: The _from of this EventDto.  # noqa: E501
        :rtype: object
        """
        return self.__from

    @_from.setter
    def _from(self, _from):
        """Sets the _from of this EventDto.


        :param _from: The _from of this EventDto.  # noqa: E501
        :type: object
        """

        self.__from = _from

    @property
    def to(self):
        """Gets the to of this EventDto.  # noqa: E501


        :return: The to of this EventDto.  # noqa: E501
        :rtype: object
        """
        return self._to

    @to.setter
    def to(self, to):
        """Sets the to of this EventDto.


        :param to: The to of this EventDto.  # noqa: E501
        :type: object
        """

        self._to = to

    @property
    def type(self):
        """Gets the type of this EventDto.  # noqa: E501


        :return: The type of this EventDto.  # noqa: E501
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EventDto.


        :param type: The type of this EventDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["CREATED", "DISABLED", "DELETED", "REACTIVATED", "PLAN_UPDATE", "PAYMENT_METHOD_UPDATE", "SEND_EMAIL_CHANGE", "AUTOMATIC_PLAN_UPGRADE_CHANGE", "MAX_LIMIT_CHANGE", "SAMPLING_CHANGE", "OWNERSHIP_CHANGE", "PIPELINE_CHANGE"]  # noqa: E501
        if type not in allowed_values:
            raise ValueError(
                "Invalid value for `type` ({0}), must be one of {1}"  # noqa: E501
                .format(type, allowed_values)
            )

        self._type = type

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
        if issubclass(EventDto, dict):
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
        if not isinstance(other, EventDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
