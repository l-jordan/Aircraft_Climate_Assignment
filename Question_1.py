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
rh = 110/100

# es = np.exp(a_ei[0]*(1/T**(-3)) + a_ei[1]*(1/T**-2) + a_ei[2]*(1/T) + a_ei[3] + a_ei[4]*T + a_ei[5]*T**2 + a_ei[5]*np.log(T))
# print(es)

G = cpk * p * EIh20 / (eta * (1-nu) * LHVk)
print(G)

e_initial_e = a_ei[0]*(1/T) + a_ei[1] + a_ei[2]*T + a_ei[3]*T**2 + a_ei[4]*T**3 + a_ei[5]*T**4
ep_initial = (np.exp(bei*np.log(T) + e_initial_e)) * rh
print(ep_initial)

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

plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G, 'r-', label='Mixing line')
plt.title(r'Saturation pressure [Pa] vs Temperature [K]')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()


#test

# we should probably have both plots in the same figure and then just add the mixing line starting at T = 225K, and saturation pressure = ep_initial

# c) New value for engine efficiency

nu = 0.4
G2 = cpk * p * EIh20 / (eta * (1-nu) * LHVk)
print(G2)

plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G2, 'r-', label='Mixing line')
plt.title(r'Saturation pressure [Pa] vs Temperature [K]')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()

# d)

nu = 0.3
EIh20h = 8.94 # kg/kg
LHVh = 120 * 10**6 # J/kg

G3 = cpk * p * EIh20h / (eta * (1-nu) * LHVh)
print(G3)

plt.plot(np.arange(210, 253), ep_el, label= "Saturation w.r.t. liquid", color = 'purple')
plt.plot(np.arange(210, 253), ep_ei, label= "Saturation w.r.t. ice", color = 'orange')
plt.plot(T, ep_initial, 'ro', label='Atmospheric condition')
plt.plot(np.arange(T, 253), ep_initial + (np.arange(T, 253) - T) * G3, 'r-', label='Mixing line')
plt.title(r'Saturation pressure [Pa] vs Temperature [K]')
plt.xlabel('Temperature [K]')
plt.ylabel('Saturation pressure [Pa]')
plt.grid()
plt.legend()
plt.show()


# e) for all three mixing lines, contrails form, but they are only persistent for the third mixing line ( d) ). (TO BE VERIFIED)

