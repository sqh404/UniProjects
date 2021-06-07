#!/usr/bin/python

import googlemaps
import sys
import csv

gmaps = googlemaps.Client(key='AIzaSyBmjaKszLBO5UPKvsVlyUgzC9Uwv2gUuR8')

# results = gmaps.geocode("Los Angeles")
#
# print(results[0].keys())
# print(results[0]["geometry"]["location"])


infile = open('missing.txt', 'r', encoding='utf-8')
tosearch = []
locations = []

for line in infile:
    l = line.strip()
    s = l.find('(')
    if s > 0:
        l = l[:s]
    tosearch.append(l)
infile.close()
print(tosearch)

header = ["name", "lat", "long"]
locations.append(header)

count = 1
for location in tosearch:
    results = gmaps.geocode(location)
    if len(results) > 0:
        lat = results[0]["geometry"]["location"]["lat"]
        long = results[0]["geometry"]["location"]["lng"]
        locations.append([location, lat, long])
        print(locations[count])
        count += 1

with open("geomissing_out.csv", 'w', newline='', encoding='utf-8') as csvout:
    csvw = csv.writer(csvout)
    csvw.writerows(locations)
