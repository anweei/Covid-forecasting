import pandas as pd
import folium
from folium.plugins import MarkerCluster
from extract_func import extract_func

#This function takes four list of countries (Intention is one list per cluster) as input and places these on a map using the folium package.
#The input clusters are assigned the colors green, red, blue and orange respecitivly based on order clusters are 
#given as argument to function.
#Filepath can be given as argument to specify folder path from cluster_mapping to extract_func.

def cluster_mapping_func(cluster_1,cluster_2,cluster_3,cluster_4, filepath=''):
    m = folium.Map(
        #coordinates of map center
        location=[40, 1],
        #level of zoom when map is first displayed
        zoom_start=1,
        #map type
        tiles='OpenStreetMap',  
    )
    
    color_list=['green','red','blue','orange']
    counter=0

    for cluster in [cluster_1,cluster_2,cluster_3,cluster_4]:
        #select color
        color = color_list[counter]
        counter+=1
        for country in cluster:
            #extract latitude and longitude for each country from lookup table, using ectract function 
            lat = extract_func(country,'Latitude', filepath)
            lon = extract_func(country,'Longitude', filepath)

            #add country name to marker  
            popup = '<b>{}</b></br><i> </i>'.format(country)
            #create icon in correct color and with circle icon 
            icon = folium.Icon(color=color,icon='circle')
            
            #add marker to map
            folium.Marker([lat, lon], popup=popup,icon=icon).add_to(m)
    
    
    return m



