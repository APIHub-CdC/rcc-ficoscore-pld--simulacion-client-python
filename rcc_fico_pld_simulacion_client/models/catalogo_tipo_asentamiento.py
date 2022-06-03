# coding: utf-8




import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_simulacion_client.configuration import Configuration


class CatalogoTipoAsentamiento(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    allowed enum values
    """
    _0 = "0"
    _1 = "1"
    _2 = "2"
    _3 = "3"
    _4 = "4"
    _5 = "5"
    _6 = "6"
    _7 = "7"
    _8 = "8"
    _9 = "9"
    _10 = "10"
    _11 = "11"
    _12 = "12"
    _13 = "13"
    _14 = "14"
    _15 = "15"
    _16 = "16"
    _17 = "17"
    _18 = "18"
    _19 = "19"
    _20 = "20"
    _21 = "21"
    _22 = "22"
    _23 = "23"
    _24 = "24"
    _25 = "25"
    _26 = "26"
    _27 = "27"
    _28 = "28"
    _29 = "29"
    _30 = "30"
    _31 = "31"
    _32 = "32"
    _33 = "33"
    _34 = "34"
    _35 = "35"
    _36 = "36"
    _37 = "37"
    _38 = "38"
    _39 = "39"
    _40 = "40"
    _41 = "41"
    _42 = "42"
    _43 = "43"
    _44 = "44"
    _45 = "45"
    _46 = "46"
    _47 = "47"
    _48 = "48"
    _49 = "49"
    _50 = "50"
    _51 = "51"
    _52 = "52"
    _53 = "53"
    _54 = "54"
    _55 = "55"

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
    }

    attribute_map = {
    }

    def __init__(self, _configuration=None):  # noqa: E501
        """CatalogoTipoAsentamiento - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration
        self.discriminator = None

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
        if issubclass(CatalogoTipoAsentamiento, dict):
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
        if not isinstance(other, CatalogoTipoAsentamiento):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CatalogoTipoAsentamiento):
            return True

        return self.to_dict() != other.to_dict()
