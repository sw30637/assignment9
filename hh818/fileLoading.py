'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''
import pandas as pd
from dataCleanup import *
from testRestaurantGrades import *

def loadGrades():
    '''load file create a dataframe'''
    grades = pd.read_csv("DOHMH_New_York_City_Restaurant_Inspection_Results.csv", low_memory = False)
    
    return grades