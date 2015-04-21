# -*- coding: utf-8 -*-
###################################
#  Tae Kim
#
#  plotter.py
#  April 19,2015
#
#  Saves plots - called from assignment9.py
# 
#
###################################


import matplotlib.pyplot as plt
import pandas as pd


class plotterClass():
    
  def __init__(self, thisDF): 
    '''
    DataFrame from assignment9
    ''' 
    self.thisDF = thisDF
    
    
  def plotBoroughs(self):
    '''
     this function will save a plot per borough
    '''
    for key, value in self.thisDF.items():
        thisBorough = pd.Series(value)
        plotThis = thisBorough.groupby(thisBorough.values).count()
        self.plotTer(key, plotThis)

  def plotNYC(self):
      '''
      save a plot for NYC
      '''
      nyc = pd.Series(self.thisDF.values())
      plotThis = nyc.groupby(nyc.values).count()
      self.plotTer("NYC", plotThis)
      
  def plotTer(self, key, plotThis):
    '''
    Plotting function
    '''  
    fig = plt.figure(figsize=(10,6), dpi=90)
    ax = plt.subplot(111)    
    plt.bar(plotThis.index,plotThis.values, 1)
    ax.set_ylabel('Frequency')
    ax.set_xlabel(key)
    plt.title("Restaurants Analysis based on ratings")
    plt.savefig('grade_improvement_%s.pdf' %(key)) 
      

