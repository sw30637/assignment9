'''
Created on Mar 18, 2015
Created by Joseph Song (JLS731)
These exceptions capture specific errors rather than using catchall.
Note these are modified exception catchers from assignment 5.
'''


class incorrectInputException(Exception):
    """ Raises error message when one of the input's to the function is incorrect """
    def __str__(self):
        return 'Wrong datatype--Input GRADE or SCORE' 
