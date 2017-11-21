import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import *
from pylab import *

#ax1 = subplot(2,1,1)
#ax2 = subplot(2,1,2)

######################plotting current camb Cls

ax1 = subplot(1,1,1)

#Converting to muK^2 units: 
muK = 7.46*10**(12)

temp = np.genfromtxt('/Users/darshkodwani/Documents/Darsh/Research/Sound_modes/ModifiedCAMB-DecayingMode/decay_out/decay_scalCls.dat')
tempclass = muK*np.genfromtxt('/Users/darshkodwani/Desktop/class_decay/output/decaycls_addcs.dat')
xdata = temp[:,0]
ytemp = 2*temp[:,1]
ytempclass = tempclass[:,1]

ax1.loglog(xdata,ytemp, label="CAMB decay n=2")
ax1.loglog(xdata,ytempclass, label="CLASS decay n=2")

ax1.set_xlabel("$l$")
ax1.set_ylabel("$C^{TT}_l l(l+1)$")
plt.legend()

show()
