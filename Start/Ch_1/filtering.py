# Example file for Advanced Python: Working With Data by Joe Marini
# using the filter() function to filter a data set

import json


def filterEvens(x):
    # filters out even numbers and keeps odd numbers
    if x % 2 == 0:
        return False
    return True


def filterUppers(x):
    # filters out upper-case letters and keeps lower case letters
    if x.isupper():
        return False
    return True

def is_earthquake(dataitem):
    return dataitem['properties']['type'] == 'earthquake'

def not_earthquake(dataitem):
    return not dataitem['properties']['type'] == 'earthquake'

# define some sample sequences to operate on
nums = (1, 8, 4, 5, 13, 26, 381, 410, 58, 47)
chars = "abcDeFGHiJklmnoP"

# TODO: use filter to remove items from a list
odds = list(filter(filterEvens, nums))
lowers = list(filter(filterUppers, chars))

print(odds)
print(lowers)

# TODO: use filter on non-numeric sequence

# Use the filter on our data - let's filter out all seismic events that were *not* quakes
# open the data file and load the JSON
with open("../../30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

earthquakes = list(filter(is_earthquake, data['features']))
not_earthquakes = list(filter(not_earthquake, data['features']))
for i in range(5):
    print(not_earthquakes[i].get('properties').get('type'))