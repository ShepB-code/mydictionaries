# Author:     Shepard Berry
# Class:      MIS-4322
# Due:        2/8/2023
# Assignment: Dictionaries

'''
the eq_data file is a json file that contains detailed information about
earthquakes around the world for a period of a month.

NOTE: No hard-coding allowed except for keys for the dictionaries

1) print out the number of earthquakes

2) iterate through the dictionary and extract the location, magnitude, 
   longitude and latitude of the location and put it in a new
   dictionary, name it 'eq_dict'. We are only interested in earthquakes that have a 
   magnitude > 6. Print out the new dictionary.

3) using the eq_dict dictionary, print out the information as shown below (first three shown):

Location: Northern Mid-Atlantic Ridge
Magnitude: 6.2
Longitude: -36.0923
Latitude: 35.4364


Location: 166km SSE of Muara Siberut, Indonesia
Magnitude: 6.1
Longitude: 100.0208
Latitude: -2.8604


Location: 14km ENE of Puerto Madero, Mexico
Magnitude: 6.6
Longitude: -92.2981
Latitude: 14.7628

'''

import json

def main():
    with open("eq_data.json", 'r') as f:
        data = json.load(f)

        # get number of earthquakes
        earthquakes = [feature for feature in data['features'] if feature['properties']['type'] == 'earthquake']

        print(f'Number of Earthquakes: {len(earthquakes)}\n\n')

        eq_dict = {'features' : []}

        for eq in earthquakes:
            if eq['properties']['mag'] > 6:
                eq_dict['features'].append({
                    'location' : eq['properties']['place'],
                    'magnitude' : eq['properties']['mag'],
                    'longitude' : eq['geometry']['coordinates'][0],
                    'latitude' : eq['geometry']['coordinates'][1]
                })

        print(f'eq_dict: {eq_dict}\n\n')

        for eq in eq_dict['features']:
            print(f'Location: {eq["location"]}\n'
                  f'Magnitude: {eq["magnitude"]}\n'
                  f'Longitude: {eq["longitude"]}\n'
                  f'Latitude: {eq["latitude"]}\n')



if __name__ == "__main__":
    main()