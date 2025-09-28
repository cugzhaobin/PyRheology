import numpy as np
import logging

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
            A     = pre-exponential factor, 1/(MPa^(-n)*s)
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


    def get_strain_rate(self):
        '''
        Compute strain rate ε given stress σ.
        '''
        if self.sigma is None:
            logging.warning("σ (stress) not set. Cannot compute ε.")
            return None

        strain_rate = (self.A * 
                       self.d**(-self.m) *
                       self.Coh**self.r *
                       self.sigma**self.n *
                       np.exp(-(self.Q+self.P*self.V)/(self.R*self.T)))
        return strain_rate

    def get_viscosity(self):
        '''
        Calculate viscosity.
        '''
        if self.d == 0:
            self.d = 1.0
        if self.Coh == 0:
            self.Coh = 1.0
        print(self.Coh, self.d)
            
        # equation (7) of Freed et al. 2012
        if self.sigma is None and self.epsilon is not None:
            eta = (self.epsilon ** ((1-self.n)/self.n) *
                   np.exp((self.Q+self.P*self.V)/(self.n*self.R*self.T)) /
                   (self.A*self.d**(-self.m) * self.Coh**self.r)**(1/self.n)/2)
            
        # equation (6) of Freed et al. 2012
        elif self.sigma is not None and self.epsilon is None:
            eta = (np.power(self.sigma, (1-self.n)) *
                   np.exp((self.Q+self.P*self.V)/(self.R*self.T)) /
                   (2 * self.A * self.d**(-self.m)* self.Coh**self.r))
        else:
            logging.warning("Need either σ or ε to compute viscosity.")
            eta = None
        return eta*1e6

    def get_stress(self):
        '''
        Calculate stress σ given strain rate ε.
        '''
        if self.epsilon is None:
            logging.warning("ε (strain rate) not set. Cannot compute σ.")
            return None
        
        sigma = (self.epsilon /
                 self.A /
                 self.d**(-self.m) /
                 self.Coh**self.r /
                 np.exp(-(self.Q+self.P*self.V)/(self.R*self.T)))
        sigma = np.power(sigma, 1/self.n)
        return sigma
    
    @staticmethod
    def plot_tempeature_viscosity(T, eta):
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
    def plot_depth_viscosity(depth, eta):
        '''
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        plt.plot(eta, depth)
        plt.xlabel('Viscosity (Pas)')
        plt.ylabel('Depth (km)')
        ax = plt.gca()
        ax.invert_yaxis()
        ax.set_xscale('log')
        plt.show()
        
    @staticmethod
    def plot_depth_stress(depth, stress):
        '''
        '''
        import numpy as np
        import matplotlib.pyplot as plt
        plt.plot(stress, depth)
        plt.xlabel('Stress (MPa)')
        plt.ylabel('Depth (km)')
        ax = plt.gca()
        ax.invert_yaxis()
        plt.show()
