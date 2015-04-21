'''
The main module for assignment 9. The data is read in using the CleanData 
method in the RestaurantData class. Coming up with the measure of 
restaurants' progress over time is done in the TestRestaurantGrades module. 
The Graphs are created using the GenerateGraphs function in the GenerateGraphs 
module. 

Created on Apr 14, 2015
@author: Adam Biesenbach
'''

from DataClass import RestaurantData
from TestRestaurantGrades import GradeByBoro
from GenerateGraphs import GenerateGraphs
import sys 

if __name__ == "__main__":
    
    try:
        
        ''' The RestaurantData class itself generates a object containing the 
        restaurant data as a pandas dataframe. Here we call the CleanData method,
        which pulls in and cleans the data (removes obs with missing values, etc.). '''
        
        CleanGrades = RestaurantData().CleanData()
    
        ''' Question four asks us to efficiently compute the sum of the function 
        over all restaurants in the data and for each of the five Boroughs, and to 
        Print out these values. Here is the code for this part of the assignment.'''

        # Produce the cumulative value by Borough and for NYC as a whole.
        GradeByBoro(CleanGrades)
            
        # Graph the data. 
        GenerateGraphs(CleanGrades)
   
    except KeyboardInterrupt:
        print "\n whoops...KeyboardInterrupt... exiting program."
        sys.exit(0)   