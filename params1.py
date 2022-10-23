# Computational Methods - Week_1
# Exercise 1.2 
# Define two functions for mass and radius that use the planet name (“Earth“) 
# as input and return the mass and the radius of that planet,respectively.
# Call the density function by using the return value of the two params
# functions as input to calculate the density.


def mass(planet_mass):
    Earth_mass = 5.972*10**24
    return (Earth_mass)


def radius(planet_radius):
    Earth_radius = 6371*10**3
    return (Earth_radius)

planet = "Earth"
planet_mass = mass(planet)
print(planet, "mass = ", planet_mass, "kg")
planet_radius = radius("Earth")
print(planet, "radius = ", planet_radius, "m")


from planets import density

planet_density = density(planet_mass, planet_radius)
print(planet, "density = ", planet_density, "kg/m^3")








