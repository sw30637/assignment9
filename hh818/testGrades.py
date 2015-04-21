'''
Created on Apr 20, 2015

@author: ds-ga-1007
'''

def test_grades(grade_list):
    '''takes a list of grades, compare and return 1 if grade improved, 0 the same, and -1 declined.
    if the last grade is better than the first grade, it is considered as improved, and etc.'''
    #in ascii table, 'A' is the smallest, than 'B', than 'C'
    if grade_list[0] < grade_list[-1]:
        return -1
    elif grade_list[0] == grade_list[-1]:
        return 0
    else:
        return 1
