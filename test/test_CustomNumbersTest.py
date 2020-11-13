# -*- coding: utf-8 -*-

import unittest

from src.CustomNumbers import addNumbers


class TestSetup(unittest.TestCase):

    def setUp(self):
        self.a = 10
        self.b = 20

    def testAddNumbers(self):
        c = addNumbers(self.a, self.b)
        self.assertEqual(40, c)


if __name__ == '__main__':
    unittest.main()
