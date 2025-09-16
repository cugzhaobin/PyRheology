import numpy as np
class flow_law(object):
    '''
    A power law dependence of strain rate on differential stress.
                                          Q+PV  
    epsilon = A*signma^n*d^(-m)*Coh^r*exp(----)
                                          -RT
    epsilon is strain rate
    '''
    def __init__(self, A, n, d, m, Coh, r, Q, P, V, T, R=8.314, sigma=None, epsilon=None):
        '''
        If m is 0, dislocation creep
        If n is 0, diffisioin creep
            A     = pre-exponential factor, 1/(Pa^(-n)*s)
            n     = stress exponent
            d     = grain size, um = 1e-6 m
            m     = grain size exponent
            Coh   = water concentration, ppm H/Si
            r     = water concentration exponent
            Q     = activation energy, J/mol
            p     = confining pressure, Pa
            V     = activation volume, m^3/mol
            R     = universal gas constant, J/(mol*K)
            T     = temperature, (K)
            sigma = deviatoric stress, Pa
            epsilon = strain rate in /s
        '''

        self.A     = A
        self.n     = n
        self.d     = d
        self.m     = m
        self.Coh   = Coh
        self.r     = r
        self.Q     = Q
        self.P     = P
        self.V     = V
        self.R     = R
        self.T     = T
        self.sigma = sigma
        self.epsilon=epsilon
        return


    def GetEpsilon(self):
        '''
        '''
        epsilon = None
        if self.sigma != None:
            print(self.A, self.sigma, self.n)
            epsilon = self.A * self.sigma**self.n *\
                      self.d**(-self.m) * self.Coh**self.r *\
                      np.exp(-(self.Q+self.P*self.V)/(self.R*self.T))
        return epsilon

    def viscosity(self):
        '''
        Calculate viscosity.
        '''
        if self.sigma == None and self.epsilon != None:
            print('1')
            eta = (np.power(self.epsilon, (1-self.n)/self.n)*
                   np.exp((self.Q+self.P*self.V)/(self.n*self.R*self.T))/
                   np.power(self.A*self.d**(-self.m) * self.Coh**self.r, 1/self.n)/2)
        elif self.sigma != None and self.epsilon == None:
            print('2')
            eta = (np.power(self.sigma, (1-self.n))*
                   np.exp((self.Q+self.P*self.V)/(self.R*self.T))/
                   (2*self.A)/
                   self.d**(-self.m)/
                   self.Coh**self.r)

        return eta

    def GetSigma(self):
        '''
        Calculate 
        '''
        if self.epsilon != None:
            sigma = (self.epsilon/
                       self.A/
                       np.power(self.d,-self.m)/
                       np.power(self.Coh, self.r)/
                       np.exp(-(self.Q+self.P*self.V)/(self.R*self.T)))
            sigma = np.power(sigma, 1/self.n)
        else:
            sigma = None

        return sigma
    
    @staticmethod
    def plot_T_eta(T, eta):
        '''
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        plt.plot(eta, T-273)
        plt.xlabel('Viscosity (Pas)')
        plt.ylabel('Temperature')
        ax = plt.gca()
        ax.invert_yaxis()
        ax.set_xscale('log')
        plt.show()
        
    @staticmethod
    def plot_T_stress(T, stress):
        '''
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        plt.plot(stress, T-273)
        plt.xlabel('Stress (MPa)')
        plt.ylabel('Temperature')
        ax = plt.gca()
        ax.invert_yaxis()
        plt.show()