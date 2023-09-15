import math

from constants import trig


def solveforEccentricAnomoly(e: float, v: float) -> float:
    """
    This solves for the eccentric anomaly.
    This is based on the equation 4.2-8 from the BMW book
    :param e: eccentricity
    :type e: float
    :param v: True anomaly
    :type v: float
    :return: eccentric anomaly
    :rtype: float
    """
    cosV = math.cos(v * trig.degrees2radians)
    tmp = (e + cosV)/(1.0 + e*cosV)
    return math.acos(tmp)*trig.radians2degrees
