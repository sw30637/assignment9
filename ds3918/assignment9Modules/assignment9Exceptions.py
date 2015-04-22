# Name: 	assignment9Exceptions.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	Defines specific exceptions for assignment 9
########################################################################################## 


class noSuchRestaurantException(Exception):
    '''
    Exception used in testRestaurantGrades() in Graphs class 
    when a restaurant with a non-existing CAMIS id is selected.
    '''
    def __str__(self):
        print ' There is no restaurant with the given id'


class noSuchBoroughException(Exception):
    '''
    Exception used in selectBorough() when a non-existing borough is selected from the data
    and in plotGradeCountOverTime() in Graphs class. 
    '''
    def __str__(self):
        return ' There is no such a borough in NYC'


class noSuchDataException(Exception):
    '''
    Exception used in loadRestaurantData() in the RestaurantData class when IOError is raised in reading the file
    '''
    def __str__(self):
        return ' You are trying to load data from a file that does not exist'


class loadedDataException(Exception):
    '''
    Exception often used in the RestaurantData class when the wrong data are read in 
    '''
    def __str__(self):
        return ' You might have forgotten to load data, or loaded the wrong data set'


class graphInstantiationException(Exception):
    '''
    Exception used in Graphs class when an error occurs while instantiating the class. 
    '''
    def __str__(self):
        return " You failed to instantiate a Graph object"


class urgentProgramExit(Exception):
    '''
    Exception used in Graphs class to denote user's attempt to exit the program. 
    '''
    def __str__(self):
        return " You asked to exit the program"
