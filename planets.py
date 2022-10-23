# Computational Methods - Week_1
# Exercise 1.1 
# Define a function to calculate the density of Earth depending on its mass and radius.
# Use Earth values: M=5.972 × 10^24 kg, R=6371 km 
# Print the density (in kg/m^3)

from math import pi

def density (M,R):
    return (M/((4/3)*pi*R**3))

Earth_density = density(5.972*10**24,6371*10**3)   
#print("Earth's density = ", Earth_density, "kg/m^3")


   