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

    def test_GeneralBallisticMissileProblem2(self):
        """
        Example problem starting on page 291 of BMW book.
        A missile's coordinates at burnout are: 30N, 60E.  Reentry is planned for
        30S, 60W.  Burnout velocity is 1.0817 DU/TU and altitude is 0.025DU.
        psi is less than 180.

        What must the flight-path angle be at burnout?
        """
        print("Problem on pg. 291 - 1st ed")

        v_bo = 1.0817  # in DU/TU
        h_bo = 0.025  # in DU
        lat_bo = 30.0
        lon_bo = 60.0
        lat_re = -30.0
        lon_re = -60.0

        typeUsed = ReturnType.CANONICAL

        # Find elliptical radius at burnout
        r_bo = earth.getMeanEquatorialRadius(typeUsed) + h_bo

        # Find Q_bo
        Q_bo = six_02_general_ballistic_missile_problem.solveForNondimentionalParametericParameter621(v_bo, r_bo, typeUsed)
        # should be 1.2
        self.assertAlmostEqual(Q_bo, 1.2, 2, " Wrong Q_bo")

        # Find psi from spherical trig
        deltaLat = lat_bo - lat_re
        # should be 60
        self.assertAlmostEqual(deltaLat, 60, 1, "Wrong deltaLat")
        deltaLatRad = deltaLat * trig.degrees2radians

        deltaLon = lon_bo - lon_re
        # should be 120
        self.assertAlmostEqual(deltaLon, 120, 1, "Wrong deltaLon")
        deltaLonRad = deltaLon * trig.degrees2radians

        cosLat = math.cos(deltaLatRad)
        sinLat = math.sin(deltaLatRad)
        cosLon = math.cos(deltaLonRad)
        sinLon = math.sin(deltaLonRad)

        cosFreeFlightAngle = cosLat*cosLon + sinLat*sinLon*cosLon
        # should be -0.625
        self.assertAlmostEqual(cosFreeFlightAngle, -0.625, 3, "Wrong cosFreeFlightAngle")

        freeFlightAngle = math.acos(cosFreeFlightAngle) * trig.radians2degrees
        # should be 128.68218745

        # find flight path angles
        fpa_bo = six_02_general_ballistic_missile_problem.solveForFlightPathAngle(freeFlightAngle, Q_bo)
        # should be (0, 39.36)
        self.assertAlmostEqual(fpa_bo[1], 39.36, 1, "Wrong FPA_bo")

        if Q_bo < 1:
            if freeFlightAngle < 180:
                print("Burnout flight path angles:> %.4f $.4f" % fpa_bo[0], fpa_bo[1])
            else:
                print("It is impossible to the FPA at burnout for current conditions")
        elif Q_bo > 1:
            print("Burnout flight path angle:> %.4f" % fpa_bo[1])


    def test_GeneralBallisticMissileProblem3(self):
        """
        Example problem starting on page 294 of BMW book.
         A ballistic missile was observed to have a burnout speed and altitude of
         24,300 ft/sec and 258 nm respectively.  What must the be the maximum
         free-flight range capability of this missile?
        """



def suite():
    suite = unittest.TestSuite()
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem1'))
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem2'))
    return suite

if __name__ == '__main__':
    unittest.main()

