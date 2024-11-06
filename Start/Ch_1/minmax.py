# Example file for Advanced Python: Working With Data by Joe Marini
# Demonstrates the usage of the min and max functions
import json


# Declare an array with some sample data in it
values = [3.0, 2.5, 5.1, 4.1, 1.8, 1.6, 2.2, 5.7, 6.1]
strings = ["one", "three", "five", "seven", "eleven", "eighteen", "seventeen"]


# TODO: The min() function finds the minimum value


# TODO: The max() function finds the maximum value


# TODO: define a custom "key" function to extract a data field
# print(min(strings, key=len))
# print(max(strings, key=len))

# TODO: open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

def getitem(dataitem):
    magnitude = 0 if dataitem['properties']['mag'] == None else dataitem['properties']['mag']
    return float(magnitude)

print(min(data['features'], key=getitem).get('properties').get('mag'))
print(max(data['features'], key=getitem).get('properties').get('mag'))