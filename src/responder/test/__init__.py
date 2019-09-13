import unittest

from .helper import HelperTestCase


def make_suite():
    test_1 = unittest.TestLoader().loadTestsFromTestCase(HelperTestCase)

    suite = unittest.TestSuite([test_1, ])
    return suite


def do_tests():
    runner = unittest.TextTestRunner()
    test_suite = make_suite()
    runner.run(test_suite)
