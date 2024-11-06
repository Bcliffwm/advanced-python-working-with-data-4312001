# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

from collections import defaultdict
import json

def get_type(data):
    return 'None' if data['properties']['type'] is None else data['properties']['type']

# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# getting totals in default dictionary
totals = defaultdict(int)

for event in data['features']:
    totals[get_type(event)] += 1

print(totals)