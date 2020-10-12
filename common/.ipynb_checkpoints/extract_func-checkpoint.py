import pandas as pd
import matplotlib.pyplot as plt
import datetime

data = pd.read_csv('df_lookup_table.csv')

def extract_func(country_name, info_type):
    
    return data.loc[data.Country == country_name, info_type].values[0]
   
  

   
