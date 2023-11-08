from hamcrest import assert_that, is
from mutable_bytestring import MutableByteString
import unittest

class TestMutableByteString(unittest.TestCase):

    def test_replace_empty(self):
        str = MutableByteString("hello".encode('utf-8'))
        str.replace(bytearray(), bytearray(b'-'))
        self.assertEqual(str.toStringUtf8(), "-h-e-l-l-o-")

    def test_replace_multiple(self):
        str = MutableByteString("hello".encode('utf-8'))
        str.replace(bytearray(b'l'), bytearray(b'1,2,3'))
        self.assertEqual(str.toStringUtf8(), "he1,2,3o")

    def test_to_hex_string(self):
        str = MutableByteString("hello".encode('utf-8'))
        self.assertEqual(str.toHexString(), "68656c6c6f")

    def test_append(self):
        str = MutableByteString("hello".encode('utf-8'))
        str.append(ord(','))
        str.append(ord(' '))
        str.append(ord('w'))
        str.append(ord('o'))
        str.append(ord('r'))
        str.append(ord('l'))
        str.append(ord('d'))
        self.assertEqual(str.toStringUtf8(), "hello, world")

    def test_substring(self):
        str = MutableByteString("hello, world".encode('utf-8'))
        self.assertEqual(str.substring(0, 5).toStringUtf8(), "hello")
        self.assertEqual(str.substring(7, 12).toStringUtf8(), "world")

    def test_region_equals(self):
        str = MutableByteString("hello".encode('utf-8'))
        self.assertTrue(str.regionEquals(0, MutableByteString(bytearray(b'h')), 0, 1))
        self.assertFalse(str.regionEquals(0, MutableByteString(bytearray(b'h')), 0, 2))