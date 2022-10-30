# Computational Methods - Week_2
# Plot the adiabatic temperature profile in Earth’s mantle

import numpy as np
import matplotlib.pyplot as plt

pot_temp = 1300 + 273.15 #in K 
mantle_thick = 2850 * pow(10,3) #in m
a = 2*pow(10, -5) #in 1/K (expansion coefficient)
g = 9.81 #in m/s^2
Cp = 1200 #in J/kg*K
Rp = 6371*pow(10,3) #in m 
R_core = Rp - mantle_thick #in m


radius = np.arange(R_core, Rp+1, 50*pow(10,3))
print(radius)
T = np.zeros(len(radius))
T[-1] = pot_temp
print(T)



for i in range(len(T)-1, 0, -1): 
    T[i-1] = (a*g/Cp) * T[i] * (radius[i] - radius[i-1]) + T[i]
                      
print(T) 

T[-1] = 300   
print(T)  

fig = plt.figure() 
plt.plot(T, radius/1000) #r in km
plt.grid()
plt.title("Adiabatic temperature profile in Earth’s mantle")
plt.xlabel('Temperature (K)')
plt.ylabel('Radius (km)')
plt.show()
fig.savefig("Week_2.png", dpi=200)