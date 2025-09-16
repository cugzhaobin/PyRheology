import numpy as np
import math
import matplotlib.pyplot as plt

def calc_T(z, Ts, Ti, G, thid):
    DEL = 2*(Ti-Ts)/(G*np.sqrt(np.pi))
    if thid == 2:
        T = [Ts+(Ti-Ts)*math.erf(z[i]/DEL) for i in range(len(z))]
        T = np.array(T)
    else:
        T = Ts+z*G
    return T