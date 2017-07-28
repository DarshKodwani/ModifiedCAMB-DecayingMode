import sys, platform, os
from matplotlib import pyplot as plt
import numpy as np
print('Using CAMB installed at '+ os.path.realpath(os.path.join(os.getcwd(),'..')))
sys.path.insert(0,os.path.realpath(os.path.join(os.getcwd(),'..')))
import camb
from camb import model, initialpower

#You can also directly access some lower level quantities, for example the CMB transfer functions:
pars = camb.CAMBparams()
pars.set_accuracy(lSampleBoost=1., lAccuracyBoost=1.0, AccuracyBoost = 1.)
pars.set_cosmology(H0=67.5, ombh2=0.022, omch2=0.122)
data = camb.get_transfer_functions(pars)
transfer = data.get_cmb_transfer_data()
print 'Number of sources (T, E, phi..): %s; number of ell: %s; number of k: %s '%tuple(transfer.delta_p_l_k.shape)


#Getting the amplitude ratio from background transfers compared to transfers for decaying mode
Dbl_T = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/background_transfer_T.txt')
Dbl_E = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/background_transfer_E.txt')
Dbl_TE = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/background_transfer_TE.txt')

#Computing Dl (plotting transfer functions as a function of l)


DAmpl_T = np.zeros((transfer.l.size, transfer.q.size))
DAmpl_E = np.zeros((transfer.l.size, transfer.q.size))
DAmpl_TE = np.zeros((transfer.l.size, transfer.q.size))

for i in range(0, np.size(transfer.l)):
    DAmpl_T[i,:] = np.sqrt((transfer.delta_p_l_k[0,i,:])**2/(Dbl_T[i,:])**2)
    DAmpl_E[i,:] = transfer.delta_p_l_k[1,i,:]/Dbl_E[i,:]
    DAmpl_TE[i,:] = transfer.delta_p_l_k[2,i,:]/Dbl_TE[i,:]

np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_T.txt', DAmpl_T)
np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_E.txt', DAmpl_E)
np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/Renorm_Deq1_TE.txt', DAmpl_TE)

lplot = 3
kmax=2736
ksub= 1500

meanDl = np.zeros(np.size(range(ksub, np.size(transfer.q))))

for i in range(0, np.size(meanDl)):
    meanDl[i] = np.average(DAmpl_T[:,transfer.q[i+ksub]])
    
#plt.semilogx(transfer.q, DAmpl_T[lplot,:])
#plt.semilogx(transfer.l, DAmpl_T[:,kmax])

#plt.plot(transfer.l, DAmpl_T[:,1500])


print transfer.l[lplot]
#plt.set_title(r'$\ell = %s$'%transfer.l[lpot])

#Plotting transfer functions for k

#Background (growing mode) transfer for l=2,3,4,5,10 

#Saving the growing mode (i.e for different accuracies)

#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l2.txt', transfer.delta_p_l_k[0,0,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l3.txt', transfer.delta_p_l_k[0,1,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l4.txt', transfer.delta_p_l_k[0,2,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l5.txt', transfer.delta_p_l_k[0,3,:])
#np.savetxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l10.txt', transfer.delta_p_l_k[0,8,:])

#loading the growing mode
grow_l2 = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l2.txt')
grow_l3 = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l3.txt')
grow_l4 = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l4.txt')
grow_l5 = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l5.txt')
grow_l10 = np.loadtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/grow_trnsf_l10.txt')

#Making plots of background (growing mode)

#plt.semilogx(transfer.q, grow_l2)
#plt.semilogx(transfer.q, grow_l3)
#plt.semilogx(transfer.q, grow_l4)
#plt.semilogx(transfer.q, grow_l5)
#plt.semilogx(transfer.q, grow_l10)

#Making plots of current CAMB transfers

plt.semilogx(transfer.q, transfer.delta_p_l_k[0,0,:])
plt.semilogx(transfer.q, transfer.delta_p_l_k[0,1,:])
plt.semilogx(transfer.q, transfer.delta_p_l_k[0,2,:])
plt.semilogx(transfer.q, transfer.delta_p_l_k[0,3,:])
plt.semilogx(transfer.q, transfer.delta_p_l_k[0,8,:])

plt.legend(['l=2d','l=3d', 'l=4d', 'l=5d', 'l=10d'  ], loc = 'upper left');

plt.show()

