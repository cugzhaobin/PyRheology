import numpy as np
def byerlee(did, branch):
    if branch == 1:
        tag = 'ByerLeeLP'
        C   = 0
        mu  = 0.85
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 2:
        tag = 'ByerLeeHP'
        C   = 50e6
        mu  = 0.6
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 3:
        tag = 'LizarditeReiner'
        C   = 0
        mu  = 0.25
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 4:
        tag = 'LizarditeAmiguet'
        C   = 100e6
        mu  = 0.0
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)  
    
    if branch == 5:
        tag = '300MPa'
        C   = 300e6
        mu  = 0.0
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 6:
        tag = '100MPa'
        C   = 100e6
        mu  = 0.0
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 7:
        tag = '30MPa'
        C   = 30e6
        mu  = 0.0
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
        
    if branch == 8:
        tag = '10MPa'
        C   = 10e6
        mu  = 0.0
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
        
    if branch == 9:
        tag = 'Icefriction'
        C   = 8.3e6
        mu  = 0.2
        Ci  = C/np.sqrt(1+mu**2)
        fi  = mu/np.sqrt(1+mu**2)
    if branch == 0:
        Ci = 1
        fi = 1
        
        
    if did == 1:
        S = Ci/(1-fi)
        f = fi/(1-fi)
        
    if did == 2:
        S = Ci/(1+fi)
        f = fi/(1+fi)
    
    if did == 3:
        S = Ci
        f = fi
        
    return S, f


S,f=byerlee(3,2)
print(S,f)
