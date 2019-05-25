#!/usr/bin/bash/python3
"""Unittest for max_integer([...])
"""


import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger (unittest.TestCase):

    def test_max_integer(self):
        self.assertEqual(max_integer, (45, 54, 728), 728)
        self.assertEqual(max_integer,(), None)
        self.assertEqual(max_integer,("perro" ))
        with self.assertRaises(TypeError):
            max_integer(None)

if __name__ == '__main__':
    unittest.main()


