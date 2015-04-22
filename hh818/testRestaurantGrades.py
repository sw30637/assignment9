'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''
from testGrades import *

def test_restaurant_grades(group):
    '''take the list of grades of a restuarant and check if grades are improving, declining, or stayed the same'''
    
    grades = group['GRADE'].tolist()
    results = test_grades(grades)
    
    return results

