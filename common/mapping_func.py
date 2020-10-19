import pandas as pd
import folium
from folium.plugins import MarkerCluster
from extract_func import extract_func

def mapping_func(list_over_countries, filepath=''):
    m = folium.Map(
        location=[40.416775, -3.703790],
        #level of zoom when map is first displayed
        zoom_start=2,
        tiles='OpenStreetMap', 
        width='80%', 
    )

    m.add_child(folium.LatLngPopup())

    marker_cluster = MarkerCluster().add_to(m)

    for country in list_over_countries:
        lat = extract_func(country,'Latitude', filepath)
        lon = extract_func(country,'Longitude', filepath)
    
        popup = '<b>{}</b></br><i> </i>'.format(country)
    
        folium.Marker([lat, lon], popup=popup, tooltip=country).add_to(marker_cluster)
    
    return m