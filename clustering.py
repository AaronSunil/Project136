from sklearn.cluster import KMeans
import matplotlib.pyplot as plt
import seaborn as sns
import csv
import pandas as pd

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

for star in star_Data_Rows:
  mass.append(star[3])
  radius.append(star[7])
  name.append(star[1])

gravity = []

for index,n in enumerate(name):
  g = (float(mass[index]) * 5.972e+24)/(float(radius[index]) * float(radius[index]) * 6371000 * 6371000) * 6.674e-11
  gravity.append(g)

low_gravity_star = []
for index, g in enumerate(gravity):
  if g < 100:
    low_gravity_star.append(star_Data_Rows[index])

print(len(low_gravity_star))

star_type_values = []

for star_data in star_Data_Rows:
  star_type_values.append(star_data[6])

print(list(set(star_type_values)))

star_masses = []
star_radius = []

for star in low_gravity_star:
  star_masses.append(star[3])
  star_radius.append(star[7])

X = []
for index, p_m in enumerate(star_masses):
  temp_list = [star_radius[index], star_masses]
  X.append(temp_list)

wcss = []
for i in range(1,11):
  kmeans = KMeans(n_clusters=i, init='k-means++', random_state=42)
  kmeans.fit(X)
  wcss.append(kmeans.inertia_)

plt.figure(figsize=(10,5))
sns.linePlot(x=range(1,11), y=wcss, marker='o', color='red')
plt.title('The Elbow Method')
plt.xlabel("Number of cluster")
plt.ylabel("WCSS")
plt.show()


