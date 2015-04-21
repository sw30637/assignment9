'''
A Class that pulls in the restaurant grade data and cleans it up, if that method is desired. 

Created on Apr 14, 2015
@author: Adam Biesenbach
'''

import pandas as pd
from Exceptions import InvalidInputError

class RestaurantData(object):
    '''A class to pull together the restaurant data with a number of helpful methods.'''

    def __init__(self):
        
        # Import the restaurant grades data. 
        try:
            self.grades = pd.read_csv('grades.csv', sep=',', error_bad_lines=False, index_col=False, dtype='unicode')
        except:
            raise InvalidInputError("Problem in reading in the restaurant data.")
        
    def CleanData(self):
        """ Clean  the data by removing ratings observations for restaurants that
        aren't yet rated or have a z or p score. """
        
        # Just Select the variables we need
        self.grades = self.grades[['GRADE','CAMIS','INSPECTION DATE', 'BORO']]
        
        # Convert date to date time variable.
        self.grades = self.grades.loc[~self.grades['INSPECTION DATE'].isin(['01/01/1900'])]
        self.grades['INSPECTION DATE'] = pd.to_datetime(self.grades['INSPECTION DATE'])

        # Drop rows that have a missing values.
        self.grades = self.grades[pd.notnull(self.grades['GRADE'])]
        self.grades = self.grades[pd.notnull(self.grades['BORO'])]
        self.grades = self.grades[pd.notnull(self.grades['INSPECTION DATE'])]
             
        # Drop row where  the grade has not been given yet.
        self.grades = self.grades.loc[~self.grades['GRADE'].isin(['Not Yet Graded', 'P', 'Z'])]
                
        # Drop row where  the borough info is missing has not been given yet.
        self.grades = self.grades.loc[~self.grades['BORO'].isin(['Missing'])]
   
        # Drop duplicated (same restaurant and same date) inspection records.
        self.grades.drop_duplicates(['CAMIS','INSPECTION DATE','GRADE'], take_last=True, inplace=True)
        
        # Sort the data
        self.grades = self.grades.sort(['BORO','CAMIS','INSPECTION DATE'], ascending=[1,1,1])
        return self.grades
