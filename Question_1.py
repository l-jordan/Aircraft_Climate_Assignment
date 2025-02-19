import matplotlib.pyplot as plt
import numpy as np

a_el = [-0.58002206*10**(4), 1.3914993, -0.48640239*10**(-1), 0.41764768*10**(-4),  -0.14452093*10**(-7), 0]
a_ei = [-0.56745359*10**(4), 6.3925247, -0.96778430*10**(-2), 0.62215701*10**(-6), 0.20747825*10**(-8), -0.94840240*(10**(-12))]
bel = 6.5459673
bei = 4.1645019

ep_el = []
ep_ei = []
G = []

#Saturation pressure [Pa] vs el and ei [K]
for T in np.arange(210, 253):
    el_e = a_el[0]*(1/T) + a_el[1] + a_el[2]*T + a_el[3]*T**2 + a_el[4]*T**3 + a_el[5]*T**4
    ei_e = a_ei[0]*(1/T) + a_ei[1] + a_ei[2]*T + a_ei[3]*T**2 + a_ei[4]*T**3 + a_ei[5]*T**4
    ep_el.append(np.exp(bel*np.log(T) + el_e))
    ep_ei.append(np.exp(bei*np.log(T) + ei_e))


cpk = 1004 # J/kg/K
p = 220*10**2 # Pa
EIh20 = 1.25 # kg/kg
eta = 0.622 # - 
LHVk = 43.2 * 10**6 # J/kg
T = 225 # K
nu = 0.3 
rhi = 110/100


G = cpk * p * EIh20 / (eta * (1-nu) * LHVk)

#MIXING LINE
e_initial_e = a_ei[0]*(1/T) + a_ei[1] + a_ei[2]*T + a_ei[3]*T**2 + a_ei[4]*T**3 + a_ei[5]*T**4
ep_initial = (np.exp(bei*np.log(T) + e_initial_e))*rhi

#THRESHOLD
Tlm = (-46.46+9.43*np.log(G-0.053)+0.720*(np.log(G-0.053))**2)+273.15
e_initial_elm = a_ei[0]*(1/Tlm) + a_ei[1] + a_ei[2]*Tlm + a_ei[3]*Tlm**2 + a_ei[4]*Tlm**3 + a_ei[5]*Tlm**4
ep_initial_lm = (np.exp(bei*np.log(Tlm) + e_initial_elm))*rhi


plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G, 'r-', label='Mixing line')
plt.plot(np.arange(210, 253), ep_initial_lm + (np.arange(210, 253)-Tlm) * G, 'green', label='Threshold line')
#plt.fill_between(np.arange(210, 253), ep_el, ep_ei, color='gray', alpha=0.3)
#plt.fill_between(np.arange(210, 253), ep_ei, ep_initial_lm + (np.arange(210, 253)-Tlm) * G, color='white', alpha=0.3)
plt.ylim(0, ep_el[-1])
plt.title(r'Saturation pressure [Pa] vs Temperature [K]')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()

#--------------------------------------------
# c)

nu = 0.4
G2 = cpk * p * EIh20 / (eta * (1-nu) * LHVk)

Tlm2 = (-46.46+9.43*np.log(G2-0.053)+0.720*(np.log(G2-0.053))**2)+273.15
e_initial_elm2 = a_ei[0]*(1/Tlm2) + a_ei[1] + a_ei[2]*Tlm2 + a_ei[3]*Tlm2**2 + a_ei[4]*Tlm2**3 + a_ei[5]*Tlm2**4
ep_initial_lm2 = (np.exp(bei*np.log(Tlm2) + e_initial_elm2))*rhi

plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G2, 'r-', label='Mixing line')
plt.plot(np.arange(200, 253), ep_initial_lm2 + (np.arange(200, 253) - Tlm2) * G2, 'green', label='Threshold line')
plt.ylim(0, ep_el[-1])
plt.title(r'Saturation Pressure [Pa] vs Temperature [K] for $\eta$ =  0.4')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()

#--------------------------------------------
# d)
nu = 0.3
EIh20h = 8.94 # kg/kg
LHVh = 120 * 10**6 # J/kg

G3 = cpk * p * EIh20h / (eta * (1-nu) * LHVh)

Tlm3 = (-46.46+9.43*np.log(G3-0.053)+0.720*(np.log(G3-0.053))**2)+273.15
e_initial_elm3 = a_ei[0]*(1/Tlm3) + a_ei[1] + a_ei[2]*Tlm3 + a_ei[3]*Tlm3**2 + a_ei[4]*Tlm3**3 + a_ei[5]*Tlm3**4
ep_initial_lm3 = (np.exp(bei*np.log(Tlm3) + e_initial_elm3))*rhi

plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G3, 'r-', label='Mixing line')
plt.plot(np.arange(200, 253), ep_initial_lm3 + (np.arange(200, 253) - Tlm3) * G3, 'green', label='Threshold line')
plt.ylim(0, ep_el[-1])
plt.title(r'Hydrogen Conditions Saturation pressure [Pa] vs Temperature [K] for $\eta$ = 0.3')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()

