# -*- coding: utf-8 -*-
"""
Updated Jan 21, 2018
The primary goal of this file is to demonstrate a simple unittest implementation

@author: jrr
@author: rk
"""

import unittest

from Triangle import classifyTriangle

# This code implements the unit test functionality
# https://docs.python.org/3/library/unittest.html has a nice description of the framework

class TestTriangles(unittest.TestCase):

    def testRightTriangleA(self):
        self.assertEqual(classifyTriangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')

    def testRightTriangleB(self):
        self.assertEqual(classifyTriangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')

    def testRightTriangleC(self):
        self.assertEqual(classifyTriangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def testEquilateralTriangleA(self):
        self.assertEqual(classifyTriangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')

    def testEquilateralTriangleB(self):
        self.assertEqual(classifyTriangle(2, 2, 2), 'Equilateral', '2,2,2 should be equilateral')

    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(2, 3, 4), 'Scalene', '2,3,4 is a Scalene triangle')

    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(12, 15, 23), 'Scalene', '12,15,23 is a Scalene triangle')

    def testIsocelesTriangleA(self):
        self.assertEqual(classifyTriangle(2, 2, 3), 'Isoceles', '2,2,3 is an Isoceles triangle')

    def testIsocelesTriangleB(self):
        self.assertEqual(classifyTriangle(67, 67, 100), 'Isoceles', '67,67,100 is an Isoceles triangle')

    def testValidA(self):
        self.assertEqual(classifyTriangle(201, 1, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidB(self):
        self.assertEqual(classifyTriangle(1, 201, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidC(self):
        self.assertEqual(classifyTriangle(1, 2, 201), 'InvalidInput', 'This triangle is not valid')

    def testValidD(self):
        self.assertEqual(classifyTriangle(0, 1, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidE(self):
        self.assertEqual(classifyTriangle(1, 0, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidF(self):
        self.assertEqual(classifyTriangle(1, 2, 0), 'InvalidInput', 'This triangle is not valid')

    def testValidG(self):
        self.assertEqual(classifyTriangle(1.5, 1, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidH(self):
        self.assertEqual(classifyTriangle(1, 1.5, 2), 'InvalidInput', 'This triangle is not valid')

    def testValidI(self):
        self.assertEqual(classifyTriangle(1, 2, 1.5), 'InvalidInput', 'This triangle is not valid')

    def testValidJ(self):
        self.assertEqual(classifyTriangle(3, 1, 2), 'NotATriangle', 'This is not a triangle')

    def testValidK(self):
        self.assertEqual(classifyTriangle(1, 3, 2), 'NotATriangle', 'This is not a triangle')

    def testValidL(self):
        self.assertEqual(classifyTriangle(1, 2, 3), 'NotATriangle', 'This is not a triangle')

    if __name__ == '__main__':
        print('Running unit tests')
        unittest.main()
