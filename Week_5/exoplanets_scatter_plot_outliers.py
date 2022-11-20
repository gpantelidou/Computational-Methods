# Computational Methods - Week_5
#Produce a scatter plot of all exoplanets, with mass in Earth masses on the x-axis 
#and radius in Earth radii on the y-axis. 
#Adapt the colors of the data points to the density of the planet.

import pandas as pd 
import planets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap


Earth_density = planets.density(5.972*10**24,6371*10**3)   
#print("Earth's density = ", Earth_density, "kg/m^3")

df = pd.read_csv("exoplanet.csv", usecols = ['# name','mass', 'radius'])

#Convert the masses and radii from Jupiter masses/radius to Earth masses and radii
df['mass'] = (df['mass'] * 1.898 * pow(10,27)) / (5.972 * pow(10,24))
df['radius'] = (df['radius'] * 6.9911 * pow(10,7)) / (6.371 * pow(10, 6))

#Convert the masses and radii from Earth masses/radius to kg and m to calculate density
df['mass_kg'] = df['mass'] * 5.972 * pow(10,24)
df['radius_m'] = df['radius'] * 6.371 * pow(10, 6)
df['density'] = planets.density(df['mass_kg'], df['radius_m'])


#new dataframe to store mass, radius values for terrestial planets in our solar system
df2 = pd.DataFrame({'# name': ['Mercury', 'Venus', 'Earth', 'Mars'],
                   'mass': [0.055, 0.815, 1, 0.107],
                   'radius': [0.383, 0.95, 1, 0.532]})

fig, ax = plt.subplots()

#Insert in the exoplanets scatterplot our terrestial planets
terrestial_planets = ['Mercury', 'Venus', 'Earth', 'Mars']
colors = ListedColormap(['g', 'y', 'b', 'r'])
# indexes that correspond to colors: 1st datapoint 0 green, 2nd datapoint 1 yellow etc
values = [0,1,2,3] 
mass_planet = df2['mass']
radius_planet = df2['radius']
im2 = ax.scatter(mass_planet, radius_planet, c=values, cmap = colors, s=100)
plt.legend(handles=im2.legend_elements()[0], labels = terrestial_planets)
#different color for each planet 

#create a new dataframe by selecting to keep values for the density up to 20000 kg/m^3
not_outliers_df = df.loc[df['density'].between(0,20000)]
density_not_outliers = not_outliers_df['density']
mass_not_outliers = not_outliers_df['mass']
radius_not_outliers = not_outliers_df['radius']

im = ax.scatter(mass_not_outliers, radius_not_outliers,
                c = density_not_outliers, zorder = 2, cmap = 'copper')

cbar = fig.colorbar(im, ax=ax)

 
ax.set(xlabel = 'Planet mass (Earth mass)', ylabel = 'Planet radius (Earth radii)', 
       title = 'Potentially rocky exoplanets')
cbar.set_label('density (kg/$m^{3}$)')
#ax.set_xlim(0, 10)
#ax.set_ylim(0, 2)
ax.grid(zorder = 0)

#for loop to enter the planet names in the graph
terrestial_planets_mass = df2['mass'].tolist()
terrestial_planets_radius = df2['radius'].tolist()
for i,j,z in zip(terrestial_planets_mass, terrestial_planets_radius, terrestial_planets):
    plt.text(i, j, z, 
          horizontalalignment = 'left',
          verticalalignment = 'top')


fig.savefig("Week_5.png", dpi=200)

