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


class DataSeriesRequest(object):
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
        'default_interval': 'int',
        'end': 'str',
        'filters': 'dict(str, DataSeriesFilter)',
        'granularity': 'str',
        'interval': 'str',
        'metric': 'str',
        'start': 'str'
    }

    attribute_map = {
        'default_interval': 'defaultInterval',
        'end': 'end',
        'filters': 'filters',
        'granularity': 'granularity',
        'interval': 'interval',
        'metric': 'metric',
        'start': 'start'
    }

    def __init__(self, default_interval=None, end=None, filters=None, granularity=None, interval=None, metric=None, start=None):  # noqa: E501
        """DataSeriesRequest - a model defined in Swagger"""  # noqa: E501

        self._default_interval = None
        self._end = None
        self._filters = None
        self._granularity = None
        self._interval = None
        self._metric = None
        self._start = None
        self.discriminator = None

        if default_interval is not None:
            self.default_interval = default_interval
        if end is not None:
            self.end = end
        if filters is not None:
            self.filters = filters
        if granularity is not None:
            self.granularity = granularity
        if interval is not None:
            self.interval = interval
        self.metric = metric
        if start is not None:
            self.start = start

    @property
    def default_interval(self):
        """Gets the default_interval of this DataSeriesRequest.  # noqa: E501


        :return: The default_interval of this DataSeriesRequest.  # noqa: E501
        :rtype: int
        """
        return self._default_interval

    @default_interval.setter
    def default_interval(self, default_interval):
        """Sets the default_interval of this DataSeriesRequest.


        :param default_interval: The default_interval of this DataSeriesRequest.  # noqa: E501
        :type: int
        """

        self._default_interval = default_interval

    @property
    def end(self):
        """Gets the end of this DataSeriesRequest.  # noqa: E501

        End time of interval. Can be expressed as timestamp in milliseconds or UTC date in yyyy-MM-dd HH:mm:ss format  # noqa: E501

        :return: The end of this DataSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._end

    @end.setter
    def end(self, end):
        """Sets the end of this DataSeriesRequest.

        End time of interval. Can be expressed as timestamp in milliseconds or UTC date in yyyy-MM-dd HH:mm:ss format  # noqa: E501

        :param end: The end of this DataSeriesRequest.  # noqa: E501
        :type: str
        """

        self._end = end

    @property
    def filters(self):
        """Gets the filters of this DataSeriesRequest.  # noqa: E501

        Map of allowed filter values and aggregation strategy. List of available filter values can be fetched using metric filters endpoint and default aggregation strategy depends on metric  # noqa: E501

        :return: The filters of this DataSeriesRequest.  # noqa: E501
        :rtype: dict(str, DataSeriesFilter)
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this DataSeriesRequest.

        Map of allowed filter values and aggregation strategy. List of available filter values can be fetched using metric filters endpoint and default aggregation strategy depends on metric  # noqa: E501

        :param filters: The filters of this DataSeriesRequest.  # noqa: E501
        :type: dict(str, DataSeriesFilter)
        """

        self._filters = filters

    @property
    def granularity(self):
        """Gets the granularity of this DataSeriesRequest.  # noqa: E501

        Data points interval granularity between two data points.Default value is \"AUTO\" - calculated based on selected time span. Not required while getting filters.  # noqa: E501

        :return: The granularity of this DataSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._granularity

    @granularity.setter
    def granularity(self, granularity):
        """Sets the granularity of this DataSeriesRequest.

        Data points interval granularity between two data points.Default value is \"AUTO\" - calculated based on selected time span. Not required while getting filters.  # noqa: E501

        :param granularity: The granularity of this DataSeriesRequest.  # noqa: E501
        :type: str
        """
        allowed_values = ["AUTO", "ONE_MINUTE", "FIVE_MINUTES", "HOUR", "DAY", "WEEK", "MONTH"]  # noqa: E501
        if granularity not in allowed_values:
            raise ValueError(
                "Invalid value for `granularity` ({0}), must be one of {1}"  # noqa: E501
                .format(granularity, allowed_values)
            )

        self._granularity = granularity

    @property
    def interval(self):
        """Gets the interval of this DataSeriesRequest.  # noqa: E501


        :return: The interval of this DataSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._interval

    @interval.setter
    def interval(self, interval):
        """Sets the interval of this DataSeriesRequest.


        :param interval: The interval of this DataSeriesRequest.  # noqa: E501
        :type: str
        """

        self._interval = interval

    @property
    def metric(self):
        """Gets the metric of this DataSeriesRequest.  # noqa: E501

        Metric name or metric group prefix  # noqa: E501

        :return: The metric of this DataSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this DataSeriesRequest.

        Metric name or metric group prefix  # noqa: E501

        :param metric: The metric of this DataSeriesRequest.  # noqa: E501
        :type: str
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")  # noqa: E501

        self._metric = metric

    @property
    def start(self):
        """Gets the start of this DataSeriesRequest.  # noqa: E501

        Start time of interval. Can be expressed as timestamp in milliseconds or UTC date in yyyy-MM-dd HH:mm:ss format  # noqa: E501

        :return: The start of this DataSeriesRequest.  # noqa: E501
        :rtype: str
        """
        return self._start

    @start.setter
    def start(self, start):
        """Sets the start of this DataSeriesRequest.

        Start time of interval. Can be expressed as timestamp in milliseconds or UTC date in yyyy-MM-dd HH:mm:ss format  # noqa: E501

        :param start: The start of this DataSeriesRequest.  # noqa: E501
        :type: str
        """

        self._start = start

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
        if issubclass(DataSeriesRequest, dict):
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
        if not isinstance(other, DataSeriesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
