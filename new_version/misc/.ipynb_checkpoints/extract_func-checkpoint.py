import pandas as pd

#Function takes country name and info_type as input and returns corresponding information about country.
#Country name can be any country in the raw data.csv file while info_type can be one of the following:
#'Continent', 'Latitude', 'Longitude', 'Average temperature per year', 'Hospital beds per 1000 people', 'Medical doctors per 1000 people', 'GDP/Capita','Population', 'Median age', 'Population aged 65 and over (%)'

def extract_func(country_name, info_type, filepath=''):
    #load lookup_table parquet file 
    data = pd.read_parquet(filepath+'../data/df_lookup_table.parquet')
    #returns the value inn cell coresponding to index = country and column = info_type
    return data.loc[data.index == country_name, info_type].values[0]
   
  

   
