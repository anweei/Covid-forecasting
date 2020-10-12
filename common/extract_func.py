import pandas as pd
import matplotlib.pyplot as plt
import datetime

def extract_func(country_name, info_type):
    data = pd.read_csv('df_lookup_table.csv')
    country = data[data['Country'] == country_name]
    value = str(country.info_type)
    return value[0]