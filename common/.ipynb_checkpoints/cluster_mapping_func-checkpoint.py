import pandas as pd
import folium
from folium.plugins import MarkerCluster
from extract_func import extract_func

def cluster_mapping_func(cluster_1,cluster_2,cluster_3,cluster_4, filepath=''):
    m = folium.Map(
        location=[40.416775, -3.703790],
        #level of zoom when map is first displayed
        zoom_start=2,
        tiles='OpenStreetMap', 
        #width='80%', 
    )

    m.add_child(folium.LatLngPopup())

    for country in cluster_1:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
        icon = folium.Icon(color='green',icon='circle')
    
        folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
        
    for country in cluster_2:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
        icon = folium.Icon(color='red',icon='circle')
    
        folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
        
    for country in cluster_3:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
        icon = folium.Icon(color='blue',icon='circle')
    
        folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
        
    for country in cluster_4:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
        icon = folium.Icon(color='orange',icon='circle')
    
        folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
    
    return m



