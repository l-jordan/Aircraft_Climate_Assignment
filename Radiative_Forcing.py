import matplotlib.pyplot as plt
import numpy as np 

# Longwave radiative flux change due to a contrail
# Beer-Lambert Law
# PART A)
tau = 0.1
T = 288.15 # K
sigma = 5.670374419 * 10**(-8) # W/m^2/K^4 

F_in = sigma*(T**4)

F_out = F_in*np.exp(-tau)

#RFC_LW = F_out_nocontrail - F_out_contrail
RFC_LW = F_in * (1 - np.exp(-tau))
F_out_nc = RFC_LW + F_out

print("Radiative flux change RFClw [W/m^2]: ", RFC_LW)

#-----------------------------
#PART B)
x = 1000 # m
t = 3*3600 # s
#Radiative force is independent of location and time 
EF = (RFC_LW*x*t) #Assuming 1D area projection 

print("Energy force per metre of contrail [W*s/m]: ", EF) # J/m 

#-----------------------------
#PART C + D)

d = 0.1*(50*10**9)*10**3 

ef_d = EF*d/(365.25*24*60**2) #J

print("Total energy forcing []: ",ef_d)

#-----------------------------
#PART E)

r = 6371*(10**3)
print(4*np.pi*r**2)                                         
ans = ef_d/(4*np.pi*r**2) 

print("Radiative forcing (mWm^-2): ", ans*10**3)