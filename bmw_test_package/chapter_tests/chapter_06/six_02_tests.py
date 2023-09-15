import math
import unittest

from constants import earth, trig
from constants.conversions import convertDeg2NM
from constants.earth import ReturnType
from one_twoBodyOrbitalMecanics import one_04_constants_of_the_motion
from six_ballisticMissileTrajectories import six_02_general_ballistic_missile_problem


class Six02Tests(unittest.TestCase):
    """
    Integration tests to work through Chapter 6, Section 2 word problems of the BMW book
    """

    def test_GeneralBallisticMissileProblem1(self):
        """
        Example problem starting on page 290 of BMW book.

        During the test firing of a ballistic missile, the following measurements
        were made: h_bo = 1/5 DU, v_bo = 2/3 DU/TU, and h_apogee = 0.5 DU.
        Assuming a symmetrical trajectory, what was the free-flight range of the
        missile during the test in nautical miles?
        """
        print("Problem on pg. 290 - 1st ed")

        h_bo = 1.0/5.0  # distance units
        v_bo = 2.0/3.0  # distance units/time units
        h_apogee = 0.5  # distance units

        typeUsed = ReturnType.CANONICAL

        r_bo = earth.getMeanEquatorialRadius(typeUsed) + h_bo
        r_apogee = earth.getMeanEquatorialRadius(typeUsed) + h_apogee

        # Q_bo and FPA_bo must be found

        # solve for the missile's specific energy needs to be found
        energy = one_04_constants_of_the_motion.solveForSpecificMechanicalEnergy(v_bo, r_bo, typeUsed)
        # energy should be -11/18 DU^2/TU^2 or -0.61111
        self.assertAlmostEqual(energy, -11/18, 3, "Wrong specific energy")

        # solve for v_apogee using the specific energy equation
        v_apogee = one_04_constants_of_the_motion.solveForVelocityFromSpecificEnergy(energy, r_apogee, typeUsed)
        # v_apogee should be 1/3 DU/TU or 0.3333
        self.assertAlmostEqual(v_apogee, 1/3, 3, "Wrong velocity at apogee")

        # solve for the angular momentum of the missile around the ballistic ellipse
        angularMomentum = one_04_constants_of_the_motion.solveForAngularMomentum(v_apogee, r_apogee)
        # angularMomentum should be 1/2 DU^2/TU or 0.5
        self.assertAlmostEqual(angularMomentum, 1/2, 3, "Wrong angular momentum")

        # solve for the burnout flight path angle
        FPA_bo = one_04_constants_of_the_motion.solveForFPAFromAngularMomentum(angularMomentum, v_bo, r_bo)
        # FPA_bo should be 51.31781255 degrees or cos(FPA_bo) = 0.625
        self.assertAlmostEqual(FPA_bo, 51.31781255, 3, "Wrong FPA")

        # solve for Q at burnout
        Q_bo = six_02_general_ballistic_missile_problem.solveForNondimentionalParametericParameter621(v_bo, r_bo, typeUsed)
        # Q_bo should be 0.533
        self.assertAlmostEqual(Q_bo, 0.533, 3, "Wrong Q_bo")

        # solve for free-flight angle
        freeFlightAngle = six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(Q_bo, FPA_bo)
        # free-flight angle should be 36.4
        self.assertAlmostEqual(freeFlightAngle, 36.4, 1, "Wrong free flight angle")

        flightDistance = convertDeg2NM(freeFlightAngle)
        print("Free-Flight range => %.4f nm" % flightDistance)
        print()

#    def test_something(self):
#        self.assertEqual(True, False)  # add assertion here


if __name__ == '__main__':
    unittest.main()

