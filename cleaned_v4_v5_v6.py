import pandas as pd
from geopy.geocoders import Nominatim
import folium
from folium.plugins import HeatMap
import time
import random

#Initialize geocoder (timeout of 10 seconds to prevent high limit overload)
geolocator = Nominatim(user_agent="road_geocoder", timeout=10)

#Load CSV file
file_path = 'C:\\Users\\ysj04\\Downloads\\updated3.csv' #Replace with your own file path 
df = pd.read_csv(file_path)

#Store the coordinates using starting and ending of each road
start_latitudes = []
start_longitudes = []
end_latitudes = []
end_longitudes = []

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
start_time = time.time()  #Start tracking time
total_rows = len(df)

for index, row in df.iterrows():
    start_address = row['5']
    end_address = row['6']
    
    #Geocode starting point
    start_lat, start_lon = geocode_address(start_address)
    #Geocode ending point
    end_lat, end_lon = geocode_address(end_address)

    #Add coordinates to be stored (Unless address not found then use nan as substitute)
    start_latitudes.append(start_lat if start_lat is not None else np.nan)
    start_longitudes.append(start_lon if start_lon is not None else np.nan)
    end_latitudes.append(end_lat if end_lat is not None else np.nan)
    end_longitudes.append(end_lon if end_lon is not None else np.nan)
    
    #Print progress every 100 roads to verify that it is working
    if (index + 1) % 100 == 0 or (index + 1) == total_rows:
        elapsed_time = time.time() - start_time
        print(f"Processed {index + 1} of {total_rows} roads. Elapsed time: {elapsed_time:.2f} seconds.")
    
    random_sleep()

file_path = 'C:\\Users\\ysj04\\Downloads\\updated3.csv' #Replace with your own file path 
df = pd.read_csv(file_path)

df['start_latitude'] = start_latitudes
df['start_longitude'] = start_longitudes
df['end_latitude'] = end_latitudes
df['end_longitude'] = end_longitudes

cleaned_data_4 = 'C:\\Users\\ysj04\\Downloads\\updated4.csv' #Replace with your own file path
df.to_csv(cleaned_data_4, index=False)
print(df)

file_path = 'C:\\Users\\ysj04\\Downloads\\updated4.csv' #Replace with your own file path
df = pd.read_csv(file_path)

df.columns = range(df.shape[1]) #Reset column index

#Renaming
df.iloc[0, 10] = 'start_lat'
df.iloc[0, 11] = 'start_lon'  
df.iloc[0, 12] = 'end_lat'     
df.iloc[0, 13] = 'end_lon'  

cleaned_data_5 = 'C:\\Users\\ysj04\\Downloads\\updated5.csv' #Replace with your own file path
df.to_csv(cleaned_data_5, index=False
print(df)

file_path = 'C:\\Users\\ysj04\\Downloads\\updated5.csv' #Replace with your own file path
df = pd.read_csv(file_path)

#Delete any rows with any missing values
df.dropna(inplace=True)

cleaned_data_6 = 'C:\\Users\\ysj04\\Downloads\\updated6.csv' #Replace with your own file path
df.to_csv(cleaned_data_6, index=False)
print(df)
