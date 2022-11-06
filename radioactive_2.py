import numpy as np
import matplotlib.pyplot as plt 

data = np.array([[4.47*pow(10,9), 2.02*pow(10,-8), 9.46*pow(10,-5)], 
                [7.04*pow(10,8), 1.44*pow(10,-10), 5.69*pow(10,-4)],
                [1.40*pow(10,10), 7.95*pow(10,-8), 2.64*pow(10,-5)],
                [1.25*pow(10,9), 3.07*pow(10,-8),  2.92*pow(10,-5)]])

radionuclides = ['U-238', 'U-235', 'Th-232', 'K-40']

lambda_values = np.zeros(data.shape[0])
for i in range(len(data)):
    lambda_values[i] = -np.log(0.5) / data[i,0]
    print(lambda_values[i])
    
print("\n")    
    

C = np.zeros(data.shape[0])
for i in range(len(data)):
    C[i] = data[i,1] * np.exp(-lambda_values[i]* 4.5*pow(10,9))
    print(C[i])
    
print("\n")       
    
time = np.linspace(0, 4.5*pow(10, 9), 50)
print(time)

print("\n")    


C1_values = np.zeros(time.shape[0])
C2_values = np.zeros(time.shape[0])
C3_values = np.zeros(time.shape[0])
C4_values = np.zeros(time.shape[0])

for i in range(len(time)):
    C1_values[i] = C[0] * np.exp(-lambda_values[0] * time[i])
    C2_values[i] = C[1] * np.exp(-lambda_values[1] * time[i])
    C3_values[i] = C[2] * np.exp(-lambda_values[2] * time[i])
    C4_values[i] = C[3] * np.exp(-lambda_values[3] * time[i])

H1 = data[0,2]
H2 = data[1,2]
H3 = data[2,2]
H4 = data[3,2]

H1_curve = H1 * C1_values
H2_curve = H2 * C2_values
H3_curve = H3 * C3_values
H4_curve = H4 * C4_values

H_curve = H1_curve + H2_curve + H3_curve + H4_curve 

plt.plot(time/pow(10,9), H1_curve)
plt.plot(time/pow(10,9), H2_curve)
plt.plot(time/pow(10,9), H3_curve)
plt.plot(time/pow(10,9), H4_curve)
plt.plot(time/pow(10,9), H_curve)
plt.xlabel("Time [Gyr]")
plt.ylabel("Radioactive Heating [W/kg]")
plt.grid()
plt.show()    


