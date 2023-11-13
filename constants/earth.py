from enum import Enum

import numpy as np


class EarthConstants():
    _name = ''
    _mu = np.NaN
    _radius = np.NaN

    def __init__(self, name, mu, radius):
        self._name = name
        self._mu = mu
        self._radius = radius

    def getName(self):
        return self._name

    def getMu(self):
        return self._mu

    def getRadius(self):
        return self._radius


class ReturnType(Enum):
    ENGLISH = EarthConstants('English', 1.407654e16, 2.092567257e7)
    METRIC = EarthConstants('METRIC', 3.986012e5, 6378.145)
    CANONICAL = EarthConstants('CANONICAL', 1.0, 1.0)

# mean equatorial radius
# rCanonical = 1.0
# rEnglish = 2.092567257e7
# rMetric = 6378.145

# gravitational parameter
# muEnglish = 1.407654e16
# muMetric = 3.986012e5
# muCanonical = 1.0


def getMu(returntype: ReturnType) -> float:
    """
    Returns gravitational constant based on what units are needed
    :rtype: float
    :type returntype: ReturnType
    :param returntype: Which unit type is this expected to return
    :return: gravitational constant in the unit specified
    """
    return returntype.value.getMu()
    # if returntype == ReturnType.ENGLISH:
    #     return muEnglish
    # elif returntype == ReturnType.METRIC:
    #     return muMetric
    # elif returntype == ReturnType.CANONICAL:
    #     return muCanonical
    # else:
    #     raise AssertionError(returntype.name() + " is not a possible choice.  Please try again.")


def getMeanEquatorialRadius(returntype: ReturnType) -> float:
    """
    Returns Mean Equatorial Radius based on what units are needed
    :rtype: float
    :type returntype: ReturnType
    :param returntype: Which unit type is this expected to return
    :return: Mean Equatorial Radius in the unit specified
    """
    return returntype.value.getRadius()
    # if returntype == ReturnType.ENGLISH:
    #     return rEnglish
    # elif returntype == ReturnType.METRIC:
    #     return rMetric
    # elif returntype == ReturnType.CANONICAL:
    #     return rCanonical
    # else:
    #     raise AssertionError(returntype.name() + " is not a possible choice.  Please try again.")
