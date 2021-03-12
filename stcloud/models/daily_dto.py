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

class DailyDto(object):
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
        'day': 'int',
        'failed': 'int',
        'indexed': 'int',
        'volume': 'int'
    }

    attribute_map = {
        'day': 'day',
        'failed': 'failed',
        'indexed': 'indexed',
        'volume': 'volume'
    }

    def __init__(self, day=None, failed=None, indexed=None, volume=None):  # noqa: E501
        """DailyDto - a model defined in Swagger"""  # noqa: E501
        self._day = None
        self._failed = None
        self._indexed = None
        self._volume = None
        self.discriminator = None
        if day is not None:
            self.day = day
        if failed is not None:
            self.failed = failed
        if indexed is not None:
            self.indexed = indexed
        if volume is not None:
            self.volume = volume

    @property
    def day(self):
        """Gets the day of this DailyDto.  # noqa: E501


        :return: The day of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._day

    @day.setter
    def day(self, day):
        """Sets the day of this DailyDto.


        :param day: The day of this DailyDto.  # noqa: E501
        :type: int
        """

        self._day = day

    @property
    def failed(self):
        """Gets the failed of this DailyDto.  # noqa: E501


        :return: The failed of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._failed

    @failed.setter
    def failed(self, failed):
        """Sets the failed of this DailyDto.


        :param failed: The failed of this DailyDto.  # noqa: E501
        :type: int
        """

        self._failed = failed

    @property
    def indexed(self):
        """Gets the indexed of this DailyDto.  # noqa: E501


        :return: The indexed of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._indexed

    @indexed.setter
    def indexed(self, indexed):
        """Sets the indexed of this DailyDto.


        :param indexed: The indexed of this DailyDto.  # noqa: E501
        :type: int
        """

        self._indexed = indexed

    @property
    def volume(self):
        """Gets the volume of this DailyDto.  # noqa: E501


        :return: The volume of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._volume

    @volume.setter
    def volume(self, volume):
        """Sets the volume of this DailyDto.


        :param volume: The volume of this DailyDto.  # noqa: E501
        :type: int
        """

        self._volume = volume

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
        if issubclass(DailyDto, dict):
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
        if not isinstance(other, DailyDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
