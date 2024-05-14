#!/usr/bin/env python3

import unittest
from algorithms.check_valid_username_length import validate_user

class TestCheckValidUsernameLength(unittest.TestCase):
    def test_length(self):
        testcase1 = 'Valid'
        expected1 = True
        testcase2 = 'not'
        expected2 = False
        self.assertTrue(validate_user(testcase1, 5), expected1)
        self.assertFalse(validate_user(testcase2, 5), expected2)



unittest.main()