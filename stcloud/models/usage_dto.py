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

class UsageDto(object):
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
        'daily_usage': 'list[DailyDto]',
        'daily_volume_mb': 'int',
        'end': 'datetime',
        'failed_count': 'int',
        'ingested_count': 'int',
        'ingested_volume': 'int',
        'limit_change_events': 'list[LimitChangeEventDTO]',
        'max_allowed_mb': 'int',
        'max_limit_mb': 'int',
        'start': 'datetime',
        'stored_count': 'int',
        'stored_volume': 'int',
        'volume_change_events': 'list[LimitChangeEventDTO]'
    }

    attribute_map = {
        'daily_usage': 'dailyUsage',
        'daily_volume_mb': 'dailyVolumeMB',
        'end': 'end',
        'failed_count': 'failedCount',
        'ingested_count': 'ingestedCount',
        'ingested_volume': 'ingestedVolume',
        'limit_change_events': 'limitChangeEvents',
        'max_allowed_mb': 'maxAllowedMB',
        'max_limit_mb': 'maxLimitMB',
        'start': 'start',
        'stored_count': 'storedCount',
        'stored_volume': 'storedVolume',
        'volume_change_events': 'volumeChangeEvents'
    }

    def __init__(self, daily_usage=None, daily_volume_mb=None, end=None, failed_count=None, ingested_count=None, ingested_volume=None, limit_change_events=None, max_allowed_mb=None, max_limit_mb=None, start=None, stored_count=None, stored_volume=None, volume_change_events=None):  # noqa: E501
        """UsageDto - a model defined in Swagger"""  # noqa: E501
        self._daily_usage = None
        self._daily_volume_mb = None
        self._end = None
        self._failed_count = None
        self._ingested_count = None
        self._ingested_volume = None
        self._limit_change_events = None
        self._max_allowed_mb = None
        self._max_limit_mb = None
        self._start = None
        self._stored_count = None
        self._stored_volume = None
        self._volume_change_events = None
        self.discriminator = None
        if daily_usage is not None:
            self.daily_usage = daily_usage
        if daily_volume_mb is not None:
            self.daily_volume_mb = daily_volume_mb
        if end is not None:
            self.end = end
        if failed_count is not None:
            self.failed_count = failed_count
        if ingested_count is not None:
            self.ingested_count = ingested_count
        if ingested_volume is not None:
            self.ingested_volume = ingested_volume
        if limit_change_events is not None:
            self.limit_change_events = limit_change_events
        if max_allowed_mb is not None:
            self.max_allowed_mb = max_allowed_mb
        if max_limit_mb is not None:
            self.max_limit_mb = max_limit_mb
        if start is not None:
            self.start = start
        if stored_count is not None:
            self.stored_count = stored_count
        if stored_volume is not None:
            self.stored_volume = stored_volume
        if volume_change_events is not None:
            self.volume_change_events = volume_change_events

    @property
    def daily_usage(self):
        """Gets the daily_usage of this UsageDto.  # noqa: E501


        :return: The daily_usage of this UsageDto.  # noqa: E501
        :rtype: list[DailyDto]
        """
        return self._daily_usage

    @daily_usage.setter
    def daily_usage(self, daily_usage):
        """Sets the daily_usage of this UsageDto.


        :param daily_usage: The daily_usage of this UsageDto.  # noqa: E501
        :type: list[DailyDto]
        """

        self._daily_usage = daily_usage

    @property
    def daily_volume_mb(self):
        """Gets the daily_volume_mb of this UsageDto.  # noqa: E501


        :return: The daily_volume_mb of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._daily_volume_mb

    @daily_volume_mb.setter
    def daily_volume_mb(self, daily_volume_mb):
        """Sets the daily_volume_mb of this UsageDto.


        :param daily_volume_mb: The daily_volume_mb of this UsageDto.  # noqa: E501
        :type: int
        """

        self._daily_volume_mb = daily_volume_mb

    @property
    def end(self):
        """Gets the end of this UsageDto.  # noqa: E501


        :return: The end of this UsageDto.  # noqa: E501
        :rtype: datetime
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this UsageDto.


        :param end: The end of this UsageDto.  # noqa: E501
        :type: datetime
        """

        self._end = end

    @property
    def failed_count(self):
        """Gets the failed_count of this UsageDto.  # noqa: E501


        :return: The failed_count of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._failed_count

    @failed_count.setter
    def failed_count(self, failed_count):
        """Sets the failed_count of this UsageDto.


        :param failed_count: The failed_count of this UsageDto.  # noqa: E501
        :type: int
        """

        self._failed_count = failed_count

    @property
    def ingested_count(self):
        """Gets the ingested_count of this UsageDto.  # noqa: E501


        :return: The ingested_count of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._ingested_count

    @ingested_count.setter
    def ingested_count(self, ingested_count):
        """Sets the ingested_count of this UsageDto.


        :param ingested_count: The ingested_count of this UsageDto.  # noqa: E501
        :type: int
        """

        self._ingested_count = ingested_count

    @property
    def ingested_volume(self):
        """Gets the ingested_volume of this UsageDto.  # noqa: E501


        :return: The ingested_volume of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._ingested_volume

    @ingested_volume.setter
    def ingested_volume(self, ingested_volume):
        """Sets the ingested_volume of this UsageDto.


        :param ingested_volume: The ingested_volume of this UsageDto.  # noqa: E501
        :type: int
        """

        self._ingested_volume = ingested_volume

    @property
    def limit_change_events(self):
        """Gets the limit_change_events of this UsageDto.  # noqa: E501


        :return: The limit_change_events of this UsageDto.  # noqa: E501
        :rtype: list[LimitChangeEventDTO]
        """
        return self._limit_change_events

    @limit_change_events.setter
    def limit_change_events(self, limit_change_events):
        """Sets the limit_change_events of this UsageDto.


        :param limit_change_events: The limit_change_events of this UsageDto.  # noqa: E501
        :type: list[LimitChangeEventDTO]
        """

        self._limit_change_events = limit_change_events

    @property
    def max_allowed_mb(self):
        """Gets the max_allowed_mb of this UsageDto.  # noqa: E501


        :return: The max_allowed_mb of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._max_allowed_mb

    @max_allowed_mb.setter
    def max_allowed_mb(self, max_allowed_mb):
        """Sets the max_allowed_mb of this UsageDto.


        :param max_allowed_mb: The max_allowed_mb of this UsageDto.  # noqa: E501
        :type: int
        """

        self._max_allowed_mb = max_allowed_mb

    @property
    def max_limit_mb(self):
        """Gets the max_limit_mb of this UsageDto.  # noqa: E501


        :return: The max_limit_mb of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._max_limit_mb

    @max_limit_mb.setter
    def max_limit_mb(self, max_limit_mb):
        """Sets the max_limit_mb of this UsageDto.


        :param max_limit_mb: The max_limit_mb of this UsageDto.  # noqa: E501
        :type: int
        """

        self._max_limit_mb = max_limit_mb

    @property
    def start(self):
        """Gets the start of this UsageDto.  # noqa: E501


        :return: The start of this UsageDto.  # noqa: E501
        :rtype: datetime
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this UsageDto.


        :param start: The start of this UsageDto.  # noqa: E501
        :type: datetime
        """

        self._start = start

    @property
    def stored_count(self):
        """Gets the stored_count of this UsageDto.  # noqa: E501


        :return: The stored_count of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._stored_count

    @stored_count.setter
    def stored_count(self, stored_count):
        """Sets the stored_count of this UsageDto.


        :param stored_count: The stored_count of this UsageDto.  # noqa: E501
        :type: int
        """

        self._stored_count = stored_count

    @property
    def stored_volume(self):
        """Gets the stored_volume of this UsageDto.  # noqa: E501


        :return: The stored_volume of this UsageDto.  # noqa: E501
        :rtype: int
        """
        return self._stored_volume

    @stored_volume.setter
    def stored_volume(self, stored_volume):
        """Sets the stored_volume of this UsageDto.


        :param stored_volume: The stored_volume of this UsageDto.  # noqa: E501
        :type: int
        """

        self._stored_volume = stored_volume

    @property
    def volume_change_events(self):
        """Gets the volume_change_events of this UsageDto.  # noqa: E501


        :return: The volume_change_events of this UsageDto.  # noqa: E501
        :rtype: list[LimitChangeEventDTO]
        """
        return self._volume_change_events

    @volume_change_events.setter
    def volume_change_events(self, volume_change_events):
        """Sets the volume_change_events of this UsageDto.


        :param volume_change_events: The volume_change_events of this UsageDto.  # noqa: E501
        :type: list[LimitChangeEventDTO]
        """

        self._volume_change_events = volume_change_events

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
        if issubclass(UsageDto, dict):
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
        if not isinstance(other, UsageDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
