''' Unittest '''
import unittest
from a13_mymodule import square, double, add

class TestSquare(unittest.TestCase):
    ''' Class for test square function '''
    def test1(self):
        ''' Test square function '''
        self.assertEqual(square(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(square(3.0), 9.0)  # test when 3.0 is given as input the output is 9.0.
        self.assertNotEqual(square(-3), -9)  # test when -3 is given as input the output is not -9.


class TestDouble(unittest.TestCase):
    ''' Class for test double function '''
    def test1(self):
        ''' Test double function '''
        self.assertEqual(double(2), 4) # test when 2 is given as input the output is 4.
        self.assertEqual(double(-3.1), -6.2) # test when -3.1 is given as input the output is -6.2.
        self.assertEqual(double(0), 0) # test when 0 is given as input the output is 0.


class TestAdd(unittest.TestCase):
    ''' Class for test add function '''
    def test1(self):
        ''' Test add function '''
        self.assertEqual(add(2,3), 5)
        self.assertNotEqual(add(-3.1,8), 5)
        self.assertEqual(add(0,8), 8)
        self.assertEqual(add("Hi"," world!"), "Hi world!")

unittest.main()
