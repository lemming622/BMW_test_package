import math

from constants import trig, earth
from constants.earth import ReturnType


def solveForCrossRangeErrorLateral(rangeAngle: float, lateralError: float) -> float:
    """
    This solves for the cross range error based on a thrust cutoff error.
     This is based on equation 6.3-1 in the BMW book
    Args:
        rangeAngle (float):
        lateralError (float):

    Returns:
        float: Lateral cross range error
    """
    rangeAngleRad = rangeAngle * trig.degrees2radians
    latErRad = lateralError * trig.degrees2radians

    sinPsi = math.sin(rangeAngleRad)
    cosPsi = math.cos(rangeAngleRad)
    cosDeltaX = math.cos(latErRad)

    cosDeltaC = sinPsi*sinPsi + cosPsi*cosPsi*cosDeltaX
    return math.acos(cosDeltaC)*trig.radians2degrees


def solveForCrossRangeErrorLateralSmallAngleApprox(rangeAngle: float, lateralError: float) -> float:
    """
    This solves for the cross range error based on a thrust cutoff error using small angle approximation.
     This is based on equation 6.3-2 in the BMW book
    Args:
        rangeAngle (float):
        lateralError (float):

    Returns:
        float: lateral cross range error
    """
    rangeAngleRad = rangeAngle * trig.degrees2radians
    latErRad = lateralError * trig.degrees2radians

    deltaC = latErRad * math.cos(rangeAngleRad)
    return deltaC*trig.radians2degrees


def solveForCrossRangeErrorAzimuthal(rangeAngle: float, azimuthalError: float) -> float:
    """
    This solves for the cross range error based on a thrust cutoff error.
     This is based on equation 6.3-3 in the BMW book
    Args:
        rangeAngle (float):
        azimuthalError (float):

    Returns:
        float: azimuthal cross range error
    """
    rangeAngleRad = rangeAngle*trig.degrees2radians
    azErRad = azimuthalError*trig.degrees2radians

    sinPsi = math.sin(rangeAngleRad)
    cosPsi = math.cos(rangeAngleRad)
    cosDeltaB = math.cos(azErRad)

    cosDeltaC = cosPsi*cosPsi + sinPsi*sinPsi*cosDeltaB
    return math.acos(cosDeltaC)*trig.radians2degrees


def solveForCrossRangeErrorAzimuthalSmallAngleApprox(rangeAngle: float, azimuthalError: float) -> float:
    """
    This solves for the cross range error based on a thrust cutoff error using small angle approximation.
     This is based on equation 6.3-4 in the BMW book
    Args:
        rangeAngle (float):
        azimuthalError (float):

    Returns:
        float: azimuthal cross range error
    """
    rangeAngleRad = rangeAngle*trig.degrees2radians
    azErRad = azimuthalError*trig.degrees2radians

    deltaC = azErRad*math.sin(rangeAngleRad)
    return deltaC*trig.radians2degrees


def solveForDownRangeError(Q_bo: float, fpa_bo: float) -> float:
    """
    This solves for the down range error of a ballistic missile assuming errors to the burnout flight path angle.
     This is based on equation 6.3-10 from the BMW book
    Args:
        Q_bo (float): Q at burnout
        fpa_bo (float): FPA at burnout (degrees)

    Returns:
        float: down range error (degrees)
    """
    fpa_boRad = fpa_bo*trig.degrees2radians

    cscFpaBo = trig.csc(2.0 * fpa_boRad)
    cotFpaBo = trig.cot(fpa_boRad)

    cosPsi = 2.0/Q_bo * cscFpaBo - cotFpaBo
    return math.acos(cosPsi)*2.0*trig.radians2degrees


def solveForInfluenceCoefficientFPAError (freeFlightRange: float, fpa_bo: float) -> float:
    """
    This solves for the influence coefficient as the partial derivative.
     This is based on equation 6.3-13 from the BMW book
    Args:
        freeFlightRange (float):
        fpa_bo (float):

    Returns:
        float: FPA error
    """
    twoFpa = 2.0*fpa_bo
    numHelper = (freeFlightRange + twoFpa)*trig.degrees2radians
    denHelper = (twoFpa*trig.degrees2radians)

    num = 2.0 * math.sin(numHelper)
    den = math.sin(denHelper)

    return (num/den) - 2.0


def solveForInfluenceCoefficientBurnoutHeight(r_bo: float, v_bo: float, fpa_bo: float, freelightRange: float, returntype: ReturnType) -> float:
    """
    This solves for the burnout height influence coefficient to determine the down range error.
     This is based on equation 6.3-16 from the BMW book
    Args:
        r_bo (float): burnout height
        v_bo (float): burnout velocity
        fpa_bo (float): burnout fpa
        freelightRange (float): free flight range of missile
        returntype (ReturnType): unit system being used

    Returns:
        float: burnout height influence coefficient
    """
    tmp1 = (4.0 * earth.getMu(returntype))/(v_bo*v_bo * r_bo*r_bo)

    halfAngle = (freelightRange*trig.degrees2radians)/2.0
    fpaRad = 2.0*fpa_bo*trig.degrees2radians

    sinHalfAngle = math.sin(halfAngle)

    tmp2 = (sinHalfAngle*sinHalfAngle)/math.sin(fpaRad)

    return tmp1*tmp2


def solveForInfluenceCoefficientBurnoutVelocity(r_bo: float, v_bo: float, fpa_bo: float, freeFlightRange: float, returntype: ReturnType) -> float:
    """
    This solves for the burnout velocity influence coefficient to determine
    the down range error.
      this is based on equation 6.3-18 from the BMW book
    Args:
        r_bo (float): burnout height
        v_bo (float): burnout velocity
        fpa_bo (float): burnout FPA (degrees)
        freeFlightRange (float): free flight range of missile (degrees)
        returntype (ReturnType): unit system being used

    Returns:
        float: burnout velocity influence coefficient
    """
    tmp1 = (8.0 * earth.getMu(returntype)) / (math.pow(v_bo, 3.0) * r_bo)

    halfAngle = freeFlightRange*trig.degrees2radians/2.0
    fpaRad = 2.0*fpa_bo*trig.degrees2radians

    sinHalfAngle = math.sin(halfAngle)

    tmp2 = (sinHalfAngle*sinHalfAngle)/math.sin(fpaRad)

    return tmp1*tmp2

def solveForInfluenceCoefficientBurnoutVelocityAlternative(r_bo: float, v_bo: float, icHeightError: float) -> float:
    """
    This solves for the burnout velocity influence coefficient to determine
    the down range error.
     this is based on equation 6.3-18 from the BMW book
    Args:
        r_bo (float): burnout height
        v_bo (float): burnout velocity
        icHeightError (float): burn out height influence coefficient

    Returns:
        float: burnout velocity influence coefficient
    """
    tmp1 = (2.0*r_bo)/v_bo
    return tmp1*icHeightError
