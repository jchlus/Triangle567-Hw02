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
    # define multiple sets of tests as functions with names that begin
    
    # tests in main code already detect if it is a triangle or not
    
    def testValidInputA(self): 
        self.assertEqual(classifyTriangle(300,300,300),'InvalidInput','300,300,300 should be InvalidInput')
        
    def testValidInputC(self): 
        self.assertEqual(classifyTriangle(-300,300,300),'InvalidInput','-300,300,300 should be InvalidInput') 
        
    def testValidInputD(self): 
        self.assertEqual(classifyTriangle(300,-300,300),'InvalidInput','300,-300,300 should be InvalidInput')    
        
    def testValidInputE(self): 
        self.assertEqual(classifyTriangle(300,300,-300),'InvalidInput','300,300,-300 should be InvalidInput')
        
    def testValidInputG(self): 
        self.assertEqual(classifyTriangle(-30,30,30),'InvalidInput','-30,30,30 should be InvalidInput') 
        
    def testValidInputH(self): 
        self.assertEqual(classifyTriangle(30,-30,30),'InvalidInput','30,-30,30 should be InvalidInput')    
        
    def testValidInputI(self): 
        self.assertEqual(classifyTriangle(30,30,-30),'InvalidInput','30,30,-30 should be InvalidInput')    
        
    def testValidInputJ(self): 
        self.assertEqual(classifyTriangle(-30,-20,-15),'InvalidInput','-30,-20,-15 should be InvalidInput')
      
        
        
    def testRightTriangleA(self): 
        self.assertEqual(classifyTriangle(3,4,5),'Right','3,4,5 is a Right triangle')

    def testRightTriangleB(self): 
        self.assertEqual(classifyTriangle(5,3,4),'Right','5,3,4 is a Right triangle')
        
    def testRightTriangleC(self): 
        self.assertEqual(classifyTriangle(10,6,8),'Right','10,6,8 is a Right triangle')
        
                
        
    def testEquilateralTrianglesA(self): 
        self.assertEqual(classifyTriangle(1,1,1),'Equilateral','1,1,1 should be equilateral')
        
    def testEquilateralTrianglesB(self): 
        self.assertEqual(classifyTriangle(5,5,5),'Equilateral','5,5,5 should be equilateral')
        
                
        
    def testIsociliesTriangleA(self):
        self.assertEqual(classifyTriangle(3,6,6), 'Isoceles','3,6,6 should be isoceles')
        
    def testIsociliesTriangleB(self):
        self.assertEqual(classifyTriangle(6,6,3), 'Isoceles','6,6,3 should be isoceles')  
        
    def testIsociliesTriangleC(self):
        self.assertEqual(classifyTriangle(6,3,6), 'Isoceles','6,6,3 should be isoceles')
        
        
        
    def testScaleneTriangleA(self):
        self.assertEqual(classifyTriangle(10,15,20), 'Scalene','10,15,20 should be scalene')
        
    def testScaleneTriangleB(self):
        self.assertEqual(classifyTriangle(20,15,10), 'Scalene','20,15,10 should be scalene')
        
        
        
    def testNotATriangleA(self):
        self.assertEqual(classifyTriangle(10,15,40), 'NotATriangle','10,15,40 should not be a triangle')
            
    def testNotATriangleB(self):
        self.assertEqual(classifyTriangle(40,10,10), 'NotATriangle','40,10,10 should not be a triangle')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()

