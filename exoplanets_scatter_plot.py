# Computational Methods - Week_4
#Produce a scatter plot of all exoplanets, with mass in Earth masses on the x-axis 
#and radius in Earth radii on the y-axis. 
#Adapt the colors of the data points to the density of the planet.

import pandas as pd 
import planets
import matplotlib.pyplot as plt

Earth_density = planets.density(5.972*10**24,6371*10**3)   
print("Earth's density = ", Earth_density, "kg/m^3")

df = pd.read_csv("exoplanet.csv", usecols = ['# name','mass', 'radius',
                                             'mass_error_min', 'mass_error_max',
                                             'radius_error_min', 'radius_error_max'])
#Convert the masses and radii from Jupiter masses to Earth masses and radii
df['mass'] = (df['mass'] * 1.898 * pow(10,27)) / (5.972 * pow(10,24))
df['radius'] = (df['radius'] * 6.9911 * pow(10,7)) / (6.371 * pow(10, 6))
df['density'] = planets.density(df['mass'], df['radius'])

df['mass_error_min'] = (df['mass_error_min'] * 1.898 * pow(10,27)) / (5.972 * pow(10,24))
df['mass_error_max'] = (df['mass_error_max'] * 1.898 * pow(10,27)) / (5.972 * pow(10,24))
df['radius_error_min'] = (df['radius_error_min'] * 6.9911 * pow(10,7)) / (6.371 * pow(10, 6))
df['radius_error_max'] = (df['radius_error_max'] * 6.9911 * pow(10,7)) / (6.371 * pow(10, 6))

fig, ax = plt.subplots()
x = df['mass']
y = df['radius']
z = df['density']

xerrormin = df['mass_error_min']
xerrormax = df['mass_error_max']
yerrormin = df['radius_error_min']
yerrormax = df['radius_error_max']

xerror = [xerrormin, xerrormax]
yerror = [yerrormin, yerrormax]


max_density = df['density'].max()
min_density = df['density'].min()
mean_density = df['density'].mean()

max_lim = min_density + mean_density

im = ax.scatter(x, y, c = z, zorder = 2)
cbar = fig.colorbar(im, ax=ax)
im.set_clim(min_density, max_lim)
ax.set(xlabel = 'Planet mass (Earth mass)', ylabel = 'Planet radius (Earth radii)', 
       title = 'Potentially rocky exoplanets')
cbar.set_label('density (kg/$m^{-3}$)')
ax.errorbar(x, y, xerr = xerror, yerr = yerror,  fmt='.k', capsize = 2, zorder = 1)
#ax.set_xlim(0, 10)
#ax.set_ylim(0, 2)
ax.grid(zorder = 0)

fig.savefig("Week_4.png", dpi=200)

