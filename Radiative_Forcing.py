import matplotlib.pyplot as plt
import numpy as np 

# Longwave radiative flux change due to a contrail
# Beer-Lambert Law
# Part a)
tau = 0.1
T = 288.15 # K
sigma = 5.670374419 * 10**(-8) # W/m^2/K^4 

F_in = sigma*(T**4)

print("Ingoing radiative flux [W/m^2]: ", np.round(F_in, 2))

F_out = F_in*np.exp(-tau)

#RFC_LW = F_out_nocontrail - F_out_contrail
RFC_LW = F_in * (1 - np.exp(-tau))
F_out_nc = RFC_LW + F_out

print("Radiative flux change RFClw [W/m^2]: ", np.round(RFC_LW, 2))

#-----------------------------
# Part B)
x = 1000 # m
t = 3*3600 # s

# Radiative force is independent of location and time 
EF = (RFC_LW*x*t) #Assuming 1D area projection 

print("Energy force per metre of contrail [Ws/m]: ", np.round(EF/10**8, 2)) 

#-----------------------------
# Part C + D)

d = 0.1*(50*10**9)*10**3 

ef_d = EF*d/(365.25*24*60**2) #J

print("Total energy forcing [TW]: ", np.round(ef_d/10**12, 2))

#-----------------------------
# Part e)

r = 6371*(10**3)                                      
ans = ef_d/(4*np.pi*r**2) 

print("Radiative forcing [mWm^-2]: ", np.round(ans*10**3, 2))