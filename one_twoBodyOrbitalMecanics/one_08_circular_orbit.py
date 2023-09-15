import math

from constants import earth
from constants.earth import ReturnType


def circularSatelliteSpeed(r: float, type: ReturnType) -> float:
    """
This solves for the Circular Satellite speed v :sub:`cs` .
This is the speed needed to put a satellite in circular orbit.
This is based on equation 1.8-2 from the BMW book
    :param r: radius or circular orbit in ft
    :type r:
    :param type:
    :type type:
    :return:
    :rtype:
    """
    return math.sqrt(earth.getMu(type) / r)
