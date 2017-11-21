import sys, platform, os
from matplotlib import pyplot as plt
import numpy as np
print('Using CAMB installed at '+ os.path.realpath(os.path.join(os.getcwd(),'..')))
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import camb
from camb import model, initialpower

pars = camb.set_params(H0=67.5, ombh2=0.022, omch2=0.122, As=2e-9, ns=0.95, dscalarAmp=0.0, dscalarPure=True)
data= camb.get_background(pars)


#z = np.linspace(10**2,10**8,10**5)
z = np.linspace(1100,10**5,10**5)

def plot_ev(ev, k):
    plt.figure(figsize=(8,6))
    plt.semilogx(z,ev[:,0])
    plt.semilogx(z,ev[:,1])
    plt.semilogx(z,ev[:,2])
    plt.semilogx(z,ev[:,3])
    plt.title(r'$k= %s/\rm{Mpc}$'%k)
    plt.xlabel(r'$z$');
    plt.legend([r'$\Delta_c$', r'$\Delta_\gamma$', r'$\Delta_b$', r'$\Delta_\nu$'], loc = 'upper right');
    plt.show()
k=0.2
plot_ev(data.get_redshift_evolution(k, z, ['delta_cdm','delta_photon', 'delta_baryon', 'delta_nu']),k)
