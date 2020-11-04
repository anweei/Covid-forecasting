import pandas as pd


def extract_func(country_name, info_type, filepath=''):
    data = pd.read_parquet(filepath+'../data/df_lookup_table.parquet')
    return data.loc[data.index == country_name, info_type].values[0]
   
  

   
