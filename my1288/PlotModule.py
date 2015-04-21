####################################################################################################
#
#
#	Author : Maha Yaqub (my1288)
#	DS GA 1007
#	Assignment 9
#
#	This module contains the class which will be used to plot the graphs
#
####################################################################################################

# Import the modules needed
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# This class will take in the performance results for each borough and then plot the results needed 
class PlotGraphs:

	# The constructor function which defines the class variable
	def __init__(self, performance, boro):
		self.performance = performance
		self.borough 	    = boro


	# Function defined to save the plots
	def Plot_Graphs(self):

		# Declare variables for the xticks
		x = [-1, 0, 1]
		x_values = ['Declining Performance', 'No Change', 'Improving Performance']

		# Give proper commands to plot the boxplot
		plt.hist(self.performance, range=[-1.5,1.5], align='mid')
		plt.title('Performance Indicator Distribution for Restaurants in '+ self.borough)
		plt.xlabel('Performance Indicator')
		plt.ylabel('Frequency')
		plt.xticks(x, x_values)

		# This command saves the graph in a pdf file
		figName = 'grade_improvement_'+self.borough+'.pdf'
		plt.savefig(figName)
		plt.clf()

