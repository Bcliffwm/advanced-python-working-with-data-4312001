# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json

# for this challenge, we're going to summarize the earthquake data as follows:

TotalEvents = 0
TotalFelt = 0
MostFeltEvent = ""
MostFeltCount = 0

def calc_summary():
    global TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount
    
    # open the data file and load the JSON
    with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)

    TotalEvents = len(data['features'])

    TotalFelt = sum(quake['properties']['felt'] is not None
                 and quake['properties']['felt'] >= 100
                 for quake in data['features'])
    
    MostFeltEvent = max(data['features'], key=getitem).get('properties').get('place')
    MostFeltCount = max(data['features'], key=getitem).get('properties').get('felt')

    return TotalEvents, TotalFelt, MostFeltEvent, MostFeltCount


with open("../../30DayQuakes.json", "r") as datafile:
        data = json.load(datafile)
    
# 1: How many quakes are there in total?
total_events = len(data['features'])
# print(total_events)

# 2: How many quakes were felt by at least 100 people?
total_felt = sum(quake['properties']['felt'] is not None
                 and quake['properties']['felt'] >= 100
                 for quake in data['features'])
# print(total_felt)

# 3: Print the name of the place whose quake was felt by the most people, with the # of reports

def getitem(dataitem):
    magnitude = 0 if dataitem['properties']['felt'] is None else dataitem['properties']['felt']
    return float(magnitude)

# print(max(data['features'], key=getitem).get('properties').get('place'),
#       max(data['features'], key=getitem).get('properties').get('felt'))

MostFeltEvent = max(data['features'], key=getitem).get('properties').get('place')
MostFeltCount = max(data['features'], key=getitem).get('properties').get('felt')

# 4: Print the top 10 most significant events, with the significance value of each
