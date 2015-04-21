'''
The main module for assignment 9. 

Created on Apr 14, 2015
@author: Adam Biesenbach
'''

from DataClass import RestaurantData
from TestRestaurantGrades import GradeAllNYC, GradeByBoro
from GenerateGraphs import GenerateGraphs
import sys 

if __name__ == "__main__":
    
    try:
        
        ''' The RestaurantData class itself generates a object containing the 
        restaurant data as a pandas dataframe. Here we call the CleanData method,
        which cleans the data (removes obs with missing values, etc.). '''
        
        CleanGrades = RestaurantData().CleanData()
    
        ''' Question four asks us to efficiently compute the sum of the function 
        over all restaurants in the data and for each of the five Boroughs, and to 
        Print out these values. Here is the code for this part of the assignment.'''
        
        # Produce the cumulative value for all NYC restaurants.
        GradeAllNYC(CleanGrades)
        
        # Produce the cumulative value by Borough.
        GradeByBoro(CleanGrades)
            
        # Graph the data. 
        GenerateGraphs(CleanGrades)
   
    except KeyboardInterrupt:
        print "\n whoops...KeyboardInterrupt... exiting program."
        sys.exit(0)   