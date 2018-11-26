#!/usr/bin/env python
# coding: utf-8
#Introducing US Gun Deaths Data
import csv
import datetime
f=open('guns.csv','r')
file=csv.reader(f)
data=list(file)
print(data[:5])
#Removing Headers from A List of Lists
header=data[0]
data=data[1:]
print(header)
print(data[:4])
year_counts ={}
years_counts=0
years=[]
sexs=[]
races=[]
intents=[]
for row in data:
    year=row[1]
    sex=row[5]
    race=row[7]
    intt=row[3]
    intents.append(intt)
    years.append(year)
    sexs.append(sex)
    races.append(race)
#years=list(years)
#print(years)
# Counting Gun Deaths By Year
for year in years:
    if year not in year_counts:
        year_counts[year]=0
    else:
        year_counts[year] +=1
print(year_counts)
#Exploring Gun Deaths by Month and Year
dates=[datetime.datetime(year=int(row[1]),month=int(row[2]),day = 1) for row in data]
date_counts={}
for d in dates:
    if d in date_counts.keys():
        date_counts[d] +=1
    else:
        date_counts[d] = 1
print(date_counts[datetime.datetime(2012, 1, 1, 0, 0)])
#Exploring Gun Deaths by Race and Sex
sex_counts={}
for d in sexs:
    if d in sex_counts.keys():
        sex_counts[d] += 1
    else:
        sex_counts[d] = 1
print(sex_counts)

race_counts={}
for d in races:
    if d in race_counts.keys():
        race_counts[d] += 1
    else:
        race_counts[d] = 1
print(race_counts)

# Second dataset
import csv
f= open('census.csv','r')
census=csv.reader(f)
census=list(census)
#print(census)
census=census[1:]
#print(census)
# computing rates of gun deaths per race
for a in census:
    a1= int(a[14])+ int(a[15])
    a2= int(a[12])
    a3= int(a[13])
    a4= int(a[11])
    a5= int(a[10])
list1=[a1,a2,a3,a4,a5]
print(list1)
mapping=dict(zip(["Asian/Pacific Islander","Black","Native American/Native Alaskan","Hispanic","White"],list1))
print(mapping)

race_per_hundredk=dict((k,race_counts[k]/mapping[k] * 100000) for k in race_counts)
print(race_per_hundredk)

#Filtering by Intent
intents=list(intents)
#print(intents)
#print(races)
homicide_race_counts={}

for i,race in enumerate(races):
    if race not in homicide_race_counts:
        homicide_race_counts[race] = 0
    if intents[i]=="Homicide":
        homicide_race_counts[race] += 1
print(homicide_race_counts)

race_per_hundredk=dict((k,homicide_race_counts[k]/mapping[k] * 100000) for k in homicide_race_counts)
print(race_per_hundredk)

