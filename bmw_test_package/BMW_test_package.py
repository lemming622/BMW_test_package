import unittest

from bmw_test_package.chapter_tests.chapter_06 import six_02_tests, six_03_tests


def suite():
    suite = unittest.TestSuite()

    # chapter 6, section 2 tests
    suite.addTests(six_02_tests.suite())

    # chapter 6, section 3 tests
    suite.addTests(six_03_tests.suite())


    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
