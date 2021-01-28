#!/usr/bin/python

import sys
import csv

#move data from csv to 2D list
data = list(csv.reader(open('landings_split.csv','r',encoding='utf-8')))
header = data.pop(0)
missing = set()


locations = {}
line = 0;
for row in data:
    name = row[0]
    lat = row[7]
    long = row[8]

    #check to see if geolocation is available
    if lat is not "" and long is not "":
        if lat != "0" or long != "0":
            flat = float(lat)
            flong = float(long)
            #add to dictionary if first time
            if locations.get(name) is None:
                locations.update({name:[1,flat,flong]})
            #compute running total otherwise
            else:
                counter = 1 + locations.get(name)[0]
                sumlat = flat + locations.get(name)[1]
                sumlong = flong + locations.get(name)[2]
                locations.update({name:[counter, sumlat,sumlong]})

#find averages for all locations
for loc in locations.values():
    count = loc[0]
    avglat = loc[1]/count
    avglong = loc[2]/count
    loc[1] = round(avglat, 5)
    loc[2] = round(avglong, 5)

imputecount = 0
missingcount = 0
#impute missing location values with calculated averages
for row in data:
    name = row[0]
    lat = row[7]
    long = row[8]

    #check to see if geolocation is unavailable, then replace with average
    if lat is "" and long is "" or lat == "0" and long == "0":
        if name in locations:
            newlat = locations.get(name)[1]
            newlong = locations.get(name)[2]
            geolocation = "(" + str(newlat) + ", " + str(newlong) + ")"
            row[7] = newlat
            row[8] = newlong
            row[9] = geolocation
            imputecount += 1
        else:
            missing.add(name)
            missingcount += 1

print("Total imputed is ", imputecount)
print("Total still missing is ", missingcount)
print("Number of locations with missing values: ", len(missing))

with open("imputedlocation_out.csv", 'w', newline='',encoding='utf-8') as csvout:
     csvw = csv.writer(csvout)
     csvw.writerow(header)
     csvw.writerows(data)


locheader = ["sitename", "count","avg_latitude","avg_longitude"]
loclist = []
for key, value in locations.items():
    temp = [key, value[0], value[1], value[2]]
    loclist.append(temp)

with open("averagelocation_out.csv", 'w', newline='',encoding='utf-8') as csvout:
     csvw = csv.writer(csvout)
     csvw.writerow(locheader)
     csvw.writerows(loclist)

with open("averagelocation_min2.csv", 'w', newline='', encoding='utf-8') as csvout:
    csvw = csv.writer(csvout)
    csvw.writerow(locheader)
    for loc in loclist:
        if int(loc[1]) > 1:
            csvw.writerow(loc)

with open("missinglocation_out.txt", 'w', newline='', encoding='utf-8') as txtout:
    for location in missing:
        print(location,file=txtout)


