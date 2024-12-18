import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap
import time
import random

#Initialize geocoder (timeout of 10 seconds to prevent high limit overload)
geolocator = Nominatim(user_agent="road_geocoder", timeout=10)

#Load the CSV file (final cleaned data version)
file_path = 'C:\\Users\\ysj04\\Downloads\\updated6.csv'
df = pd.read_csv(file_path)

#Store the coordinates using starting and ending of each road
coordinates = []

#Geocode the address and get latitude and longitude coordinates
def geocode_address(address):
    try:
        location = geolocator.geocode(address)
        if location:
            return location.latitude, location.longitude
        else:
            print(f"Address not found: {address}")
            return None, None
    except Exception as e:
        print(f"Error geocoding {address}: {e}")
        return None, None

#Random delay to prevent rate limits
def random_sleep():
    time.sleep(random.uniform(1, 2))  #Add some random delay between 1 and 2 seconds

#Loop through dataframe to get coordinates
start_time = time.time()  # Start tracking time
total_rows = len(df)

for index, row in df.iterrows():
    start_address = row['5']
    end_address = row['6']
    
    #Geocode starting point
    start_lat, start_lon = geocode_address(start_address)
    #Geocode ending point
    end_lat, end_lon = geocode_address(end_address)
    
    if start_lat and start_lon and end_lat and end_lon:
        coordinates.append([start_lat, start_lon])  # Add start point
        coordinates.append([end_lat, end_lon])  # Add end point
    
    #Print progress every 100 roads to verify that it is working
    if (index + 1) % 100 == 0 or (index + 1) == total_rows:
        elapsed_time = time.time() - start_time
        print(f"Processed {index + 1} of {total_rows} roads. Elapsed time: {elapsed_time:.2f} seconds.")

    random_sleep()

#Create a Folium map centered around the average of the coordinates
map_center = [sum([coord[0] for coord in coordinates])/len(coordinates),
              sum([coord[1] for coord in coordinates])/len(coordinates)]
road_heatmap = folium.Map(location=map_center, zoom_start=12)

#Incorporate heatmap to the map
HeatMap(coordinates).add_to(road_heatmap)

#Save heatmap as HTML file
road_heatmap.save('heatmap_final.html')
