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


class ReportInfo(object):
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
        'addresses': 'str',
        'app_id': 'int',
        'end_date': 'datetime',
        'filters': 'str',
        'report_name': 'str',
        'start_date': 'datetime',
        'subject': 'str',
        'text': 'str'
    }

    attribute_map = {
        'addresses': 'addresses',
        'app_id': 'appId',
        'end_date': 'endDate',
        'filters': 'filters',
        'report_name': 'reportName',
        'start_date': 'startDate',
        'subject': 'subject',
        'text': 'text'
    }

    def __init__(self, addresses=None, app_id=None, end_date=None, filters=None, report_name=None, start_date=None, subject=None, text=None):  # noqa: E501
        """ReportInfo - a model defined in Swagger"""  # noqa: E501

        self._addresses = None
        self._app_id = None
        self._end_date = None
        self._filters = None
        self._report_name = None
        self._start_date = None
        self._subject = None
        self._text = None
        self.discriminator = None

        if addresses is not None:
            self.addresses = addresses
        if app_id is not None:
            self.app_id = app_id
        if end_date is not None:
            self.end_date = end_date
        if filters is not None:
            self.filters = filters
        if report_name is not None:
            self.report_name = report_name
        if start_date is not None:
            self.start_date = start_date
        if subject is not None:
            self.subject = subject
        if text is not None:
            self.text = text

    @property
    def addresses(self):
        """Gets the addresses of this ReportInfo.  # noqa: E501

        Comma separated list of email addresses  # noqa: E501

        :return: The addresses of this ReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._addresses

    @addresses.setter
    def addresses(self, addresses):
        """Sets the addresses of this ReportInfo.

        Comma separated list of email addresses  # noqa: E501

        :param addresses: The addresses of this ReportInfo.  # noqa: E501
        :type: str
        """

        self._addresses = addresses

    @property
    def app_id(self):
        """Gets the app_id of this ReportInfo.  # noqa: E501


        :return: The app_id of this ReportInfo.  # noqa: E501
        :rtype: int
        """
        return self._app_id

    @app_id.setter
    def app_id(self, app_id):
        """Sets the app_id of this ReportInfo.


        :param app_id: The app_id of this ReportInfo.  # noqa: E501
        :type: int
        """

        self._app_id = app_id

    @property
    def end_date(self):
        """Gets the end_date of this ReportInfo.  # noqa: E501


        :return: The end_date of this ReportInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._end_date

    @end_date.setter
    def end_date(self, end_date):
        """Sets the end_date of this ReportInfo.


        :param end_date: The end_date of this ReportInfo.  # noqa: E501
        :type: datetime
        """

        self._end_date = end_date

    @property
    def filters(self):
        """Gets the filters of this ReportInfo.  # noqa: E501


        :return: The filters of this ReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._filters

    @filters.setter
    def filters(self, filters):
        """Sets the filters of this ReportInfo.


        :param filters: The filters of this ReportInfo.  # noqa: E501
        :type: str
        """

        self._filters = filters

    @property
    def report_name(self):
        """Gets the report_name of this ReportInfo.  # noqa: E501


        :return: The report_name of this ReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._report_name

    @report_name.setter
    def report_name(self, report_name):
        """Sets the report_name of this ReportInfo.


        :param report_name: The report_name of this ReportInfo.  # noqa: E501
        :type: str
        """

        self._report_name = report_name

    @property
    def start_date(self):
        """Gets the start_date of this ReportInfo.  # noqa: E501


        :return: The start_date of this ReportInfo.  # noqa: E501
        :rtype: datetime
        """
        return self._start_date

    @start_date.setter
    def start_date(self, start_date):
        """Sets the start_date of this ReportInfo.


        :param start_date: The start_date of this ReportInfo.  # noqa: E501
        :type: datetime
        """

        self._start_date = start_date

    @property
    def subject(self):
        """Gets the subject of this ReportInfo.  # noqa: E501


        :return: The subject of this ReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._subject

    @subject.setter
    def subject(self, subject):
        """Sets the subject of this ReportInfo.


        :param subject: The subject of this ReportInfo.  # noqa: E501
        :type: str
        """

        self._subject = subject

    @property
    def text(self):
        """Gets the text of this ReportInfo.  # noqa: E501


        :return: The text of this ReportInfo.  # noqa: E501
        :rtype: str
        """
        return self._text

    @text.setter
    def text(self, text):
        """Sets the text of this ReportInfo.


        :param text: The text of this ReportInfo.  # noqa: E501
        :type: str
        """

        self._text = text

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
        if issubclass(ReportInfo, dict):
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
        if not isinstance(other, ReportInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
