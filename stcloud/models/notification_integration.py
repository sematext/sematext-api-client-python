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

class NotificationIntegration(object):
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
        'applicability': 'str',
        'create_date': 'datetime',
        'created_by_owner': 'bool',
        'creator_id': 'int',
        'id': 'int',
        'integration_type': 'str',
        'name': 'str',
        'params': 'dict(str, str)',
        'state': 'str',
        'user_id': 'int'
    }

    attribute_map = {
        'applicability': 'applicability',
        'create_date': 'createDate',
        'created_by_owner': 'createdByOwner',
        'creator_id': 'creatorId',
        'id': 'id',
        'integration_type': 'integrationType',
        'name': 'name',
        'params': 'params',
        'state': 'state',
        'user_id': 'userId'
    }

    def __init__(self, applicability=None, create_date=None, created_by_owner=None, creator_id=None, id=None, integration_type=None, name=None, params=None, state=None, user_id=None):  # noqa: E501
        """NotificationIntegration - a model defined in Swagger"""  # noqa: E501
        self._applicability = None
        self._create_date = None
        self._created_by_owner = None
        self._creator_id = None
        self._id = None
        self._integration_type = None
        self._name = None
        self._params = None
        self._state = None
        self._user_id = None
        self.discriminator = None
        if applicability is not None:
            self.applicability = applicability
        if create_date is not None:
            self.create_date = create_date
        if created_by_owner is not None:
            self.created_by_owner = created_by_owner
        if creator_id is not None:
            self.creator_id = creator_id
        if id is not None:
            self.id = id
        if integration_type is not None:
            self.integration_type = integration_type
        if name is not None:
            self.name = name
        if params is not None:
            self.params = params
        if state is not None:
            self.state = state
        if user_id is not None:
            self.user_id = user_id

    @property
    def applicability(self):
        """Gets the applicability of this NotificationIntegration.  # noqa: E501


        :return: The applicability of this NotificationIntegration.  # noqa: E501
        :rtype: str
        """
        return self._applicability

    @applicability.setter
    def applicability(self, applicability):
        """Sets the applicability of this NotificationIntegration.


        :param applicability: The applicability of this NotificationIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["NONE", "USE_ALWAYS"]  # noqa: E501
        if applicability not in allowed_values:
            raise ValueError(
                "Invalid value for `applicability` ({0}), must be one of {1}"  # noqa: E501
                .format(applicability, allowed_values)
            )

        self._applicability = applicability

    @property
    def create_date(self):
        """Gets the create_date of this NotificationIntegration.  # noqa: E501


        :return: The create_date of this NotificationIntegration.  # noqa: E501
        :rtype: datetime
        """
        return self._create_date

    @create_date.setter
    def create_date(self, create_date):
        """Sets the create_date of this NotificationIntegration.


        :param create_date: The create_date of this NotificationIntegration.  # noqa: E501
        :type: datetime
        """

        self._create_date = create_date

    @property
    def created_by_owner(self):
        """Gets the created_by_owner of this NotificationIntegration.  # noqa: E501


        :return: The created_by_owner of this NotificationIntegration.  # noqa: E501
        :rtype: bool
        """
        return self._created_by_owner

    @created_by_owner.setter
    def created_by_owner(self, created_by_owner):
        """Sets the created_by_owner of this NotificationIntegration.


        :param created_by_owner: The created_by_owner of this NotificationIntegration.  # noqa: E501
        :type: bool
        """

        self._created_by_owner = created_by_owner

    @property
    def creator_id(self):
        """Gets the creator_id of this NotificationIntegration.  # noqa: E501


        :return: The creator_id of this NotificationIntegration.  # noqa: E501
        :rtype: int
        """
        return self._creator_id

    @creator_id.setter
    def creator_id(self, creator_id):
        """Sets the creator_id of this NotificationIntegration.


        :param creator_id: The creator_id of this NotificationIntegration.  # noqa: E501
        :type: int
        """

        self._creator_id = creator_id

    @property
    def id(self):
        """Gets the id of this NotificationIntegration.  # noqa: E501


        :return: The id of this NotificationIntegration.  # noqa: E501
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this NotificationIntegration.


        :param id: The id of this NotificationIntegration.  # noqa: E501
        :type: int
        """

        self._id = id

    @property
    def integration_type(self):
        """Gets the integration_type of this NotificationIntegration.  # noqa: E501


        :return: The integration_type of this NotificationIntegration.  # noqa: E501
        :rtype: str
        """
        return self._integration_type

    @integration_type.setter
    def integration_type(self, integration_type):
        """Sets the integration_type of this NotificationIntegration.


        :param integration_type: The integration_type of this NotificationIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["PAGER_DUTY", "NAGIOS", "WEB_HOOKS", "WEB_HOOKS_TEMPLATE", "HIP_CHAT", "EMAIL_LIST", "TEMPORARY_EMAIL_LIST"]  # noqa: E501
        if integration_type not in allowed_values:
            raise ValueError(
                "Invalid value for `integration_type` ({0}), must be one of {1}"  # noqa: E501
                .format(integration_type, allowed_values)
            )

        self._integration_type = integration_type

    @property
    def name(self):
        """Gets the name of this NotificationIntegration.  # noqa: E501


        :return: The name of this NotificationIntegration.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this NotificationIntegration.


        :param name: The name of this NotificationIntegration.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def params(self):
        """Gets the params of this NotificationIntegration.  # noqa: E501


        :return: The params of this NotificationIntegration.  # noqa: E501
        :rtype: dict(str, str)
        """
        return self._params

    @params.setter
    def params(self, params):
        """Sets the params of this NotificationIntegration.


        :param params: The params of this NotificationIntegration.  # noqa: E501
        :type: dict(str, str)
        """

        self._params = params

    @property
    def state(self):
        """Gets the state of this NotificationIntegration.  # noqa: E501


        :return: The state of this NotificationIntegration.  # noqa: E501
        :rtype: str
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this NotificationIntegration.


        :param state: The state of this NotificationIntegration.  # noqa: E501
        :type: str
        """
        allowed_values = ["ACTIVE", "DISABLED", "DELETED"]  # noqa: E501
        if state not in allowed_values:
            raise ValueError(
                "Invalid value for `state` ({0}), must be one of {1}"  # noqa: E501
                .format(state, allowed_values)
            )

        self._state = state

    @property
    def user_id(self):
        """Gets the user_id of this NotificationIntegration.  # noqa: E501


        :return: The user_id of this NotificationIntegration.  # noqa: E501
        :rtype: int
        """
        return self._user_id

    @user_id.setter
    def user_id(self, user_id):
        """Sets the user_id of this NotificationIntegration.


        :param user_id: The user_id of this NotificationIntegration.  # noqa: E501
        :type: int
        """

        self._user_id = user_id

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
        if issubclass(NotificationIntegration, dict):
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
        if not isinstance(other, NotificationIntegration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
