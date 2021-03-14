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

class UpdateAppInfo(object):
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
        'description': 'str',
        'ignore_percentage': 'float',
        'max_events': 'int',
        'max_limit_mb': 'int',
        'name': 'str',
        'sampling': 'bool',
        'sampling_percentage': 'int',
        'staggering': 'bool',
        'status': 'str'
    }

    attribute_map = {
        'description': 'description',
        'ignore_percentage': 'ignorePercentage',
        'max_events': 'maxEvents',
        'max_limit_mb': 'maxLimitMB',
        'name': 'name',
        'sampling': 'sampling',
        'sampling_percentage': 'samplingPercentage',
        'staggering': 'staggering',
        'status': 'status'
    }

    def __init__(self, description=None, ignore_percentage=None, max_events=None, max_limit_mb=None, name=None, sampling=None, sampling_percentage=None, staggering=None, status=None):  # noqa: E501
        """UpdateAppInfo - a model defined in Swagger"""  # noqa: E501
        self._description = None
        self._ignore_percentage = None
        self._max_events = None
        self._max_limit_mb = None
        self._name = None
        self._sampling = None
        self._sampling_percentage = None
        self._staggering = None
        self._status = None
        self.discriminator = None
        if description is not None:
            self.description = description
        if ignore_percentage is not None:
            self.ignore_percentage = ignore_percentage
        if max_events is not None:
            self.max_events = max_events
        if max_limit_mb is not None:
            self.max_limit_mb = max_limit_mb
        if name is not None:
            self.name = name
        if sampling is not None:
            self.sampling = sampling
        if sampling_percentage is not None:
            self.sampling_percentage = sampling_percentage
        if staggering is not None:
            self.staggering = staggering
        if status is not None:
            self.status = status

    @property
    def description(self):
        """Gets the description of this UpdateAppInfo.  # noqa: E501


        :return: The description of this UpdateAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this UpdateAppInfo.


        :param description: The description of this UpdateAppInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def ignore_percentage(self):
        """Gets the ignore_percentage of this UpdateAppInfo.  # noqa: E501


        :return: The ignore_percentage of this UpdateAppInfo.  # noqa: E501
        :rtype: float
        """
        return self._ignore_percentage

    @ignore_percentage.setter
    def ignore_percentage(self, ignore_percentage):
        """Sets the ignore_percentage of this UpdateAppInfo.


        :param ignore_percentage: The ignore_percentage of this UpdateAppInfo.  # noqa: E501
        :type: float
        """

        self._ignore_percentage = ignore_percentage

    @property
    def max_events(self):
        """Gets the max_events of this UpdateAppInfo.  # noqa: E501


        :return: The max_events of this UpdateAppInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_events

    @max_events.setter
    def max_events(self, max_events):
        """Sets the max_events of this UpdateAppInfo.


        :param max_events: The max_events of this UpdateAppInfo.  # noqa: E501
        :type: int
        """

        self._max_events = max_events

    @property
    def max_limit_mb(self):
        """Gets the max_limit_mb of this UpdateAppInfo.  # noqa: E501


        :return: The max_limit_mb of this UpdateAppInfo.  # noqa: E501
        :rtype: int
        """
        return self._max_limit_mb

    @max_limit_mb.setter
    def max_limit_mb(self, max_limit_mb):
        """Sets the max_limit_mb of this UpdateAppInfo.


        :param max_limit_mb: The max_limit_mb of this UpdateAppInfo.  # noqa: E501
        :type: int
        """

        self._max_limit_mb = max_limit_mb

    @property
    def name(self):
        """Gets the name of this UpdateAppInfo.  # noqa: E501


        :return: The name of this UpdateAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this UpdateAppInfo.


        :param name: The name of this UpdateAppInfo.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def sampling(self):
        """Gets the sampling of this UpdateAppInfo.  # noqa: E501


        :return: The sampling of this UpdateAppInfo.  # noqa: E501
        :rtype: bool
        """
        return self._sampling

    @sampling.setter
    def sampling(self, sampling):
        """Sets the sampling of this UpdateAppInfo.


        :param sampling: The sampling of this UpdateAppInfo.  # noqa: E501
        :type: bool
        """

        self._sampling = sampling

    @property
    def sampling_percentage(self):
        """Gets the sampling_percentage of this UpdateAppInfo.  # noqa: E501


        :return: The sampling_percentage of this UpdateAppInfo.  # noqa: E501
        :rtype: int
        """
        return self._sampling_percentage

    @sampling_percentage.setter
    def sampling_percentage(self, sampling_percentage):
        """Sets the sampling_percentage of this UpdateAppInfo.


        :param sampling_percentage: The sampling_percentage of this UpdateAppInfo.  # noqa: E501
        :type: int
        """

        self._sampling_percentage = sampling_percentage

    @property
    def staggering(self):
        """Gets the staggering of this UpdateAppInfo.  # noqa: E501


        :return: The staggering of this UpdateAppInfo.  # noqa: E501
        :rtype: bool
        """
        return self._staggering

    @staggering.setter
    def staggering(self, staggering):
        """Sets the staggering of this UpdateAppInfo.


        :param staggering: The staggering of this UpdateAppInfo.  # noqa: E501
        :type: bool
        """

        self._staggering = staggering

    @property
    def status(self):
        """Gets the status of this UpdateAppInfo.  # noqa: E501


        :return: The status of this UpdateAppInfo.  # noqa: E501
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """Sets the status of this UpdateAppInfo.


        :param status: The status of this UpdateAppInfo.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DISABLED"]  # noqa: E501
        if status not in allowed_values:
            raise ValueError(
                "Invalid value for `status` ({0}), must be one of {1}"  # noqa: E501
                .format(status, allowed_values)
            )

        self._status = status

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
        if issubclass(UpdateAppInfo, dict):
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
        if not isinstance(other, UpdateAppInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
