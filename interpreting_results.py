import pandas as pd
import plotly.express as px
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

mass = []
radius = []
name = []
distance = []

for star in star_Data_Rows:
  mass.append(star[3])
  radius.append(star[4])
  name.append(star[1])
  distance.append(star[2])

gravity = []

for index,n in enumerate(name):
  g = (float(mass[index]) * 5.972e+24)/(float(radius[index]) * float(radius[index]) * 6371000 * 6371000) * 6.674e-11
  gravity.append(g)

fig = px.scatter(x=name, y=mass, hover_data=[name])
fig.show()

fig = px.scatter(x=name, y=radius, hover_data=[name])
fig.show()

fig = px.scatter(x=name, y=distance, hover_data=[name])
fig.show()

fig = px.scatter(x=name, y=mass, hover_data=[name])
fig.show()