# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  unittest9.py 
#  April 19,2015
#
#  1. Test correctly to calculating the changes of the ratings. 
# 
#  
###################################

import unittest
import assignment9 as a9

class Assignment9Test(unittest.TestCase):

    def setUp(self):
        print "setUp"
    
    
    def testTest_grades(self):
        '''
        Testing test_grades
        '''
        self.assertEqual(a9.test_grades(['A','B']), -1)  
        self.assertEqual(a9.test_grades(['B','B']),  0)  
        self.assertEqual(a9.test_grades(['B','A']),  1)  
        self.assertEqual(a9.test_grades(['A','B','C']), -2)  
        self.assertEqual(a9.test_grades(['C','B','A']),  2)  
 
    
        
if __name__ == '__main__':
   unittest.main()
   
   