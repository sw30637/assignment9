'''
A Test module for assignment 9. 

Created on Apr 19, 2015
@author: Adam Bisenbach
'''
import unittest
import os

class Test(unittest.TestCase):

    def testFilesExist(self):
        
        for Area in ["bronx", "brooklyn", "nyc", "queens", "staten", "manhattan" ]:
            self.assertTrue(os.path.exists("./grade_improvement_"+ str(Area)+".pdf"),"The graph for " + str(Area) + " didn't save to output.")
        self.assertTrue(os.path.exists("./results.txt"), "Results file doesn't exist.")

if __name__ == "__main__":

    unittest.main()