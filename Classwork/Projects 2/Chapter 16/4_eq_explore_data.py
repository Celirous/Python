print('\n') 

from pathlib import Path
import json 

# Read data as a string to convert to a Python object. 

path = Path('eq_data/eq_data_1_day_m1.geojson')
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

mags, lons, lats = [], [], [] 
for eq_dict in all_eq_dicts:
    mag = eq_dict['properties']['mag']
    lon = eq_dict['geometry']['coordinates'][0]
    lat = eq_dict['geometry']['coordinates'][1]
    mags.append(mag)
    lons.append(lon)
    lats.append(lat)


print(mags[:10])
print(lons[:10])
print(lats[:10])

print('\n')