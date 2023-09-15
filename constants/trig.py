import math


# Helper variables that are related to trig
degrees2radians = math.pi/180.0
radians2degrees = 180.0/math.pi
piover2 = math.pi/2.0


def csc(theta: float) -> float:
    """
    This performs the cosecant of the angle theta.  Assumes theta in radians.
    :param theta:
    :return:
    :rtype: float
    """
    return 1.0/math.sin(theta)


def cot(theta: float) -> float:
    """
    This performs the cotangent of the angle theta.  Assumes theta in radians.
    :param theta:
    :return:
    :rtype: float
    """
    return math.cos(theta)/math.sin(theta)
