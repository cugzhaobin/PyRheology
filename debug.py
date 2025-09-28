import rheology
import numpy as np
import calc_temperature
depth = np.arange(0,100,1)

rhe   = rheology.flow_law(12.7, 3.0, 0, 0, 1000, 1.2, 641e3, 1e9, 24e-6, 600+273, epsilon=1e-12)
print(f'{rhe.get_viscosity():e}')