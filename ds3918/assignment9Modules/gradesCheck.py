# Name: 	gradesCheck.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	Computes performance values for a restaurant from an ordered list of grades
########################################################################################## 

import pandas as p


def testGrades(gradeList):
    '''
    Takes as argument an ordered list of grades. Returns a value showing whether a restaurant is improving, staying the same, or worsening.
    If the sum of positive changes is higher than the sum of zero or negative changes, returns 1. 
    If the sum of negative changes is higher than the sum of zero or positive changes, returns -1. 
    Otherwise, returns 0. 
    A change is positive (1) if the grade goes from C to B, or from B to A. 
    A change is positive (2) if the grade goes from C to A.
    To types of negative changes are defined in a similar way.
    A zero change happens if the grade remains the same between two grading episodes. 
    '''
    sumOfChanges = 0
    for i in range(len(gradeList)-1):
        sumOfChanges += (ord(gradeList.iloc[i,]) - ord(gradeList.iloc[(i+1),]))
    if sumOfChanges < 0:
        return -1
    elif sumOfChanges == 0:
        return 0
    else:
        return 1


