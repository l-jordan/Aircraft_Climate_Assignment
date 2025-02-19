import matplotlib.pyplot as plt
import numpy as np 

# Longwave radiative flux change due to a contrail
# Beer-Lambert Law

tau = 0.1
T = 288.15 # K
sigma = 5.670374419 * 10**(-8) # W/m^2/K^4 

F_in = sigma * T**4

F_out = F_in *np.exp(-tau)


RFC_LW = F_out_nocontrail - F_out_contrail
RFC_LW2 = F_in * (1 - np.exp(-tau))