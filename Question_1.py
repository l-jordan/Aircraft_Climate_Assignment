import matplotlib.pyplot as plt
import numpy as np

# Coeeficients used within the approximation of the saturation vapour pressure
a_el = [-0.58002206*10**(4), 1.3914993, -0.48640239*10**(-1), 0.41764768*10**(-4),  -0.14452093*10**(-7), 0]
a_ei = [-0.56745359*10**(4), 6.3925247, -0.96778430*10**(-2), 0.62215701*10**(-6), 0.20747825*10**(-8), -0.94840240*(10**(-12))]
bel = 6.5459673
bei = 4.1635019

ep_el = []
ep_ei = []
G = []

# Saturation pressure [Pa] vs el and ei [K]
for T in np.arange(210, 253):
    el_e = a_el[0]*(1/T) + a_el[1] + a_el[2]*T + a_el[3]*T**2 + a_el[4]*T**3 + a_el[5]*T**4
    ei_e = a_ei[0]*(1/T) + a_ei[1] + a_ei[2]*T + a_ei[3]*T**2 + a_ei[4]*T**3 + a_ei[5]*T**4
    ep_el.append(np.exp(bel*np.log(T) + el_e))
    ep_ei.append(np.exp(bei*np.log(T) + ei_e))

#------------------------------------------
# Fuel parameters and physical constants
cpk = 1004 # J/kg/K
p = 220*10**2 # Pa
EIh20 = 1.25 # kg/kg
eta = 0.622 # - 
LHVk = 43.2 * 10**6 # J/kg
T = 225 # K
nu = 0.3 
rhi = 110/100

# b) Mixing line slope
G = cpk * p * EIh20 / (eta * (1-nu) * LHVk)
print("The mixing line slope for b) is", G)

e_initial_e = a_ei[0]*(1/T) + a_ei[1] + a_ei[2]*T + a_ei[3]*T**2 + a_ei[4]*T**3 + a_ei[5]*T**4
ep_initial = (np.exp(bei*np.log(T) + e_initial_e))*rhi
print(ep_initial)

# c) New mixing slope for engine efficiency
nu = 0.4
G2 = cpk * p * EIh20 / (eta * (1-nu) * LHVk)
print(G2)
# d) New mixing slope for hydrogen

nu = 0.3
EIh20h = 8.94 # kg/kg
LHVh = 120 * 10**6 # J/kg

G3 = cpk * p * EIh20h / (eta * (1-nu) * LHVh)
print(G3)
plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'black')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = '#D2386C')
plt.plot(T, ep_initial, color = '#FFCBA4', marker = 'o', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G, color = '#D4A5EB', linestyle = '-.', label=r'Mixing line for kerosene condition $\eta$ = 0.3')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G2, color = 'pink', linestyle = '-.', label=r'Mixing line for kerosene condition $\eta$ = 0.4')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G3, color = '#FFCBA4', linestyle = '-.', label=r'Mixing line for hydrogen condition $\eta$ = 0.3')
plt.ylim(0, ep_el[-1])
plt.title(r'Saturation pressure [Pa] vs Temperature [K] with Relative Humidity w.r.t. Ice')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()









