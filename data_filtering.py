import pandas as pd
import matplotlib as plt
import csv

rows = []
with open("final_data.csv", "r") as f:
  csv_reader = csv.reader(f)
  for row in csv_reader:
    rows.append(row)

headers = rows[0]
star_Data_Rows = rows[1:]

print(headers)
print(star_Data_Rows[0])

di = []
mass = []
radius = []
name = []

for star in star_Data_Rows:
    di.append(star[2])
    mass.append(star[3])
    radius.append(star[4])
    name.append(star[1])

gravity = []

for index,n in enumerate(name):
  g = (float(mass[index]) * 5.972e+24)/(float(radius[index]) * float(radius[index]) * 6371000 * 6371000) * 6.674e-11
  gravity.append(g)

if star[2] <= 100:
   di.append()

for star_data in di:  
    if gravity[8] < 150 or gravity > 300:
        di.remove(star_data)

di.to_csv('filtered_data.csv')
