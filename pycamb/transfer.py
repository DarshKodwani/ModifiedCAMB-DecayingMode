import sys, platform, os
from matplotlib import pyplot as plt
import numpy as np
import camb
from camb import model, initialpower

#GENERATING TRANSFERS

pars=camb.CAMBparams()
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, mnu=0.06, omk=0, tau=0.06,dscalarAmp=0., dscalarPure=True)
pars.InitPower.set_params(ns=0.965, r=0)
pars.set_for_lmax(2500, lens_potential_accuracy=0);
pars.set_accuracy(AccuracyBoost=1.0)
results = camb.get_results(pars)
powers =results.get_cmb_power_spectra(pars)
data = camb.get_transfer_functions(pars)
transfer = data.get_cmb_transfer_data()

plt.semilogx(transfer.q,transfer.delta_p_l_k[0,5,:],'r',label="Decay l=100")

# np.savetxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l2.txt", transfer.delta_p_l_k[0,2,:])
# np.savetxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l5.txt", transfer.delta_p_l_k[0,5,:])
# np.savetxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l10.txt", transfer.delta_p_l_k[0,10,:])
# np.savetxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l50.txt", transfer.delta_p_l_k[0,50,:])

#MAKE PLOTS

#dTl2=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l2.txt",unpack=True)
#dTl5=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l5.txt",unpack=True)
#dTl10=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l10.txt",unpack=True)
#dTl50=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/decay_trnsf_l50.txt",unpack=True)
#
#gTl2=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l2.txt",unpack=True)
#gTl5=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l5.txt",unpack=True)
#gTl10=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l10.txt",unpack=True)
#gTl50=np.loadtxt("/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l50.txt",unpack=True)

#plt.semilogx(transfer.q,dTl2,'r',label="Decay l=2")
#plt.semilogx(transfer.q,dTl5,'r',label="Decay l=7")
#plt.semilogx(transfer.q,dTl10,'r',label="Decay l=15")
#plt.semilogx(transfer.q,dTl50,'r',label="Decay l=1550")

#lt.semilogx(transfer.q,gTl2,'b',label="Grow l=2")
#plt.semilogx(transfer.q,gTl5,'b',label="Grow l=7")
#plt.semilogx(transfer.q,gTl10,'b',label="Grow l=15")
#plt.semilogx(transfer.q,gTl50,'b',label="Grow l=1550")

plt.legend()
plt.show()
