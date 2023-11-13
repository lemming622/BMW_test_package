import unittest

from bmw_test_package.chapter_tests.chapter_06 import six_02_tests, six_03_tests


def suite():
    suiteRun = unittest.TestSuite()

    # chapter 6, section 2 tests
    suiteRun.addTests(six_02_tests.suite())

    # chapter 6, section 3 tests
    suiteRun.addTests(six_03_tests.suite())

    return suiteRun


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
