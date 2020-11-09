import pandas as pd
import folium
from folium.plugins import MarkerCluster
from extract_func import extract_func

#This function takes list over all countries as input and places these on a map using the folium package.
#Filepath can be given as argument to specify folder path from cluster_mapping to extract_func.

def country_mapping_func(list_over_countries, filepath=''):
    m = folium.Map(
        #coordinates of map center
        location=[40, 1],
        #level of zoom when map is first displayed
        zoom_start=1,
        #map type
        tiles='OpenStreetMap', 
    )

    for country in list_over_countries:
        #extract latitude and longitude for each country from lookup table, using ectract function 
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
        
        #add country name to marker   
        popup = '<b>{}</b></br><i> </i>'.format(country)
    
        #add marker to map
        folium.Marker([lat, lon], popup=popup).add_to(m)
    
    return m
