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
LHVk = 120 # MJ/kg
T = 225 # K
nu = 0.3 

# es = np.exp(a_ei[0]*(1/T**(-3)) + a_ei[1]*(1/T**-2) + a_ei[2]*(1/T) + a_ei[3] + a_ei[4]*T + a_ei[5]*T**2 + a_ei[5]*np.log(T))
# print(es)

G = cpk * p * EIh20 / (eta * (1-nu) * LHVk)
print(eta * (1-nu) * LHVk)
print(G)

fig, ax = plt.subplots(1, 2, figsize=(10, 5))

ax[0].plot(np.arange(210, 253), ep_el, label= r'$e_{l}$', color = 'purple')
ax[0].set_title(r'Saturation pressure [Pa] vs $e_{l}$ [K]')
ax[0].set_xlabel('Temperature [K]')
ax[0].set_ylabel('Saturation pressure [Pa]')
ax[0].grid()
ax[0].legend()

ax[1].plot(np.arange(210, 253), ep_ei, label=r'$e_{i}$', color = 'orange')
ax[1].set_title(r'Saturation pressure [Pa] vs $e_{i}$ [K]')
ax[1].set_xlabel('Temperature [K]')
ax[1].set_ylabel('Saturation pressure [Pa]')
ax[1].grid()
ax[1].legend()
plt.show()