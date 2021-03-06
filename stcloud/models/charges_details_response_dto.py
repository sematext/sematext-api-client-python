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

class ChargesDetailsResponseDto(object):
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
        'app': 'App',
        'charge_base': 'str',
        'day_usage_data': 'list[DayUsageData]',
        'monthly_fee_amount': 'float',
        'period_fee_periods': 'list[MinPeriodFeePeriod]',
        'total_amount': 'float',
        'usage_amount': 'float'
    }

    attribute_map = {
        'app': 'app',
        'charge_base': 'chargeBase',
        'day_usage_data': 'dayUsageData',
        'monthly_fee_amount': 'monthlyFeeAmount',
        'period_fee_periods': 'periodFeePeriods',
        'total_amount': 'totalAmount',
        'usage_amount': 'usageAmount'
    }

    def __init__(self, app=None, charge_base=None, day_usage_data=None, monthly_fee_amount=None, period_fee_periods=None, total_amount=None, usage_amount=None):  # noqa: E501
        """ChargesDetailsResponseDto - a model defined in Swagger"""  # noqa: E501
        self._app = None
        self._charge_base = None
        self._day_usage_data = None
        self._monthly_fee_amount = None
        self._period_fee_periods = None
        self._total_amount = None
        self._usage_amount = None
        self.discriminator = None
        if app is not None:
            self.app = app
        if charge_base is not None:
            self.charge_base = charge_base
        if day_usage_data is not None:
            self.day_usage_data = day_usage_data
        if monthly_fee_amount is not None:
            self.monthly_fee_amount = monthly_fee_amount
        if period_fee_periods is not None:
            self.period_fee_periods = period_fee_periods
        if total_amount is not None:
            self.total_amount = total_amount
        if usage_amount is not None:
            self.usage_amount = usage_amount

    @property
    def app(self):
        """Gets the app of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The app of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: App
        """
        return self._app

    @app.setter
    def app(self, app):
        """Sets the app of this ChargesDetailsResponseDto.


        :param app: The app of this ChargesDetailsResponseDto.  # noqa: E501
        :type: App
        """

        self._app = app

    @property
    def charge_base(self):
        """Gets the charge_base of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The charge_base of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: str
        """
        return self._charge_base

    @charge_base.setter
    def charge_base(self, charge_base):
        """Sets the charge_base of this ChargesDetailsResponseDto.


        :param charge_base: The charge_base of this ChargesDetailsResponseDto.  # noqa: E501
        :type: str
        """
        allowed_values = ["SUMMARIZED_USAGE", "MIN_MONTHLY_FEE", "SUM_OF_DAILY_FEES", "TOTAL_MONTHLY_FEE"]  # noqa: E501
        if charge_base not in allowed_values:
            raise ValueError(
                "Invalid value for `charge_base` ({0}), must be one of {1}"  # noqa: E501
                .format(charge_base, allowed_values)
            )

        self._charge_base = charge_base

    @property
    def day_usage_data(self):
        """Gets the day_usage_data of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The day_usage_data of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: list[DayUsageData]
        """
        return self._day_usage_data

    @day_usage_data.setter
    def day_usage_data(self, day_usage_data):
        """Sets the day_usage_data of this ChargesDetailsResponseDto.


        :param day_usage_data: The day_usage_data of this ChargesDetailsResponseDto.  # noqa: E501
        :type: list[DayUsageData]
        """

        self._day_usage_data = day_usage_data

    @property
    def monthly_fee_amount(self):
        """Gets the monthly_fee_amount of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The monthly_fee_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._monthly_fee_amount

    @monthly_fee_amount.setter
    def monthly_fee_amount(self, monthly_fee_amount):
        """Sets the monthly_fee_amount of this ChargesDetailsResponseDto.


        :param monthly_fee_amount: The monthly_fee_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :type: float
        """

        self._monthly_fee_amount = monthly_fee_amount

    @property
    def period_fee_periods(self):
        """Gets the period_fee_periods of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The period_fee_periods of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: list[MinPeriodFeePeriod]
        """
        return self._period_fee_periods

    @period_fee_periods.setter
    def period_fee_periods(self, period_fee_periods):
        """Sets the period_fee_periods of this ChargesDetailsResponseDto.


        :param period_fee_periods: The period_fee_periods of this ChargesDetailsResponseDto.  # noqa: E501
        :type: list[MinPeriodFeePeriod]
        """

        self._period_fee_periods = period_fee_periods

    @property
    def total_amount(self):
        """Gets the total_amount of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The total_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._total_amount

    @total_amount.setter
    def total_amount(self, total_amount):
        """Sets the total_amount of this ChargesDetailsResponseDto.


        :param total_amount: The total_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :type: float
        """

        self._total_amount = total_amount

    @property
    def usage_amount(self):
        """Gets the usage_amount of this ChargesDetailsResponseDto.  # noqa: E501


        :return: The usage_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :rtype: float
        """
        return self._usage_amount

    @usage_amount.setter
    def usage_amount(self, usage_amount):
        """Sets the usage_amount of this ChargesDetailsResponseDto.


        :param usage_amount: The usage_amount of this ChargesDetailsResponseDto.  # noqa: E501
        :type: float
        """

        self._usage_amount = usage_amount

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
        if issubclass(ChargesDetailsResponseDto, dict):
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
        if not isinstance(other, ChargesDetailsResponseDto):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
