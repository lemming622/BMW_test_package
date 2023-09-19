import math
import unittest

from constants import earth, trig, conversions
from constants.earth import ReturnType
from one_twoBodyOrbitalMecanics import one_04_constants_of_the_motion
from six_ballisticMissileTrajectories import six_02_general_ballistic_missile_problem, six_03_launching_errors_on_range


class Six03Tests(unittest.TestCase):

    def test_LaunchingErrorsOnRange1(self):
        """
        Example problem starting on page 305 of BMW book.

        A ballistic missile has the following nominal burnout conditions:
        v :sub: `bo` = 0.905 DU/TU
        r :sub: `bo` = 1.1 DU
        fpa :sub: `bo` = 30 deg

        The following errors exist at burnout:
        \u0394 v :sub: `bo` = -5x10^-5 DU/TU
        \u0394 r :sub: `bo` = 5x10^-4 DU
        \u0394 fpa :sub: `bo` = -10^-4 radians

        How far will the missile miss the target?
        What will be the direction of  the miss relative to the trajectory plane?
        """
        print("Problem on pg. 305 - 1st ed")

        typeUsed = ReturnType.CANONICAL

        v_bo = 0.905  # DU/TU
        r_bo = 1.1  # DU
        fpa_bo = 30.0  # deg

        dv_bo = -5e-5  # DU/TU
        dr_bo = 5e-4  # DU
        dfpa_bo = -1e-4  # deg

        freeRangeAngle = six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(r_bo, v_bo, fpa_bo, typeUsed)
        # should be ~100
        self.assertAlmostEqual(freeRangeAngle, 100, delta=2, msg="Wrong free flight angle")

        # to solve for total down range error all of the individual errors have to be found first

        icRangeError = six_03_launching_errors_on_range.solveForInfluenceCoefficientBurnoutHeight(r_bo, v_bo, fpa_bo, freeRangeAngle, typeUsed)
        # should be 2.7535

        icVelocityError = six_03_launching_errors_on_range.solveForInfluenceCoefficientBurnoutVelocity(r_bo, v_bo, fpa_bo, freeRangeAngle, typeUsed)
        # should be 6.649

        icVelocityErrorAtl = six_03_launching_errors_on_range.solveForInfluenceCoefficientBurnoutVelocityAlternative(r_bo, v_bo, icRangeError)
        # should be 6.649

        icFPAError = six_03_launching_errors_on_range.solveForInfluenceCoefficientFPAError(freeRangeAngle, fpa_bo)
        # should be -1.21

        fpaError = icFPAError * dfpa_bo
        rError = icRangeError * dr_bo
        vError = icVelocityError * dv_bo

        # sum all of the errors up
        errorTot = fpaError + rError + vError
        # should be 11.56e-4

        # convert error to NM
        errorNM = conversions.convertCanonical2NauticalMiles(errorTot)
        print("%.4f nm" % errorNM, end=" - ")
        if errorNM > 0:
            print("Overshoot")
        else:
            print("Undershoot")

        print()



def suite():
    suite = unittest.TestSuite()
    suite.addTest(Six03Tests('test_LaunchingErrorsOnRange1'))

    return suite

if __name__ == '__main__':
    unittest.main()
