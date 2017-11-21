import sys, platform, os
from matplotlib import pyplot as plt
import numpy as np
print('Using CAMB installed at '+ os.path.realpath(os.path.join(os.getcwd(),'..')))
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import camb
from camb import model, initialpower

#You can also directly access some lower level quantities, for example the CMB transfer functions:
pars = camb.CAMBparams()
pars.set_accuracy(lSampleBoost=51., lAccuracyBoost=1.0, AccuracyBoost = 1.)
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122, dscalarAmp=0.2, dscalarPure=True)
data = camb.get_transfer_functions(pars)
transfer = data.get_cmb_transfer_data()
pars.set_for_lmax(2500, lens_potential_accuracy=0)
pars.InitPower.set_params(ns=0.96, r=0)
print 'Number of sources (T, E, phi..): %s; number of ell: %s; number of k: %s '%tuple(transfer.delta_p_l_k.shape)

#Getting the CLs
results = camb.get_results(pars)
powers =results.get_cmb_power_spectra(pars)
totCL=powers['total']
unlensedCL=powers['unlensed_scalar']
print totCL.shape

lplot = 3
#Horizon size at recombination is approx 1/270 Mpc^-1 which gives a k ~0.0037 Mpc^-1
ksub= 1250 #Has transfer.q[1250]    

#######Saving the growing mode (i.e for different accuracies) for all ells and all ks (only use for new accuracies or cosmo params!!!)##########

#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_Temp.txt', transfer.delta_p_l_k[0,:,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_Pol.txt', transfer.delta_p_l_k[1,:,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_TP.txt', transfer.delta_p_l_k[2,:,:])

###############################################################################################################################################

#Getting the amplitude ratio from background transfers compared to transfers for decaying mode

Dbl_T = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_Temp.txt')
Dbl_E = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_Pol.txt')
Dbl_TE = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_allells_TP.txt')

DAmpl_T = np.zeros(transfer.l.size)
DAmpl_E = np.zeros(transfer.l.size)
DAmpl_TE = np.zeros(transfer.l.size)

#Finding the renormalization function. 

for i in range(0, np.size(transfer.l)):
    DAmpl_T[i] = (np.mean(abs((Dbl_T[i,ksub:np.size(transfer.q)]))))/np.mean(abs(transfer.delta_p_l_k[0,i,ksub:np.size(transfer.q)]))
    DAmpl_E[i] = (np.mean(abs((Dbl_E[i,ksub:np.size(transfer.q)]))))/np.mean(abs(transfer.delta_p_l_k[1,i,ksub:np.size(transfer.q)]))
    DAmpl_TE[i] = (np.mean(abs((Dbl_TE[i,ksub:np.size(transfer.q)]))))/np.mean(abs(transfer.delta_p_l_k[2,i,ksub:np.size(transfer.q)]))

np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_T.txt', DAmpl_T)
np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_E.txt', DAmpl_E)
np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_TE.txt', DAmpl_TE)

#Making plots of current CAMB transfers

plt.semilogx(transfer.l, DAmpl_T)

plt.show()


    
    
    
