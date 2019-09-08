import unittest

from runkod.helper import resolve_path


class HelperTestCase(unittest.TestCase):

    def test_00(self):
        """
        Basic path to file
        """
        result = resolve_path('')
        expected = '/index.html'
        self.assertEqual(result, expected)

        result = resolve_path('/')
        expected = '/index.html'
        self.assertEqual(result, expected)

        result = resolve_path('foo.png')
        expected = '/foo.png'
        self.assertEqual(result, expected)

        result = resolve_path('bar/foo.js')
        expected = '/bar/foo.js'
        self.assertEqual(result, expected)

    def test_01(self):
        """
        Basic path to file
        """

        result = resolve_path('/a')
        expected = '/a/index.html'
        # self.assertEqual(result, expected)
