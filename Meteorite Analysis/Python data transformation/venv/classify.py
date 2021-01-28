#!/usr/bin/python

import sys
import csv

chondrites = {"Carbonaceous":['C','CV', 'CK', 'CM', 'CO', 'CR','CH','CB'],
              "Ordinary":['H','L','LL','OC'],
              "Enstatite":['E','EH','EL'],
              "Other":['R','K'],
              "Ungrouped":['chondrite','Chondrite']}

achondrites = {"Primitive":["Acapulcoite","Lodranite","Winonaite","prim"],
               "Asteroidal":["Howardite","Eucrite","Diogenite","Angrite","Aubrite","Ureilite","Brachinite"],
               "Lunar":["Lunar"],  #group may be listed in paren
               "Martian":["Martian"],
               "Ungrouped":["Achondrite-ung"]} #group may be listed in paren

stony_iron = {"Pallasite":["PES","PMG"],
              "Mesosiderite":["-A","-B","-C"]}

iron = {"Magmatic":['IC','IIAB','IIC','IID','IIF','IIG','IIIAB','IIIE','IIIF','IVA','IVB'],
        "Non-magmatic":['IAB complex','IAB-MG','IAB-sHH','IAB-sHL','IAB-sLH','IAB-sLL','IAB-sLM',' IAB',' IIE']}


# test_set = str.split(open("reclasses.csv","r").read(),',')
data = list(csv.reader(open('imputedlocation_out.csv','r',encoding='utf-8')))
header = data.pop(0)

output = []

def categorize(reclass):
    category, mclass, group, mtype = '','','',''

    if "Iron" in reclass or "iron" in reclass:
        category = "Iron"
        for cl, groups in iron.items():
            for g in groups:
                if g in reclass:
                    mclass = cl
                    group = g

    else:
        for cl, groups in achondrites.items():
            for g in groups:
                if g in reclass:
                    category = "Achondrite"
                    mclass = cl
                    if mclass in ['Lunar', 'Martian']:
                        if reclass.find('(')>0:
                            group = reclass[reclass.find('(')+1:reclass.find(')')]
                    elif mclass != "Ungrouped":
                        group = g
        for cl, groups in stony_iron.items():
            if cl in reclass:
                category = "Stony_Iron"
                mclass = cl
                for g in groups:
                    if g in reclass:
                        group = g
    if category == '':
        for cl, groups in chondrites.items():
            for g in groups:
                if reclass.find(g)==0:
                    category = "chondrite"
                    mclass = cl
                    group = g
                    parse = list(reclass)
                    for ch in parse:
                        if str.isdigit(ch):
                            mtype=ch
                            break


    if category == '': category = "Ungrouped"
    return [reclass, category, mclass, group, mtype]

#print(categorize("Acapulcoite"))
# for reclass in test_set:
#     output.append(categorize(reclass))
#
header.insert(4,"Category")
header.insert(5,"Class")
header.insert(6,"Group")
header.insert(7,"ChonType")
for row in data:
    catlist = categorize(row[3])
    row.insert(4,catlist[1])
    row.insert(5,catlist[2])
    row.insert(6,catlist[3])
    row.insert(7,catlist[4])

with open("classifyoutput.csv", 'w', newline='', encoding='utf-8') as csvout:
    csvw = csv.writer(csvout)
    csvw.writerow(header)
    csvw.writerows(data)