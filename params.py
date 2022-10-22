def mass(planet_name):
    Earth_mass = 5.972*10**24
    planet_mass_in_Earth_m = {"Mercury": 0.0553, 
                              "Venus": 0.815,
                              "Earth": 1,
                              "Mars": 0.107,
                              "Jupiter": 317.83,
                              "Saturn": 95.162,
                              "Uranus": 14.536,
                              "Neptune": 17.147}
    planet_mass = planet_mass_in_Earth_m[planet_name]
    return (planet_mass * Earth_mass)


def radius(planet_name):
    Earth_radius = 6371*10**3
    planet_radius_in_Earth_R = {"Mercury": 0.3829, 
                              "Venus": 0.9499,
                              "Earth": 1,
                              "Mars": 0.532,
                              "Jupiter": 10.97,
                              "Saturn": 9.14,
                              "Uranus": 3.981,
                              "Neptune": 3.865}
    planet_radius = planet_radius_in_Earth_R[planet_name]
    return (planet_radius * Earth_radius)


from planets import density

planets_solar_system = ["Mercury", "Venus", "Earth", "Mars", 
                        "Jupiter", "Saturn", "Uranus", "Neptune"]

for i in range(len(planets_solar_system)):
    current_planet = planets_solar_system[i]
    planet_density = density(mass(current_planet), radius(current_planet))
    print (current_planet,"ρ =", planet_density, "kg/m^3")
    
    

#planet_density = density(planet_mass, planet_radius)
#print(planet, "density = ", planet_density, "kg/m^3")



#planet = "Earth"
#planet_mass = mass(planet)
#print(planet, "mass = ", planet_mass, "kg")
#planet_radius = radius("Earth")
#print(planet, "radius = ", planet_radius, "m")




