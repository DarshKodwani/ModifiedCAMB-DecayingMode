import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import *
from pylab import *

#ax1 = subplot(2,1,1)
#ax2 = subplot(2,1,2)

######################plotting current camb Cls

ax1 = subplot(1,1,1)

temp = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls.dat')
qmin10 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls10.dat')
qmin20 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls20.dat')
qmin30 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls30.dat')
qmin40 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls40.dat')
#decayonly_nd1 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_ndeq1.dat')
#decayonly_nd2 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_ndeq2.dat')
#growonly_nd1 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/normalgrowingmodecls.dat')
#decayD02n1 = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decaygrow_D02_n1.dat')
xdata = temp[:,0]
ytemp = temp[:,1]
yqmin10 = qmin10[:,1]
yqmin20 = qmin20[:,1]
yqmin30 = qmin30[:,1]
yqmin40 = qmin40[:,1]
#Ydecayonly_nd1 = decayonly_nd1[:,1]
#Ydecayonly_nd2 = decayonly_nd2[:,1]
#Ygrowonly_nd1 = growonly_nd1[:,1]
#YdecayD02n1 = decayD02n1[:,1]
#Combining n=1 growing with n=2 decaying
#gn1dn2 = Ygrowonly_nd1 + Ydecayonly_nd2


ax1.loglog(xdata,ytemp,label='Decaying only n=2')
ax1.loglog(xdata,yqmin10,label='Decaying only n=2, 10qmin')
ax1.loglog(xdata,yqmin20,label='Decaying only n=2, 20qmin')
ax1.loglog(xdata,yqmin30,label='Decaying only n=2, 30qmin')
ax1.loglog(xdata,yqmin40,label='Decaying only n=2, 40qmin')
#ax1.loglog(xdata, Ydecayonly_nd1, label = 'Decaying only n=1')
#ax1.plot(xdata, Ygrowonly_nd1, label = 'Growing only (normal Cls)')
#ax1.loglog(xdata, YdecayD02n1, label = 'Decaying and growing with D=0.2 with n=1')
#ax1.loglog(xdata, Ydecayonly_nd2, label = 'Decaying only n=2')
#ax1.plot(xdata, gn1dn2, label = 'Decaying only n=2 and Growing only with n=1')


ax1.set_xlabel("$l$")
ax1.set_ylabel("$C^{TT}_l l(l+1)$")
plt.legend()

show()
