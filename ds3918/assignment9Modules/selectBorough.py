# Name: 	selectBorough.py
# Author: 	Denis Stukal
# Date: 	April 18, 2015
# Summary:	Defines a function that selects a given borough from the data.
########################################################################################## 

import assignment9Modules.assignment9Exceptions as ex

def selectBorough(data, name = 'all'):
    '''
    Takes some data as input. By default return the whole dataset. Or returns only rows corresponding to a given borough. 
    Throws noSuchBoroughException if an invalid borough name is used.
    Throws loadedDataException if the data given is not about NYC
    '''
    try:
        if name == 'all':
            return data
        else:
            output = data[data['BORO'] == name]
            if output.shape[0] == 0:
                raise noSuchBoroughException()
            else:
                return output
    except AttributeError:
        raise ex.loadedDataException()