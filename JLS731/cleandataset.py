'''
Created by: Joseph Song (JLS731)
Created on: 4/19/2015
Assignment 9
Description: This is the class to clean the raw data and sort it by date.
Note that I allow for the data to be cleaned on two different columns: GRADE and SCORE
I allow this so that I can analyze the data by SCORE (the dates do not necessarily correspond
to each other).
'''

import pandas as pd
import numpy as np
from loaddata import loadcsvdata
from errorExceptions import *
from test_grades import *
from createHistogram import *

class cleandataset:
    '''This is the class to initialize and clean the data'''
    
    def __init__(self, dataset, datatype = 'GRADE'):
        '''Initialize the data'''
        self.dataset = dataset
        self.datatype = datatype

    def cleandata(self):
        '''This is the function to clean the date.'''
        self.datatype = self.datatype.upper()
        try:
            assert self.datatype in ['GRADE', 'SCORE']
        except:
            raise incorrectInputException()
        else:
            self.dataset = self.dataset[pd.notnull(self.dataset[self.datatype])]
            gradevalue = gradevaluetable()

            #Merge the grade/value table here
            self.dataset = self.dataset.merge(gradevalue, how='inner', left_on = 'GRADE', right_on = 'GRADE')

            #This is where I allow for the data to be 'cleaned' on either SCORE or GRADE
            if self.datatype == 'GRADE':
                self.dataset = self.dataset.drop_duplicates(['CAMIS', 'GRADE DATE', 'GRADE'])
                self.dataset = self.dataset.sort(['CAMIS', 'GRADE DATE'])
            elif self.datatype == 'SCORE':
                self.dataset = self.dataset.drop_duplicates(['CAMIS', 'INSPECTION DATE', 'SCORE'])
                self.dataset = self.dataset.sort(['CAMIS', 'INSPECTION DATE'])
            self.dataset = self.dataset.reset_index(drop = True)
            return self.dataset

        





