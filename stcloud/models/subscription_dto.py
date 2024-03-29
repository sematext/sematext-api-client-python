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

class SubscriptionDto(object):
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
        'additional_params': 'str',
        'addresses': 'str',
        'enable': 'bool',
        'filters': 'str',
        'frequency': 'str',
        'id': 'int',
        'report_name': 'str',
        'send_time': 'datetime',
        'subject': 'str',
        'system_id': 'int',
        'text': 'str',
        'time_range': 'str',
        'user_permissions': 'UserPermissions'
    }

    attribute_map = {
        'additional_params': 'additionalParams',
        'addresses': 'addresses',
        'enable': 'enable',
        'filters': 'filters',
        'frequency': 'frequency',
        'id': 'id',
        'report_name': 'reportName',
        'send_time': 'sendTime',
        'subject': 'subject',
        'system_id': 'systemId',
        'text': 'text',
        'time_range': 'timeRange',
        'user_permissions': 'userPermissions'
    }

    def __init__(self, additional_params=None, addresses=None, enable=None, filters=None, frequency=None, id=None, report_name=None, send_time=None, subject=None, system_id=None, text=None, time_range=None, user_permissions=None):  # noqa: E501
        """SubscriptionDto - a model defined in Swagger"""  # noqa: E501
        self._additional_params = None
        self._addresses = None
        self._enable = None
        self._filters = None
        self._frequency = None
        self._id = None
        self._report_name = None
        self._send_time = None
        self._subject = None
        self._system_id = None
        self._text = None
        self._time_range = None
        self._user_permissions = None
        self.discriminator = None
        if additional_params is not None:
            self.additional_params = additional_params
        if addresses is not None:
            self.addresses = addresses
        if enable is not None:
            self.enable = enable
        if filters is not None:
            self.filters = filters
        if frequency is not None:
            self.frequency = frequency
        if id is not None:
            self.id = id
        if report_name is not None:
            self.report_name = report_name
        if send_time is not None:
            self.send_time = send_time
        if subject is not None:
            self.subject = subject
        if system_id is not None:
            self.system_id = system_id
        if text is not None:
            self.text = text
        if time_range is not None:
            self.time_range = time_range
        if user_permissions is not None:
            self.user_permissions = user_permissions

    @property
    def additional_params(self):
        """Gets the additional_params of this SubscriptionDto.  # noqa: E501


        :return: The additional_params of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._additional_params

    @additional_params.setter
    def additional_params(self, additional_params):
        """Sets the additional_params of this SubscriptionDto.


        :param additional_params: The additional_params of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._additional_params = additional_params

    @property
    def addresses(self):
        """Gets the addresses of this SubscriptionDto.  # noqa: E501


        :return: The addresses of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this SubscriptionDto.


        :param addresses: The addresses of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._addresses = addresses

    @property
    def enable(self):
        """Gets the enable of this SubscriptionDto.  # noqa: E501


        :return: The enable of this SubscriptionDto.  # noqa: E501
        :rtype: bool
        """
        return self._enable

    @enable.setter
    def enable(self, enable):
        """Sets the enable of this SubscriptionDto.


        :param enable: The enable of this SubscriptionDto.  # noqa: E501
        :type: bool
        """

        self._enable = enable

    @property
    def filters(self):
        """Gets the filters of this SubscriptionDto.  # noqa: E501


        :return: The filters of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this SubscriptionDto.


        :param filters: The filters of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._filters = filters

    @property
    def frequency(self):
        """Gets the frequency of this SubscriptionDto.  # noqa: E501


        :return: The frequency of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._frequency

    @frequency.setter
    def frequency(self, frequency):
        """Sets the frequency of this SubscriptionDto.


        :param frequency: The frequency of this SubscriptionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["EVERY_FIVE_MINUTES", "DAILY", "WEEKLY", "MONTHLY", "QUARTERLY"]  # noqa: E501
        if frequency not in allowed_values:
            raise ValueError(
                "Invalid value for `frequency` ({0}), must be one of {1}"  # noqa: E501
                .format(frequency, allowed_values)
            )

        self._frequency = frequency

    @property
    def id(self):
        """Gets the id of this SubscriptionDto.  # noqa: E501


        :return: The id of this SubscriptionDto.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionDto.


        :param id: The id of this SubscriptionDto.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def report_name(self):
        """Gets the report_name of this SubscriptionDto.  # noqa: E501


        :return: The report_name of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this SubscriptionDto.


        :param report_name: The report_name of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def send_time(self):
        """Gets the send_time of this SubscriptionDto.  # noqa: E501


        :return: The send_time of this SubscriptionDto.  # noqa: E501
        :rtype: datetime
        """
        return self._send_time

    @send_time.setter
    def send_time(self, send_time):
        """Sets the send_time of this SubscriptionDto.


        :param send_time: The send_time of this SubscriptionDto.  # noqa: E501
        :type: datetime
        """

        self._send_time = send_time

    @property
    def subject(self):
        """Gets the subject of this SubscriptionDto.  # noqa: E501


        :return: The subject of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this SubscriptionDto.


        :param subject: The subject of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def system_id(self):
        """Gets the system_id of this SubscriptionDto.  # noqa: E501


        :return: The system_id of this SubscriptionDto.  # noqa: E501
        :rtype: int
        """
        return self._system_id

    @system_id.setter
    def system_id(self, system_id):
        """Sets the system_id of this SubscriptionDto.


        :param system_id: The system_id of this SubscriptionDto.  # noqa: E501
        :type: int
        """

        self._system_id = system_id

    @property
    def text(self):
        """Gets the text of this SubscriptionDto.  # noqa: E501


        :return: The text of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this SubscriptionDto.


        :param text: The text of this SubscriptionDto.  # noqa: E501
        :type: str
        """

        self._text = text

    @property
    def time_range(self):
        """Gets the time_range of this SubscriptionDto.  # noqa: E501


        :return: The time_range of this SubscriptionDto.  # noqa: E501
        :rtype: str
        """
        return self._time_range

    @time_range.setter
    def time_range(self, time_range):
        """Sets the time_range of this SubscriptionDto.


        :param time_range: The time_range of this SubscriptionDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["ONE_DAY", "ONE_WEEK", "ONE_MONTH", "TWO_MONTH", "SIX_MONTH", "ONE_YEAR"]  # noqa: E501
        if time_range not in allowed_values:
            raise ValueError(
                "Invalid value for `time_range` ({0}), must be one of {1}"  # noqa: E501
                .format(time_range, allowed_values)
            )

        self._time_range = time_range

    @property
    def user_permissions(self):
        """Gets the user_permissions of this SubscriptionDto.  # noqa: E501


        :return: The user_permissions of this SubscriptionDto.  # noqa: E501
        :rtype: UserPermissions
        """
        return self._user_permissions

    @user_permissions.setter
    def user_permissions(self, user_permissions):
        """Sets the user_permissions of this SubscriptionDto.


        :param user_permissions: The user_permissions of this SubscriptionDto.  # noqa: E501
        :type: UserPermissions
        """

        self._user_permissions = user_permissions

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
        if issubclass(SubscriptionDto, dict):
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
        if not isinstance(other, SubscriptionDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
