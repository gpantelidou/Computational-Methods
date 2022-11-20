# Computational Methods - Week_5
#Produce a scatter plot of all exoplanets, with mass in Earth masses on the x-axis 
#and radius in Earth radii on the y-axis. 
#Adapt the colors of the data points to the density of the planet.

import pandas as pd 
import planets
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap
import matplotlib.image as image
from matplotlib.offsetbox import (OffsetImage, AnnotationBbox)

Earth_density = planets.density(5.972*10**24,6371*10**3)   
print("Earth's density = ", Earth_density, "kg/m^3")

df = pd.read_csv("exoplanet.csv", usecols = ['# name','mass', 'radius'])
#Convert the masses and radii from Jupiter masses/radius to Earth masses and radii
df['mass'] = (df['mass'] * 1.898 * pow(10,27)) / (5.972 * pow(10,24))
df['radius'] = (df['radius'] * 6.9911 * pow(10,7)) / (6.371 * pow(10, 6))

#Convert the masses and radii from Earth masses/radius to kg and m to calculate density
df['mass_kg'] = df['mass'] * 5.972 * pow(10,24)
df['radius_m'] = df['radius'] * 6.371 * pow(10, 6)
df['density'] = planets.density(df['mass_kg'], df['radius_m'])

#new dataframe to store mass, radius values for terrestial planets in our solar system
df2 = pd.DataFrame({'name': ['Mercury', 'Venus', 'Earth', 'Mars'],
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
im2 = ax.scatter(mass_planet, radius_planet, c=values, cmap = colors, s=100, zorder = 3)
plt.legend(handles=im2.legend_elements()[0], labels = terrestial_planets)

#Insert images for our planets using a for loop
image_files = ['Mercury.png', 'Venus.png', 'Earth.png', 'Mars.png']
for planet, file in zip(terrestial_planets, image_files):
    planet_image = image.imread(file)
    imagebox = OffsetImage(planet_image, 
                           zoom = 0.05 if (planet == 'Earth' or planet == 'Venus') else 0.12)
    abox = AnnotationBbox(imagebox, (df2.mass[df2.name.loc[df2.name == planet].index[0]], 
                                     df2.radius[df2.name.loc[df2.name == planet].index[0]]),
    frameon=False)
    ax.add_artist(abox)  
          
    
#Calculate outliers using IQR
Q1 = df['density'].quantile(0.25)
Q3 = df['density'].quantile(0.75)
IQR = Q3 - Q1
lower_lim = Q1 - 1.5 * IQR
upper_lim = Q3 + 1.5 * IQR
no_outliers = df.density[(lower_lim < df.density) &  (df.density < upper_lim)]
outliers = df.density[(lower_lim >= df.density) |  (df.density >= upper_lim)]

#create a new dataframe for no_outliers
df_IQR = df[(lower_lim < df.density) & (df.density < upper_lim)]

mass_IQR = df_IQR['mass'] 
radius_IQR = df_IQR['radius'] 

im = ax.scatter(mass_IQR, radius_IQR,
                c = no_outliers, zorder = 2, cmap = 'copper')


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
          verticalalignment = 'top', 
          zorder = 4)
    
    
fig.savefig("Week_5_pics.png", dpi=200)
