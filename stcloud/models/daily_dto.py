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
        'ingested_count': 'int',
        'ingested_volume': 'int',
        'stored_count': 'int',
        'stored_volume': 'int'
    }

    attribute_map = {
        'day': 'day',
        'failed': 'failed',
        'ingested_count': 'ingestedCount',
        'ingested_volume': 'ingestedVolume',
        'stored_count': 'storedCount',
        'stored_volume': 'storedVolume'
    }

    def __init__(self, day=None, failed=None, ingested_count=None, ingested_volume=None, stored_count=None, stored_volume=None):  # noqa: E501
        """DailyDto - a model defined in Swagger"""  # noqa: E501
        self._day = None
        self._failed = None
        self._ingested_count = None
        self._ingested_volume = None
        self._stored_count = None
        self._stored_volume = None
        self.discriminator = None
        if day is not None:
            self.day = day
        if failed is not None:
            self.failed = failed
        if ingested_count is not None:
            self.ingested_count = ingested_count
        if ingested_volume is not None:
            self.ingested_volume = ingested_volume
        if stored_count is not None:
            self.stored_count = stored_count
        if stored_volume is not None:
            self.stored_volume = stored_volume

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
    def ingested_count(self):
        """Gets the ingested_count of this DailyDto.  # noqa: E501


        :return: The ingested_count of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._ingested_count

    @ingested_count.setter
    def ingested_count(self, ingested_count):
        """Sets the ingested_count of this DailyDto.


        :param ingested_count: The ingested_count of this DailyDto.  # noqa: E501
        :type: int
        """

        self._ingested_count = ingested_count

    @property
    def ingested_volume(self):
        """Gets the ingested_volume of this DailyDto.  # noqa: E501


        :return: The ingested_volume of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._ingested_volume

    @ingested_volume.setter
    def ingested_volume(self, ingested_volume):
        """Sets the ingested_volume of this DailyDto.


        :param ingested_volume: The ingested_volume of this DailyDto.  # noqa: E501
        :type: int
        """

        self._ingested_volume = ingested_volume

    @property
    def stored_count(self):
        """Gets the stored_count of this DailyDto.  # noqa: E501


        :return: The stored_count of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._stored_count

    @stored_count.setter
    def stored_count(self, stored_count):
        """Sets the stored_count of this DailyDto.


        :param stored_count: The stored_count of this DailyDto.  # noqa: E501
        :type: int
        """

        self._stored_count = stored_count

    @property
    def stored_volume(self):
        """Gets the stored_volume of this DailyDto.  # noqa: E501


        :return: The stored_volume of this DailyDto.  # noqa: E501
        :rtype: int
        """
        return self._stored_volume

    @stored_volume.setter
    def stored_volume(self, stored_volume):
        """Sets the stored_volume of this DailyDto.


        :param stored_volume: The stored_volume of this DailyDto.  # noqa: E501
        :type: int
        """

        self._stored_volume = stored_volume

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
