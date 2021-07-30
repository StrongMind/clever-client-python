# coding: utf-8

"""
    Clever Data API

    Serves the Clever Data API  # noqa: E501

    OpenAPI spec version: 3.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from clever_client.configuration import Configuration


class SectionsDeleted(object):
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
        'data': 'SectionObject',
        'id': 'str',
        'created': 'str'
    }

    attribute_map = {
        'data': 'data',
        'id': 'id',
        'created': 'created'
    }

    def __init__(self, data=None, id=None, created=None, _configuration=None):  # noqa: E501
        """SectionsDeleted - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._data = None
        self._id = None
        self._created = None
        self.discriminator = None

        if data is not None:
            self.data = data
        if id is not None:
            self.id = id
        if created is not None:
            self.created = created

    @property
    def data(self):
        """Gets the data of this SectionsDeleted.  # noqa: E501


        :return: The data of this SectionsDeleted.  # noqa: E501
        :rtype: SectionObject
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this SectionsDeleted.


        :param data: The data of this SectionsDeleted.  # noqa: E501
        :type: SectionObject
        """

        self._data = data

    @property
    def id(self):
        """Gets the id of this SectionsDeleted.  # noqa: E501


        :return: The id of this SectionsDeleted.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SectionsDeleted.


        :param id: The id of this SectionsDeleted.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def created(self):
        """Gets the created of this SectionsDeleted.  # noqa: E501


        :return: The created of this SectionsDeleted.  # noqa: E501
        :rtype: str
        """
        return self._created

    @created.setter
    def created(self, created):
        """Sets the created of this SectionsDeleted.


        :param created: The created of this SectionsDeleted.  # noqa: E501
        :type: str
        """

        self._created = created

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
        if issubclass(SectionsDeleted, dict):
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
        if not isinstance(other, SectionsDeleted):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, SectionsDeleted):
            return True

        return self.to_dict() != other.to_dict()
