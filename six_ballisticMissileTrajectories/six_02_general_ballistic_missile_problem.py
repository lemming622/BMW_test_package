import math
from multipledispatch import dispatch
from typing import Callable

from constants import earth, trig
from constants.earth import ReturnType
from one_twoBodyOrbitalMecanics import one_08_circular_orbit

six21: Callable[[float, float, ReturnType], float] = lambda v, r, rtype: ((v * v * r)/earth.getMu(rtype))
"""
Lambda function or solving equation 6.2-1 from the BMW book
"""


def solveForNondimentionalParametericParameter621(v: float, r: float, returntype: ReturnType) -> float:
    """
This solves for the Nondimentional Parameter Q.
This is based on the equation 6.2-1 in the BMW book
    :param v: velocity in ft
    :type v: float
    :param r: radius of circular orbit
    :type r: float
    :param returntype:
    :type returntype:
    :return: nondimentional number
    :rtype: float
    """
    return six21(v, r, returntype)


def solveForVelocity621(q: float, r: float, returntype: ReturnType) -> float:
    """
    This solves or the velocity given a `Q` , a given `r` , and unit system.
    this is based on the equation 6.2-1 from the BMW book.

    Args:
        q (float): nondimentional number
        r (float): radius of circular orbit
        returntype (ReturnType): How the units are provided and expected to be returned from

    Returns:
        float: The velocity
    """
    return math.sqrt(earth.getMu(returntype) * (q/r))


def solveForNondimentionalParameter622(v: float, r: float, returntype: ReturnType) -> float:
    """
    This solves for the nondimentional parameter `Q`.
    This is based on equation 6.2-2 from the BMW bok
    Args:
        v (float): velocity
        r (float):radius of the ballistic orbit
        returntype (ReturnType): How the units are given and expected to return

    Returns:
        float: the nondimentional parameter
    """
    v_cs = one_08_circular_orbit.circularSatelliteSpeed(r, returntype)
    return math.pow(v/v_cs, 2.0)


def solveForSemiMajorAxis(r: float, Q: float) -> float:
    """
    This makes a substitution for v :sup:`2` in the equation 1.4-2 and solves for the semi-major axis.
    Args:
        r (float):  radius
        Q (float): nondimentional parameter

    Returns:
        float: semi-major axis of the ballistic orbit
    """
    return r/(2.0 - Q)


def solveForNondimentionalParameter624(r: float, a: float) -> float:
    """
    This makes a substitution for v :sup:`2` in the equation 1.4-2 and solves for the nondimentional parameter.
    This is based on equation 6.2-4 from the BMW book.
    Args:
        r (float): radius
        a (float): semi-major axis of the parabolic orbit

    Returns:
        float: nondimentional number
    """
    return 2.0 - (r/a)


def solveForRadiusOfEllipse(p: float, e: float, v: float) -> float:
    """
    Solve for the radius of the ballistic orbit using the properties of an ellipse.
    This is based on equation 6.2-5 from the BMW book
    Args:
        p (float): the semi-latus rectum
        e (float): eccentricity
        v (float): total anomaly

    Returns:
        float: radius of the ballistic orbit
    """
    cosV = math.cos(v * trig.degrees2radians)
    return p/(1.0 + e*cosV)


def solveForAnomalyOfEllipse(p: float, e: float, r: float) -> float:
    """
    This solves for the anomaly angle of ballistic orbit using the properties of an ellipse.
    This is based on the equation 6.2-6 from the BMW book.
    Args:
        p (float): semi-latus rectum
        e (float): eccentricity
        r (float): radius of the ballistic orbit

    Returns:
        float: total anomaly
    """
    tmp = (p - r) / (e * r)
    return math.cos(tmp)*trig.radians2degrees


def solveForFreeFlightAngle(v_bo: float) -> float:
    """
    This solves for the free flight range based on the anomaly angle at burnout.
    This is based on the equation 6.2-7 from the BMW book
    Args:
        v_bo (float): anomaly angle at burnout (degrees)

    Returns:
        float: free flight range (degrees)
    """
    cosV = math.cos(v_bo * trig.degrees2radians)
    halfPsi = math.acos(-cosV)
    return halfPsi * 2.0 * trig.radians2degrees


def solveForAnomalyAngleAtBurnout(freeFlightAngle: float) -> float:
    """
    This solves for the anomaly angle at burnout based on the free flight range.
    This is based on the equation 6.2-7 from the BMW book
    Args:
        freeFlightAngle (float): Free Flight Angle at burnout (degrees)

    Returns:
        float: anomaly angle at burnout (degrees)
    """
    halfAngle = freeFlightAngle / 2.0
    cosHalfAngle = math.cos(halfAngle * trig.degrees2radians)
    return math.acos(-cosHalfAngle) * trig.radians2degrees


@dispatch(float, float)
def solveForFreeFlightAngle(Q_bo: float, FPA_bo: float) -> float:
    """
    This solves for the free-flight angle using the free-flight range equation.
    This uses Q at burnout and the flight path angle at burnout to find the free-flight angle
    This is based on equation 6.2-12 from the BMW book
    Args:
        Q_bo (float): Nondimentional Parameter at burnout
        FPA_bo (float): flight path angle at burn out (degrees)

    Returns:
        float: Free Flight Angle (degrees)
    """
    fpaRadians = FPA_bo * trig.degrees2radians
    cosFPA = math.cos(fpaRadians)
    cosFPASquared = cosFPA*cosFPA

    num = (1.0 - Q_bo * cosFPASquared)
    den = math.sqrt(1.0 + Q_bo*(Q_bo - 2.0) * cosFPASquared)
    cosPsiDiv2 = num/den

    # make sure the cos is between 1 and -1
    if not(1 >= cosPsiDiv2 >= -1):
        if math.isclose(cosPsiDiv2, 1.0):
            cosPsiDiv2 = 1.0
        elif math.isclose(cosPsiDiv2, -1.0):
            cosPsiDiv2 = -1
        else:
            raise Exception("Cannot perform calculation due to cosPsiDiv2 being out of bounds")

    output = math.acos(cosPsiDiv2) * 2.0 * trig.radians2degrees
    if math.isnan(output):
        output = 0.0

    return output


@dispatch(float, float, float, ReturnType)
def solveForFreeFlightAngle(r_bo: float, v_bo: float, FPA_bo: float, returntype: ReturnType) -> float:
    """
    This is a rewrite of the `solveForFreeFlightAngle` written to take in radius, velocity, and flight path angle at burnout.
    This is a modification of the equation 6.2-12 from the BMW book
    Args:
        r_bo (float): radius at burnout
        v_bo (float): velocity at burnout
        FPA_bo (float): flight path angle at burnout (degrees)
        returntype (ReturnType): How the units are given and expected to return

    Returns:
        float: Free Flight Angle (degrees)
    """
    Q_bo = solveForNondimentionalParametericParameter621(v_bo, r_bo, returntype)
    return solveForFreeFlightAngle(Q_bo, FPA_bo)


def solveForFlightPathAngle(freeFlightRange: float, Q_bo: float) -> (float, float):
    """
    This solves for the flight path angles that are represented by a Free-flight range angle and a Nondimentional Parameter.
    This is based on equation 6.2-16 from the BMW book
    Args:
        freeFlightRange (float): Free-Flight Range Angle in degrees
        Q_bo (float): Nondimentional Parameter at burnout

    Returns:
        (float, float): flight path angles
    """

    freeFlightRangeRad = freeFlightRange * trig.degrees2radians
    halfAngle = freeFlightRangeRad/2.0
    rightSide = (2.0 - Q_bo)/Q_bo * math.sin(halfAngle)

    asin = []
    asin.append(math.asin(rightSide))
    asin.append((180.0 - (asin[0] * trig.radians2degrees)) * trig.degrees2radians)

    asin[0] -= halfAngle
    asin[1] -= halfAngle

    fpa_bo = []
    fpa_bo.append((asin[0] * trig.radians2degrees)/2.0)
    fpa_bo.append((asin[1] * trig.radians2degrees)/2.0)

    return tuple(fpa_bo)


def solveForMaxBurnoutFlightPathAngle(freeFlightRange: float) -> float:
    """
    This solves for the flight path angle at burnout under the maximum range condition.
    This is based on the equation 6.2-18 from the BMW book
    Args:
        freeFlightRange (float): Free-flight Range angle (degrees)

    Returns:
        float: max burnout flight path angle (degrees)
    """

    return 0.25 * (180.0 - freeFlightRange)


def solveForMaxRangeAngle(Q_bo: float) -> float:
    """
    This solves for the maximum range obtainable from a given Q at burnout.
    This is based on the equation 6.2-19 from the BMW book
    Args:
        Q_bo (float): Q at burnout

    Returns:
        float: max range (degrees)
    """
    q = Q_bo/(2.0 - Q_bo)
    return (math.asin(q) * trig.radians2degrees) * 2.0


def solveForRequiredQAtMaxRange(freeFlightAngle: float) -> float:
    """
    This solves for the required Q at burnout need to achieve the range.
    This is based on the equation 6.2-20 from the BMW book
    Args:
        freeFlightAngle (float): Free flight angle at burnout (degrees)

    Returns:
        float: Q required at burnout to reach range
    """
    halfAngle = freeFlightAngle/2.0
    sinHalfAngle = math.sin(halfAngle * trig.degrees2radians)

    return (2.0 * sinHalfAngle) / (1.0 + sinHalfAngle)


def solveForEccentricAnomalyFromMaxRange(e: float, freeFlightRange: float) -> float:
    """
    This solves for the eccentric anomaly based on the free flight range and eccentricity.
    This is based on equation 6.2-21 from the BMW book
    Args:
        e (float): eccentricity
        freeFlightRange (float): free Flight Range

    Returns:
        float: eccentric anomaly
    """
    halfAngle = freeFlightRange/2.0
    cosHalfAngle = math.cos(halfAngle * trig.degrees2radians)
    tmp = (e - cosHalfAngle)/(1.0 - e*cosHalfAngle)
    return math.acos(tmp) * trig.radians2degrees


def solveForTimeOfFreeFlight(capE: float, lowE: float, a: float, returntype: ReturnType) -> float:
    """
    This solves for the free flight time based on the provided eccentric anomaly, eccentricity, semi-major axis and unit system.
    This is based on equation 6.2-22 from the BMW book.
    Args:
        capE (float): Eccentric anomaly `E`
        lowE (float): eccentricity `e`
        a (float): semi-major axis
        returntype (ReturnType): Unit system to be used

    Returns:
        float: time for free flight in ReturnType units
    """
    ERads = capE * trig.degrees2radians
    tmp1 = math.sqrt(math.pow(a, 3.0) / earth.getMu(returntype))
    tmp2 = math.pi - ERads + (lowE * math.sin(ERads))

    return 2.0 * tmp1 * tmp2


def solveForFreeFlightTime(r_bo: float, returntype: ReturnType) -> float:
    """
    This solves for the free-flight time of circular orbit based on the burnout altitude.
    This is based on the equation 6.2-23 from the BWM book.
    Args:
        r_bo (float): Altitude at burnout
        returntype (ReturnType): unit system being used

    Returns:
        float: free flight time
    """
    r3 = math.pow(r_bo, 3.0)
    root = math.sqrt(r3/earth.getMu(returntype))

    return 2.0 * math.pi * root
