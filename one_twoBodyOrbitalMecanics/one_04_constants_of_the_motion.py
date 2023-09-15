import math

from constants import earth, trig
from constants.earth import ReturnType


def solveForSpecificMechanicalEnergy(v: float, r: float, returntype: ReturnType) -> float:
    """
This solves for the specific mechanical energy \u03B5.
This is based on the equation 1.4-2 from the BMW book

    :param v:velocity
    :type v: float
    :param r: radius
    :type r: float
    :param returntype: what unit type are the inputs and outputs to be provided in
    :type returntype: ReturnType
    :return: mechanical energy
    :rtype: float
    """
    return (v*v/2.0) - (earth.getMu(returntype) / r)


def solveForVelocityFromSpecificEnergy(energy: float, r: float, type: ReturnType) -> float:
    """
This is a rewrite of the specific Mechanical energy
equation solving for v instead of energy (\u03B5).
This is based on equation 1.4-2 from the BMW book.
    :param energy: Specific energy
    :type energy: float
    :param r: Radius
    :type r: float
    :param type: what unit type are the inputs and outputs
    :type type: ReturnType
    :return: Velocity in specified units
    :rtype: float
    """
    toRoot = 2.0 * (earth.getMu(type)/r + energy)
    return math.sqrt(toRoot)


def solveForAngularMomentum(v: float, r: float) -> float:
    """
This solves for angular momentum.
This is based on the equation 1.4-3 from BMW
    :param v: Velocity
    :type v: float
    :param r: radius
    :type r: float
    :return: angualr velocity
    :rtype: float
    """
    return v*r


def solveForAngularmoment(v: float, r: float, FPA: float) -> float:
    """
This solves for the angular momentum at a specific spot.
This is based on equation 1.4-4 in BMW
    :param v: velocity
    :type v: float
    :param r: radius
    :type r: float
    :param FPA: flight path angle (degrees)
    :type FPA: float
    :return: angular momentum
    :rtype: float
    """
    fpa_in_rad = FPA * trig.degrees2radians
    return v * r * math.cos(fpa_in_rad)


def solveForFPAFromAngularMomentum(h: float, v: float, r: float) -> float:
    """
This solves for the FPA from the angular momentum equation.
This is a reorganization of the equation 1.4-4 solving for FPA vs h in the BMW book
    :param h: Angular Momentum
    :type h: float
    :param v: Velocity
    :type v: float
    :param r: radius
    :type r: float
    :return: FPA (degrees)
    :rtype: float
    """
    rv = r * v
    hOverRV = h/rv
    return math.acos(hOverRV) * trig.radians2degrees