'''
Created by: Joseph Song (JLS731)
Created on: 4/21/2015
Assignment 9
Description: This is the unit test to test the package to make sure the
programs are working properly. 
'''

#Load the functions and classes
import unittest
import os.path

class Test(unittest.TestCase):

    def testfileexist(self):
        '''Test to make sure that the input and output files exist'''
        self.assertTrue(os.path.exists("./DOHMH_New_York_City_Restaurant_Inspection_Results.csv"), "The output does not exists")
        self.assertTrue(os.path.exists("./NYC_Grade.csv"), "The output does not exists")
        self.assertTrue(os.path.exists("./ByBorough_Grade.csv"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_Manhattan.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_QUEENS.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_BROOKLYN.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_BRONX.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_STATEN ISLAND.pdf"), "The output does not exists")
        self.assertTrue(os.path.exists("./grade_improvement_NYC.pdf"), "The output does not exists")

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()
