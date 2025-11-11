print('\n') 

from pathlib import Path
import json 
from datetime import datetime


import plotly.express as px

# Read data as a string to convert to a Python object. 

path = Path('eq_data/eq_data_30_day_m1.geojson')
contents = path.read_text(encoding='utf-8')
all_eq_data = json.loads(contents)

# Create a mpre reable version of the data file 
path = Path('eq_data/readable_eq_data.geojson')
readable_contents = json.dumps(all_eq_data, indent=4)
path.write_text(readable_contents, encoding='utf-8') 

# Examine all earthquakes in the dataset. 
all_eq_dicts = all_eq_data['features'] #this grabs all the info in the file under the 'features' for each line 
print(len(all_eq_dicts))

# Extracting just the magnitudes of these earth quakes

# mags = [] 
# for eq_dict in all_eq_dicts:
#     mag = eq_dict['properties']['mag']
#     mags.append(mag)

# print(mags[:10])


# Extracting the magnitudes, longitudes and latitudes of these earth quakes

mags, lons, lats, eq_titles, times= [], [], [], [], []
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    eq_title = eq_dict['properties']['title']

    timestamp = eq_dict['properties']['time'] / 1000  # milliseconds → seconds
    readable_time = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')

    times.append(readable_time)
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)
    eq_titles.append(eq_title)


title = 'Global Earthquakes'
fig = px.scatter_geo(lat=lats, lon=lons, size=mags, title=title, color=mags, color_continuous_scale='Viridis', 
                     labels={'color':'Magnitude'}, projection='natural earth', hover_name=eq_titles,  hover_data={'Time': times})
fig.show()

print('\n')


#====================== AI summary 

# 🌍 Earthquake Data Visualization Summary

# Imports & Setup:
# Uses pathlib and json to load data, datetime for timestamp conversion, and plotly.express for visualization.

# Data Loading:
# Reads a GeoJSON file (eq_data_30_day_m1.geojson) containing earthquake data and converts it from JSON text into a Python dictionary.

# Data Extraction:
# Loops through each earthquake entry under the "features" key to collect:

# Magnitude (mag)

# Longitude (lon)

# Latitude (lat)

# Title (eq_title)

# Readable time (converted from milliseconds to UTC format)

# Visualization:
# Uses Plotly Express to plot the earthquakes on a world map (scatter_geo):

# Circle size and color represent earthquake magnitude.

# Hover info shows the title and time of each quake.

# The map uses a Natural Earth projection with a “Viridis” color scale.

# Purpose:
# To create an interactive global visualization of recent earthquakes, showing their location, magnitude, and time.