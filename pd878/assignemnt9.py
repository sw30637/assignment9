import pandas as pd
import sys
import matplotlib.pyplot as plt
from functions import *

reload(sys)
sys.setdefaultencoding("utf-8") 

df_raw = pd.read_csv('DOHMH_New_York_City_Restaurant_Inspection_Results.csv', dtype={'STREET' :'unicode'})

df_NaN_removed = df_raw.dropna(subset = ['GRADE']) # removes NAN grade rows

df = df_NaN_removed[df_NaN_removed['GRADE'].isin(['A', 'B', 'C'])] #removes invalid grade input
df = df[df.BORO != 'Missing'] #remove the records with missing borough info
df['GRADE DATE'] = pd.to_datetime(df['GRADE DATE'] ) # change the type of column 'GRADE DATE' to datatime

clean_df = df.drop_duplicates(['CAMIS','GRADE','GRADE DATE'])






if __name__ == "__main__":

	boros = list(clean_df['BORO'].unique())  
	for boro in boros:
	    df_boro = clean_df[clean_df.BORO == boro]
	    CAMIS_list=list(df_boro['CAMIS'].unique())
	    result = get_improvement(CAMIS_list)
	    print "The overall improvement score of the restaurants in %s is %s. " %(boro, result)
	    filename = 'grade_improvement_%s.pdf' %boro.lower()
	    draw_graph(df_boro, filename)

	filename = 'grade_improvement_nyc.pdf' 
	draw_graph(clean_df, filename)

