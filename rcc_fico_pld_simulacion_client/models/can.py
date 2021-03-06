# coding: utf-8



import pprint
import re  # noqa: F401

import six

from rcc_fico_pld_simulacion_client.configuration import Configuration


class CAN(object):
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
        'identificador_can': 'str',
        'prelacion_origen': 'int',
        'prelacion_actual': 'int',
        'fecha_apertura_can': 'str',
        'fecha_cancelacion_can': 'str',
        'historico_can': 'str',
        'fecha_mrcan': 'str',
        'fecha_macan': 'str'
    }

    attribute_map = {
        'identificador_can': 'identificadorCAN',
        'prelacion_origen': 'prelacionOrigen',
        'prelacion_actual': 'prelacionActual',
        'fecha_apertura_can': 'fechaAperturaCAN',
        'fecha_cancelacion_can': 'fechaCancelacionCAN',
        'historico_can': 'historicoCAN',
        'fecha_mrcan': 'fechaMRCAN',
        'fecha_macan': 'fechaMACAN'
    }

    def __init__(self, identificador_can=None, prelacion_origen=None, prelacion_actual=None, fecha_apertura_can=None, fecha_cancelacion_can=None, historico_can=None, fecha_mrcan=None, fecha_macan=None, _configuration=None):  # noqa: E501
        """CAN - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._identificador_can = None
        self._prelacion_origen = None
        self._prelacion_actual = None
        self._fecha_apertura_can = None
        self._fecha_cancelacion_can = None
        self._historico_can = None
        self._fecha_mrcan = None
        self._fecha_macan = None
        self.discriminator = None

        if identificador_can is not None:
            self.identificador_can = identificador_can
        if prelacion_origen is not None:
            self.prelacion_origen = prelacion_origen
        if prelacion_actual is not None:
            self.prelacion_actual = prelacion_actual
        if fecha_apertura_can is not None:
            self.fecha_apertura_can = fecha_apertura_can
        if fecha_cancelacion_can is not None:
            self.fecha_cancelacion_can = fecha_cancelacion_can
        if historico_can is not None:
            self.historico_can = historico_can
        if fecha_mrcan is not None:
            self.fecha_mrcan = fecha_mrcan
        if fecha_macan is not None:
            self.fecha_macan = fecha_macan

    @property
    def identificador_can(self):
        """Gets the identificador_can of this CAN.  # noqa: E501

        Indica el estatus del cre??dito cuando es asociado a la no??mina. <table><thead><tr><th>Clave</th><th>Descripci??n</th></tr></thead><tbody><tr><td>01</td><td>Activo</td></tr><tr><td>02</td><td>Cancelado</td></tr></tbody></table>  # noqa: E501

        :return: The identificador_can of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._identificador_can

    @identificador_can.setter
    def identificador_can(self, identificador_can):
        """Sets the identificador_can of this CAN.

        Indica el estatus del cre??dito cuando es asociado a la no??mina. <table><thead><tr><th>Clave</th><th>Descripci??n</th></tr></thead><tbody><tr><td>01</td><td>Activo</td></tr><tr><td>02</td><td>Cancelado</td></tr></tbody></table>  # noqa: E501

        :param identificador_can: The identificador_can of this CAN.  # noqa: E501
        :type: str
        """

        self._identificador_can = identificador_can

    @property
    def prelacion_origen(self):
        """Gets the prelacion_origen of this CAN.  # noqa: E501

        Indica el orden de la prelacio??n origen.  # noqa: E501

        :return: The prelacion_origen of this CAN.  # noqa: E501
        :rtype: int
        """
        return self._prelacion_origen

    @prelacion_origen.setter
    def prelacion_origen(self, prelacion_origen):
        """Sets the prelacion_origen of this CAN.

        Indica el orden de la prelacio??n origen.  # noqa: E501

        :param prelacion_origen: The prelacion_origen of this CAN.  # noqa: E501
        :type: int
        """

        self._prelacion_origen = prelacion_origen

    @property
    def prelacion_actual(self):
        """Gets the prelacion_actual of this CAN.  # noqa: E501

        Indica el orden de la prelacio??n actual.  # noqa: E501

        :return: The prelacion_actual of this CAN.  # noqa: E501
        :rtype: int
        """
        return self._prelacion_actual

    @prelacion_actual.setter
    def prelacion_actual(self, prelacion_actual):
        """Sets the prelacion_actual of this CAN.

        Indica el orden de la prelacio??n actual.  # noqa: E501

        :param prelacion_actual: The prelacion_actual of this CAN.  # noqa: E501
        :type: int
        """

        self._prelacion_actual = prelacion_actual

    @property
    def fecha_apertura_can(self):
        """Gets the fecha_apertura_can of this CAN.  # noqa: E501

        Fecha asociada a la apertura de la domiciliacio??n CAN  # noqa: E501

        :return: The fecha_apertura_can of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._fecha_apertura_can

    @fecha_apertura_can.setter
    def fecha_apertura_can(self, fecha_apertura_can):
        """Sets the fecha_apertura_can of this CAN.

        Fecha asociada a la apertura de la domiciliacio??n CAN  # noqa: E501

        :param fecha_apertura_can: The fecha_apertura_can of this CAN.  # noqa: E501
        :type: str
        """

        self._fecha_apertura_can = fecha_apertura_can

    @property
    def fecha_cancelacion_can(self):
        """Gets the fecha_cancelacion_can of this CAN.  # noqa: E501

        Fecha asociada a la cancelacio??n de la domiciliacio??n CAN  # noqa: E501

        :return: The fecha_cancelacion_can of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._fecha_cancelacion_can

    @fecha_cancelacion_can.setter
    def fecha_cancelacion_can(self, fecha_cancelacion_can):
        """Sets the fecha_cancelacion_can of this CAN.

        Fecha asociada a la cancelacio??n de la domiciliacio??n CAN  # noqa: E501

        :param fecha_cancelacion_can: The fecha_cancelacion_can of this CAN.  # noqa: E501
        :type: str
        """

        self._fecha_cancelacion_can = fecha_cancelacion_can

    @property
    def historico_can(self):
        """Gets the historico_can of this CAN.  # noqa: E501

        Histo??rico CAN. Muestra los u??ltimos 36 meses de historia. (Cada valor representa un mes) <table><thead><tr><th>Clave</th><th>Descripci??n</th></tr></thead><tbody><tr><td>1</td><td>Activo</td></tr><tr><td>2</td><td>Cancelado</td></tr><tr><td>-</td><td>No reportado</td></tr></tbody></table>  # noqa: E501

        :return: The historico_can of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._historico_can

    @historico_can.setter
    def historico_can(self, historico_can):
        """Sets the historico_can of this CAN.

        Histo??rico CAN. Muestra los u??ltimos 36 meses de historia. (Cada valor representa un mes) <table><thead><tr><th>Clave</th><th>Descripci??n</th></tr></thead><tbody><tr><td>1</td><td>Activo</td></tr><tr><td>2</td><td>Cancelado</td></tr><tr><td>-</td><td>No reportado</td></tr></tbody></table>  # noqa: E501

        :param historico_can: The historico_can of this CAN.  # noqa: E501
        :type: str
        """

        self._historico_can = historico_can

    @property
    def fecha_mrcan(self):
        """Gets the fecha_mrcan of this CAN.  # noqa: E501

        Fecha ma??s reciente del histo??rico CAN)  # noqa: E501

        :return: The fecha_mrcan of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._fecha_mrcan

    @fecha_mrcan.setter
    def fecha_mrcan(self, fecha_mrcan):
        """Sets the fecha_mrcan of this CAN.

        Fecha ma??s reciente del histo??rico CAN)  # noqa: E501

        :param fecha_mrcan: The fecha_mrcan of this CAN.  # noqa: E501
        :type: str
        """

        self._fecha_mrcan = fecha_mrcan

    @property
    def fecha_macan(self):
        """Gets the fecha_macan of this CAN.  # noqa: E501

        Fecha ma??s antigua del histo??rico CAN (en que inicio el histo??rico)  # noqa: E501

        :return: The fecha_macan of this CAN.  # noqa: E501
        :rtype: str
        """
        return self._fecha_macan

    @fecha_macan.setter
    def fecha_macan(self, fecha_macan):
        """Sets the fecha_macan of this CAN.

        Fecha ma??s antigua del histo??rico CAN (en que inicio el histo??rico)  # noqa: E501

        :param fecha_macan: The fecha_macan of this CAN.  # noqa: E501
        :type: str
        """

        self._fecha_macan = fecha_macan

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
        if issubclass(CAN, dict):
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
        if not isinstance(other, CAN):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, CAN):
            return True

        return self.to_dict() != other.to_dict()
