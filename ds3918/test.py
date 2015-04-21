# Name: 	test.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	Contains unit-tests for assignment 9 
########################################################################################## 


import unittest
import os


class testsForAssignment9(unittest.TestCase):
    '''
    Defines 2 tests: if plots and the results.txt file exit in the working directory
    '''
    def test_plots(self):
        self.assertTrue(os.path.exists('grade_improvement_nyc.pdf'))
        self.assertTrue(os.path.exists('grade_improvement_bronx.pdf'))
        self.assertTrue(os.path.exists('grade_improvement_manhattan.pdf'))
        self.assertTrue(os.path.exists('grade_improvement_brooklyn.pdf'))
        self.assertTrue(os.path.exists('grade_improvement_staten.pdf'))
        self.assertTrue(os.path.exists('grade_improvement_queens.pdf'))
    
    def test_results_txt(self):
    	self.assertTrue(os.path.exists('results.txt'))
        

if __name__ == '__main__':
	unittest.main()




