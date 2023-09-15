

from typing import Callable

# Python migration of constant variables from Java source.

"""
This converts from Canonical units to feet
"""
c2ft: float = 2.092567257e7
CANONICAL2FEET: Callable[[float], float] = lambda c: c * c2ft


def convertCanonical2Feet(c: float) -> float:
    """
    This converts from Canonical units to feet
    :param c: Canonical input unit
    :type c: float
    :return: input converted to feet
    :rtype: float
    """
    return CANONICAL2FEET(c)


ft2c: float = 1.0 / c2ft
"""
This converts from feet to Canonical units
"""


FEET2CANONICAL: Callable[[float], float] = lambda ft: ft * ft2c
"""
Lambda function for Unit conversion of cononical to miles
"""


def convertFeet2Canonical(ft: float) -> float:
    """
    This converts from Feet to Canonical units
    :param ft: Feet input unit
    :type ft: float
    :return: Canonical unit return
    :rtype: float
    """
    return FEET2CANONICAL(ft)


c2mi: float = 3963.195563
"""
Unit conversion for cononical to miles
"""


CANONICAL2MILES: Callable[[float], float] = lambda c: c * c2mi
"""
Lambda function for Unit conversion of cononical to miles
"""


def convertCanonical2Miles(c: float) -> float:
    """
    This converts from Canonical units to miles

    :param c: Canonical unit input
    :type c: float
    :return: miles output
    :rtype: float
    """
    return CANONICAL2MILES(c)


mi2c = 1.0 / c2mi
MILES2CANONICAL: Callable[[float], float] = lambda mi: mi * mi2c
def convertMiles2Canonical(mi: float) -> float:
    """
    This converts from miles to canonical units
    :param mi:
    :type mi:
    :return:
    :rtype:
    """
    return MILES2CANONICAL(mi)


c2nm = 3443.922786
CANONICAL2NM: Callable[[float], float] = lambda c: c * c2nm
def convertCanonical2NauticalMiles(c: float) -> float:
    """
    This converts from canonical units to nautical miles
    :param c:
    :type c:
    :return:
    :rtype:
    """
    return CANONICAL2NM(c)


nm2c = 1.0 / c2nm
NM2CANONICAL: Callable[[float], float] = lambda nm: nm * nm2c
def convertNauticalMiles2Canonical(nm: float) -> float:
    """

    :param nm:
    :type nm:
    :return:
    :rtype:
    """
    return NM2CANONICAL(nm)


c2km = 6378.145
CANONICAL2KM: Callable[[float], float] = lambda c: c * c2km
def convertCanonical2Km(c: float) -> float:
    """

    :param c:
    :type c:
    :return:
    :rtype:
    """
    return CANONICAL2KM(c)


km2c = 1.0 / c2km
KM2CANONICAL: Callable[[float], float] = lambda km: km * km2c
def convertKM2Canonical(km: float) -> float:
    """

    :param km:
    :type km:
    :return:
    :rtype:
    """
    return KM2CANONICAL(km)


c2sec = 806.8118744
CANONICAL2SEC: Callable[[float], float] = lambda c: c * c2sec
def convertCanonical2Seconds(c: float) -> float:
    """

    :param c:
    :type c:
    :return:
    :rtype:
    """
    return CANONICAL2SEC(c)


sec2c = 1.0 / c2sec
SEC2CANONICAL: Callable[[float], float] = lambda sec: sec * sec2c
def convertSeconds2Canonical(sec: float) -> float:
    """

    :param sec:
    :type sec:
    :return:
    :rtype:
    """
    return SEC2CANONICAL(sec)


c2ftPerSec = 25936.24764
CANONICAL2FTPERSEC: Callable[[float], float] = lambda c: c * c2ftPerSec
def convertCanonical2FtPerSec(c: float) -> float:
    """

    :param c:
    :type c:
    :return:
    :rtype:
    """
    return CANONICAL2FTPERSEC(c)


ftPerSec2c = 1.0 / c2ftPerSec
FTPERSEC2CANONICAL: Callable[[float], float] = lambda ftPerSec: ftPerSec * ftPerSec2c
def convertFtPerSec2Canonical(ftPerSec: float) -> float:
    """

    :param ftPerSec:
    :type ftPerSec:
    :return:
    :rtype:
    """
    return FTPERSEC2CANONICAL(ftPerSec)


c2kmPerSec = 7.90536828
CANONICAL2KMPERSEC: Callable[[float], float] = lambda c: c * c2kmPerSec
def convertCanonical2KmPerSec(c: float) -> float:
    """

    :param c:
    :type c:
    :return:
    :rtype:
    """
    return CANONICAL2KMPERSEC(c)


kmPerSec2c = 1.0 / c2kmPerSec
KMPERSEC2CANONICAL: Callable[[float], float] = lambda kmPerSec: kmPerSec * kmPerSec2c
def convertKmPerSec2Canonical(kmPerSec: float) -> float:
    """

    :param kmPerSec:
    :type kmPerSec:
    :return:
    :rtype:
    """
    return KMPERSEC2CANONICAL(kmPerSec)


degrees2NauticalMiles = 60.0
DEG2NM: Callable[[float], float] = lambda deg: deg * degrees2NauticalMiles
def convertDeg2NM(deg: float) -> float:
    """

    :param deg:
    :type deg:
    :return:
    :rtype:
    """
    return DEG2NM(deg)


nauticalMiles2KiloMeters = 1.852
NM2KM: Callable[[float], float] = lambda nm: nm * nauticalMiles2KiloMeters
def convertNM2KM(nm: float) -> float:
    """

    :param nm:
    :type nm:
    :return:
    :rtype:
    """
    return NM2KM(nm)


kiloMeters2NauticalMiles = 1.0 / nauticalMiles2KiloMeters
KM2NM: Callable[[float], float] = lambda km: km * kiloMeters2NauticalMiles
def convertKM2NM(km: float) -> float:
    """

    :param km:
    :type km:
    :return:
    :rtype:
    """
    return KM2NM(km)


degrees2Kilometers = 111.12
DEG2KM: Callable[[float], float] = lambda deg: deg * degrees2Kilometers
def convertDEG2KM(deg: float) -> float:
    """

    :param deg:
    :type deg:
    :return:
    :rtype:
    """
    return DEG2KM(deg)
