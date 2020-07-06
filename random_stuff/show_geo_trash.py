import matplotlib.pyplot as plt
import pandas as pd
import geopandas as gpd
from matplotlib.patches import Ellipse
from generate_dummy_data import get_random_point_in_amsterdam

import contextily as ctx

df = pd.read_csv('dummy_data.csv')

print(df.head())

df_areas = gpd.read_file('datasets/amsterdam_areas.geojson')
df_containers = gpd.read_file('datasets/waste_containers.geojson')

# garbage_types = df_containers["waste_name"].unique()
garbage_types = ['Rest', 'GFT', 'Papier', 'Unkown', 'Plastic', 'Glas', 'Textiel']
garbage_colors = ['gray', 'green', 'white', 'black', 'blue', 'lightblue', 'orange']

fig, ax = plt.subplots(1, figsize=(8, 8))
df_areas.plot(ax=ax, color='brown')

for t, c in zip(garbage_types, garbage_colors):
    df_containers[df_containers["waste_name"] == t].plot(ax=ax, color=c, markersize=2, label=t)

# ellipse = Ellipse((4.89, 52.37), 0.2, 0.1, color='r', fill=False)
# ax.add_patch(ellipse)

for i in range(100):
    y, x = get_random_point_in_amsterdam()
    plt.scatter(x, y, color='magenta', s=10, marker="x")

ax.set_xlim(4.89 - 0.15, 4.89 + 0.15)
ax.set_ylim(52.37 - 0.1, 52.37 + 0.1)
ctx.add_basemap(ax, zoom=15)

ax.set_aspect(aspect=1.5)
plt.legend()
plt.tight_layout()
plt.show()


# try plotting (major) streets as well
