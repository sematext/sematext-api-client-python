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

class CloudWatchSettings(object):
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
        'access_key': 'str',
        'fetch_frequency': 'str',
        'region': 'str',
        'secret_key': 'str'
    }

    attribute_map = {
        'access_key': 'accessKey',
        'fetch_frequency': 'fetchFrequency',
        'region': 'region',
        'secret_key': 'secretKey'
    }

    def __init__(self, access_key=None, fetch_frequency=None, region=None, secret_key=None):  # noqa: E501
        """CloudWatchSettings - a model defined in Swagger"""  # noqa: E501
        self._access_key = None
        self._fetch_frequency = None
        self._region = None
        self._secret_key = None
        self.discriminator = None
        if access_key is not None:
            self.access_key = access_key
        if fetch_frequency is not None:
            self.fetch_frequency = fetch_frequency
        if region is not None:
            self.region = region
        if secret_key is not None:
            self.secret_key = secret_key

    @property
    def access_key(self):
        """Gets the access_key of this CloudWatchSettings.  # noqa: E501


        :return: The access_key of this CloudWatchSettings.  # noqa: E501
        :rtype: str
        """
        return self._access_key

    @access_key.setter
    def access_key(self, access_key):
        """Sets the access_key of this CloudWatchSettings.


        :param access_key: The access_key of this CloudWatchSettings.  # noqa: E501
        :type: str
        """

        self._access_key = access_key

    @property
    def fetch_frequency(self):
        """Gets the fetch_frequency of this CloudWatchSettings.  # noqa: E501


        :return: The fetch_frequency of this CloudWatchSettings.  # noqa: E501
        :rtype: str
        """
        return self._fetch_frequency

    @fetch_frequency.setter
    def fetch_frequency(self, fetch_frequency):
        """Sets the fetch_frequency of this CloudWatchSettings.


        :param fetch_frequency: The fetch_frequency of this CloudWatchSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["MINUTE", "FIVE_MINUTES", "FIFTEEN_MINUTES"]  # noqa: E501
        if fetch_frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `fetch_frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(fetch_frequency, allowed_values)
            )

        self._fetch_frequency = fetch_frequency

    @property
    def region(self):
        """Gets the region of this CloudWatchSettings.  # noqa: E501


        :return: The region of this CloudWatchSettings.  # noqa: E501
        :rtype: str
        """
        return self._region

    @region.setter
    def region(self, region):
        """Sets the region of this CloudWatchSettings.


        :param region: The region of this CloudWatchSettings.  # noqa: E501
        :type: str
        """
        allowed_values = ["US_EAST_1", "US_WEST_1", "EU_WEST_1", "US_WEST_2", "AP_SOUTHEAST_1", "AP_SOUTHEAST_2", "AP_NORTHEAST_1", "SA_EAST_1", "GovCloud", "CN_NORTH_1", "US_EAST_2", "AP_SOUTH_1", "AP_NORTHEAST_2", "CA_CENTRAL_1", "EU_CENTRAL_1", "EU_WEST_2"]  # noqa: E501
        if region not in allowed_values:
            raise ValueError(
                "Invalid value for `region` ({0}), must be one of {1}"  # noqa: E501
                .format(region, allowed_values)
            )

        self._region = region

    @property
    def secret_key(self):
        """Gets the secret_key of this CloudWatchSettings.  # noqa: E501


        :return: The secret_key of this CloudWatchSettings.  # noqa: E501
        :rtype: str
        """
        return self._secret_key

    @secret_key.setter
    def secret_key(self, secret_key):
        """Sets the secret_key of this CloudWatchSettings.


        :param secret_key: The secret_key of this CloudWatchSettings.  # noqa: E501
        :type: str
        """

        self._secret_key = secret_key

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
        if issubclass(CloudWatchSettings, dict):
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
        if not isinstance(other, CloudWatchSettings):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
