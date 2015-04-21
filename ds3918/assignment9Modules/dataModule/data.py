# Name: 	data.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	Defines RestaurantData class with functions to load and clean the data, compute and sum restaurant grades
########################################################################################## 

import pandas as p
import assignment9Modules.assignment9Exceptions as ex
import assignment9Modules.gradesCheck as gc

class RestaurantData:
    '''
    Class to load and operate on restaurant data.
    1 default atribute -- fileName. 
    5 functions: 	loadRestaurantData()
					cleanRestaurantData()
					testRestaurantGrades()
					nycRestaurantGradesSum()
					boroughRestaurantGradesSum()
    '''

    def __init__(self, fileName = 'dataRestaurants.csv'):
        '''
        Instantiates a class object with 1 attribute - fileName
        '''
        self.fileName = fileName
        
    def loadRestaurantData(self, fileName = 'dataRestaurants.csv'):
        '''
        Reads a csv file with self.fileName. 
        Throws noSuchDataException when IOError is found. 
        '''
        try:
            self.data = p.read_csv(self.fileName, header=0, low_memory = False)
        except IOError:
            raise ex.noSuchDataException()
    
    def cleanRestaurantData(self):
        '''
        Cleans data previously loaded with loadRestaurantData(), selecting only rows with grades A, B, C.
        Throws loadedDataException if loadRestaurantData() was not used before. 
        '''
        try:
            self.data = self.data[(self.data['GRADE'] == 'A') | (self.data['GRADE'] == 'B') | (self.data['GRADE'] == 'C')]
            # Change index after removing superfluous rows
            self.data.index = range(self.data.shape[0])
        except AttributeError:
            raise ex.loadedDataException()
        
    def testRestaurantGrades(self, camisId):
        '''
        Selects rows that correspond to a given restaurant in the data previously loaded with loadRestaurantData()
        and computes that restaurant's performance value with testGrades() from assignment9Modules.gradesCheck module.
        Throws: 	loadedDataException if loadRestaurantData() was not used before
                    noSuchRestaurantException() if no rows correspond to that restaurant
        '''
        try:
            # Select rows corresponding to a given restaurant ID
            currentData = self.data[self.data['CAMIS'] == camisId].sort(columns='GRADE DATE', ascending=False)
            # If no rows are selected, throw noSuchRestaurantException
            if currentData.shape[0] == 0:
                raise ex.noSuchRestaurantException()
            # Otherwise, apply testGrades()
            return gc.testGrades(currentData['GRADE'])
        except AttributeError:
            raise ex.loadedDataException()
            
    def nycRestaurantGradesSum(self,):
        '''
        Sums testRestaurantGrades() values across all restaurants in NYC.
        Throws loadedDataException() if loadRestaurantData() was not used before. 
        '''
        try:
            total = 0
            for restaurantID in self.data['CAMIS'].unique():
                total += self.testRestaurantGrades(restaurantID)
            return total
        except AttributeError:
            raise ex.loadedDataException()

            
    def boroughRestaurantGradesSum(self, boroughName):
        '''
        Sums testRestaurantGrades() values across all restaurants in a given borough of NYC.
        Throws loadedDataException() if loadRestaurantData() was not used before.
        '''
        try:
            total = 0
            for id in self.data[self.data['BORO'] == boroughName]['CAMIS'].unique():
                total += self.testRestaurantGrades(id)
            return total
        except AttributeError:
            raise ex.loadedDataException()
     







