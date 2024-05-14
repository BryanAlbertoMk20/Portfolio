#!/usr/bin/env python3

from algorithms.rearrange import rearrange_name
import unittest


class TestRearrange(unittest.TestCase):
# Check to see that function works properly.
    def test_basic(self):
        testcase1 = "Lovelace, Ada"
        expected1 = "Ada Lovelace"

        testcase2 = "Thomas, Mark"
        expected2 = "Mark Thomas"

        testcase3 = "Ade, Gator"
        expected3 = "Gator Ade"

        self.assertEqual(rearrange_name(testcase1), expected1)
        self.assertEqual(rearrange_name(testcase2), expected2)
        self.assertEqual(rearrange_name(testcase3), expected3)

# Check to see what happens when input string is empty.
    def test_check_empty(self):
        testcase1 = ""
        expected1 = ""
        self.assertEqual(rearrange_name(testcase1), expected1)

# Check if someone with two names can
    def test_double_name(self):
        testcase = "Hopper, Grace M."
        expected = "Grace M. Hopper"
        self.assertEqual(rearrange_name(testcase), expected)

# Check if there is only one name
    def test_one_name(self):
        testcase = "Maxy"
        expected = "Maxy"
        self.assertEqual(rearrange_name(testcase), expected)

# Check if input is an int
    def test_int(self):
        testcase = 1
        expected = "Not a valid name."
        self.assertEqual(rearrange_name(testcase), expected)

unittest.main()



