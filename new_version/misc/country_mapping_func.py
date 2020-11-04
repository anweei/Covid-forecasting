import pandas as pd
import folium
from folium.plugins import MarkerCluster
from extract_func import extract_func

def country_mapping_func(list_over_countries, filepath=''):
    m = folium.Map(
        location=[40.416775, -3.703790],
        #level of zoom when map is first displayed
        zoom_start=2,
        tiles='OpenStreetMap', 
        #width='80%', 
    )

    m.add_child(folium.LatLngPopup())

    for country in list_over_countries:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
    
        folium.Marker([lat, lon], popup=popup).add_to(m)
    
    return m
