import pandas as pd


def extract_func(country_name, info_type, filepath=''):
    data = pd.read_csv(filepath+'df_lookup_table.csv')
    return data.loc[data.Country == country_name, info_type].values[0]
   
  

   
