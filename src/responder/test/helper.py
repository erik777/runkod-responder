import unittest

from runkod.helper import resolve_path
from unittest.mock import patch
from unittest.mock import Mock


class HelperTestCase(unittest.TestCase):

    def test_00(self):
        """
        Basic path to file
        """
        result = resolve_path({'_id': '1'}, '')
        expected = '/index.html'
        self.assertEqual(result, expected)

        result = resolve_path({'_id': '1'}, '/')
        expected = '/index.html'
        self.assertEqual(result, expected)

        result = resolve_path({'_id': '1'}, 'foo.png')
        expected = '/foo.png'
        self.assertEqual(result, expected)

        result = resolve_path({'_id': '1'}, 'bar/foo.js')
        expected = '/bar/foo.js'
        self.assertEqual(result, expected)

        result = resolve_path({'_id': '1'}, 'main.js')
        expected = '/main.js'
        self.assertEqual(result, expected)

    @patch('runkod.helper.get_file', return_value=Mock())
    def test_01(self, mocked):
        mocked.side_effect = [
            None,
            None,
            None,
            None,
            None
        ]

        result = resolve_path({'_id': '1'}, '/foo/bar/baz/maz/')
        expected = '/foo/bar/baz/maz/'
        self.assertEqual(result, expected)

    @patch('runkod.helper.get_file', return_value=Mock())
    def test_02(self, mocked):
        mocked.side_effect = [
            {'id': 'xx'}
        ]

        result = resolve_path({'_id': '1'}, '/foo/bar/baz/maz/')
        expected = '/foo/bar/baz/maz/index.html'
        self.assertEqual(result, expected)

    @patch('runkod.helper.get_file', return_value=Mock())
    def test_03(self, mocked):
        mocked.side_effect = [
            None,
            None,
            None,
            {'id': 'xx'},
            None,

        ]

        result = resolve_path({'_id': '1'}, '/foo/bar/baz/maz/')
        expected = '/foo/index.html'
        self.assertEqual(result, expected)

    @patch('runkod.helper.get_file', return_value=Mock())
    def test_03(self, mocked):
        mocked.side_effect = [
            None,
            None,
            None,
            None,
            {'id': 'xx'}

        ]

        result = resolve_path({'_id': '1'}, '/foo/bar/baz/maz/')
        expected = '/index.html'
        self.assertEqual(result, expected)

    @patch('runkod.helper.get_file', return_value=Mock())
    def test_03(self, mocked):
        mocked.side_effect = [
            None,
            None,
            None,
            None,
            None,
            None
        ]

        result = resolve_path({'_id': '1'}, '/foo/bar/baz/maz/lorem/ipsum/dolor/sit')
        expected = '/foo/bar/baz/maz/lorem/ipsum/dolor/sit'
        self.assertEqual(result, expected)
