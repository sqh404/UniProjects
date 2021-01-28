#!/usr/bin/python

import sys
import csv

#move data from csv to 2D list
data = list(csv.reader(open('Meteorite_Landings_Cleaned.csv','r',encoding='utf-8')))
header = data.pop(0)

#split sitename and name-ID into seperate list elements
for row in data:
    #find last "word" in name value
    last_word = row[0].rfind(" ")
    if(last_word>0):
        #see if that "word" is actually an ID
        foundID = row[0][last_word+1:].isnumeric() or row[0][last_word+2:].isnumeric()
        if(foundID):
            #split
            nid = row[0][last_word+1:]
            name = row[0][:last_word]
            row[0] = name
            row.insert(1,nid)
        else:
            row.insert(1,"1")
    #default name ID = 1
    else:
        row.insert(1, "1")

header.insert(1,"nid")
with open("splitname_out.csv", 'w', newline='',encoding='utf-8') as csvout:
     csvw = csv.writer(csvout)
     csvw.writerow(header)
     csvw.writerows(data)