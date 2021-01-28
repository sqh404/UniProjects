#!/usr/bin/python

import googlemaps
import sys
import csv

gmaps = googlemaps.Client(key='AIzaSyBmjaKszLBO5UPKvsVlyUgzC9Uwv2gUuR8')

# results = gmaps.geocode("3945 Waterford CT Orange OH")
#
# print(results[0].keys())
# print(results[0]["geometry"]["location"])


infile = open('missing.txt','r',encoding='utf-8')
tosearch = []
locations = []

for line in infile:
    locations.append([line, 0, 0])
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
        if "geometery" in results[0]:
            if "location" in results[0]["geometry"]:
                lat = results[0]["geometry"]["location"]["lat"]
                long = results[0]["geometry"]["location"]["lng"]
                locations[count][1] = lat
                locations[count][2] = long

with open("geomissing_out.csv", 'w', newline='', encoding='utf-8') as csvout:
    csvw = csv.writer(csvout)
    csvw.writerows(locations)
