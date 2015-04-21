####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 9
#
#	This module contains general functions needed to clean up the dataset
#
####################################################################################################

# Import the modules needed
import pandas as pd
import numpy as np

# Define a function that will return the dataset separated for each borough
def SeparateBorough(boro, dataset):
	return dataset.loc[dataset['BORO']==boro]


# Define a function that will read through the dataset and return an array of camis_id
def SeparateCamis(dataset):
	return np.unique(dataset['CAMIS'])
