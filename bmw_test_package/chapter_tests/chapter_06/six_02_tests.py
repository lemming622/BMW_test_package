import math
import unittest

from constants import earth, trig, conversions
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

        flightDistance = conversions.convertDeg2NM(freeFlightAngle)
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

        print()

    def test_GeneralBallisticMissileProblem3(self):
        """
        Example problem starting on page 294 of BMW book.
         A ballistic missile was observed to have a burnout speed and altitude of
         24,300 ft/sec and 258 nm respectively.  What must the be the maximum
         free-flight range capability of this missile?
        """

        print("Problem on pg. 294 - 1st ed")

        v_bo_ftpersec = 24300
        h_bo_nm = 258

        v_bo = conversions.convertFtPerSec2Canonical(v_bo_ftpersec)
        # should be 0.9402
        self.assertAlmostEqual(v_bo, 0.9402, 2, "Wrong v_bo")

        h_bo = conversions.convertNauticalMiles2Canonical(h_bo_nm)
        # should be 0.0749
        self.assertAlmostEqual(h_bo, 0.0749, 3, "Wrong h_bo")

        typeUsed = ReturnType.CANONICAL

        r_bo = earth.getMeanEquatorialRadius(typeUsed) + h_bo
        # should be 1.075
        self.assertAlmostEqual(r_bo, 1.075, 3, "Wrong r_bo")

        Q_bo = six_02_general_ballistic_missile_problem.solveForNondimentionalParametericParameter621(v_bo, r_bo, typeUsed)
        # should be 0.95
        self.assertAlmostEqual(Q_bo, 0.95, 1, "Wrong Q_bo")

        freeFlightRange = six_02_general_ballistic_missile_problem.solveForMaxRangeAngle(Q_bo)
        # should be 129
        # self.assertAlmostEqual(freeFlightRange, 129, 0, "Wrong free flight range")

        missileRange = earth.getMu(typeUsed)*freeFlightRange*trig.degrees2radians
        # should be 2.25
        self.assertAlmostEqual(missileRange, 2.25, 1, "Wrong Missile range")

        rangeNM = conversions.convertCanonical2NauticalMiles(missileRange)
        print("Max Range for this missile: %.4f nm" % rangeNM)
        print()

    def test_GeneralBallisticMissileProblem4(self):
        """
        Example problem starting on page 295 of BMW book.
         It is desired to maximize the payload of a new ballistic missile for a
         free-flight range of 8000nm.  The design burnout altitude has been fixed
         at 344nm.  What should be the design burnout speed?
        """

        print("Problem on pg. 295 - 1st ed")

        typeUsed = ReturnType.CANONICAL

        freeFlightRange_nm = 8000
        h_bo_nm = 344

        freeFlightRange = conversions.convertNauticalMiles2Canonical(freeFlightRange_nm)
        # should be 2.32
        self.assertAlmostEqual(freeFlightRange, 2.32, 2, "Wrong free flight range")

        freeFlightRangeDeg = freeFlightRange*trig.radians2degrees

        h_bo = conversions.convertNauticalMiles2Canonical(h_bo_nm)
        r_bo = earth.getMeanEquatorialRadius(typeUsed) + h_bo
        # should be 1.1
        self.assertAlmostEqual(r_bo, 1.1, 0, "Wrong r_bo")

        Q_bo = six_02_general_ballistic_missile_problem.solveForRequiredQAtMaxRange(freeFlightRangeDeg)
        # should be 0.957
        self.assertAlmostEqual(Q_bo, 0.957, 2, "Wrong Q_bo")

        v_bo = six_02_general_ballistic_missile_problem.solveForVelocity621(Q_bo, r_bo, typeUsed)
        # should be 0.933
        self.assertAlmostEqual(v_bo, 0.933, 2, "Wrong v_bo")

        v_bo_ftpersec = conversions.convertCanonical2FtPerSec(v_bo)

        print("Velocity at burnout => %.4f" % v_bo_ftpersec)
        print()

    def test_GeneralBallisticMissileProblem5(self):
        """
        Example problem starting on page 243 of BMW book 2d ed.
         During the test firing of a ballistic missile, the following measurements
         were made: h :sub: `bo` = 1275.6 km, v :sub: `bo` = 5.2702 km/s, and h :sub: `apogee` = 3189.1 km.
         Assuming a symmetrical trajectory, what was the free-flight range of the
         missile during the test in nautical miles?
        """

        print("Problem on pg. 243 - 2nd ed")
        h_bo = 1275.6  # km
        v_bo = 5.2702  # km/s
        h_apogee = 3189.1  # km

        typeUsed = ReturnType.METRIC

        r_bo = earth.getMeanEquatorialRadius(typeUsed) + h_bo
        r_apogee = earth.getMeanEquatorialRadius(typeUsed) + h_apogee

        # Q_bo and FPA_bo must be found

        # solve for the missiles's specific energy needs
        energy = one_04_constants_of_the_motion.solveForSpecificMechanicalEnergy(v_bo, r_bo, typeUsed)
        # should be -38.1914
        self.assertAlmostEqual(energy, -38.1914, 2, "Wrong energy")

        # solve for v_apogee using the specific energy equation
        v_apogee = one_04_constants_of_the_motion.solveForVelocityFromSpecificEnergy(energy, r_apogee, typeUsed)
        # v_apogee should be 2.6351 km
        self.assertAlmostEqual(v_apogee, 2.6351, 3, "Wrong v_apogee")

        # solve for the angular momentum of the missile around the ballistic ellipse
        angularMomentum = one_04_constants_of_the_motion.solveForAngularMomentum(v_apogee, r_apogee)
        # angular momentum should be 25211 km ^ 2 / s
        self.assertAlmostEqual(angularMomentum, 25211, -3, "Wrong angular momentum")

        # solve for the burnout flight path angle
        FPA_bo = one_04_constants_of_the_motion.solveForFPAFromAngularMomentum(angularMomentum, v_bo, r_bo)
        # FPA_bo should be 51.31781255 degrees or cos(FPA_bo) = 0.625
        self.assertAlmostEqual(FPA_bo, 51.31781255, 1, "Wrong FPA_bo")

        # solve for Q at burnout
        Q_bo = six_02_general_ballistic_missile_problem.solveForNondimentionalParametericParameter621(v_bo, r_bo, typeUsed)
        # Q_bo should be 0.533
        self.assertAlmostEqual(Q_bo, 0.533, 1, "Wrong Q_bo")

        # solve for free - flight angle double
        freeFlightAngle = six_02_general_ballistic_missile_problem.solveForFreeFlightAngle(Q_bo, FPA_bo)
        # free - flight angle should be 36.4
        self.assertAlmostEqual(freeFlightAngle, 36.4, 1, "Wrong Free flight angle")

        flightDistance = conversions.convertNM2KM(conversions.convertDeg2NM(freeFlightAngle))
        print("Free-Flight range => %.4f km" % flightDistance)
        print()


def suite():
    suite = unittest.TestSuite()
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem1'))
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem2'))
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem3'))
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem4'))

    # 2nd ed problems
    suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem5'))
    # suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem6'))
    # suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem7'))
    # suite.addTest(Six02Tests('test_GeneralBallisticMissileProblem8'))

    return suite


if __name__ == '__main__':
    unittest.main()

