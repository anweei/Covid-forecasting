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
    
    color_list=['green','red','blue','orange']
    i=0

    for cluster in [cluster_1,cluster_2,cluster_3,cluster_4]:
        color = color_list[i]
        i+=1
        for country in cluster:
            lat = extract_func(country,'Latitude', filepath)
            lon = extract_func(country,'Longitude', filepath)
    
            popup = '<b>{}</b></br><i> </i>'.format(country)
            icon = folium.Icon(color=color,icon='circle')
        
            folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
    
    
    return m



