import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
from math import *
from pylab import *

#ax1 = subplot(2,1,1)
#ax2 = subplot(2,1,2)

######################plotting current camb Cls

ax1 = subplot(1,1,1)

temp = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls.dat')
noom = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/no_omega.dat')
xdata = temp[:,0]
ytemp = temp[:,1]
noom_y = noom[:,1]

ax1.loglog(xdata,ytemp)
ax1.loglog(xdata, noom_y)
#ax1.plot(xdata,ytemp)
#ax1.plot(xdata, noom_y)

ax1.set_xlabel("$l$")
ax1.set_ylabel("$C^{TT}_l l(l+1)$")


##################Only decaying and growing

#ax1 = subplot(1,1,1)
#decay = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_decay.dat')
#grow = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-Jan2017-2/test_scalCls.dat')

#xdata = decay[:,0]
#decaydata_Temp = 0.25*decay[:,1]
#growdata_Temp = grow[:,1]

#ax1.loglog(xdata,decaydata_Temp)
#ax1.loglog(xdata,growdata_Temp)
#ax1.legend(['Decaying mode','Growing mode'], loc='upper right')
#ax1.set_xlabel("$l$")
#ax1.set_ylabel("$C^{TE}_l l(l+1)$")




################################################TT
#
#ax1 = subplot(1,1,1)
#
#d = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_01.dat')
#d1 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_05.dat')
#d2 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_1.dat')
#d3 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_2.dat')
#d4 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_scalCls_5.dat')
#d5 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-Jan2017-2/test_scalCls.dat')
#d6 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/full_decaying.dat')
#
#xdata = d[:,0]
#adydata = d[:,1]
#ad1ydata = d1[:,1]
#ad2ydata = d2[:,1]
#ad3ydata = d3[:,1]
#ad4ydata = d4[:,1]
#ad5ydata = d5[:,1]
#ad6ydata = d6[:,1]
#
#
#dy = adydata - ad5ydata
#
#ax1.plot(xdata,adydata)
#ax1.plot(xdata,ad1ydata)
#ax1.semilogx(xdata,adydata)
#ax1.semilogx(xdata,ad1ydata)
#
#ax1.loglog(xdata,adydata)
#ax1.loglog(xdata,ad1ydata)
#ax1.loglog(xdata,ad2ydata)
#ax1.loglog(xdata,ad3ydata)
#ax1.loglog(xdata,ad4ydata)
#ax1.loglog(xdata,ad5ydata)
#ax1.loglog(xdata,ad6ydata)
#ax1.legend(['D = $1\%$','D = $5\%$', 'D = $10\%$', 'D = $20\%$', 'D=$50\%$', 'No decaying mode'], loc='upper right')
#ax1.set_xlabel("$l$")
#ax1.set_ylabel("$C^{TT}_l l(l+1)$")


#ax2.plot(xdata,dy)
##ax2.axis([0, 2400, -400, 100])
##ax2.loglog(xdata,dy)
#ax2.legend(loc = 'upper right', prop={'size':10}, borderaxespad=0.)
#ax2.set_xlabel("$l$")
#ax2.set_ylabel("$\Delta C_l l(l+1)$")

#show()


############################################EE

#ax1 = subplot(1,1,1)
#
#xdata = d[:,0]
#adydata = d[:,2]
#ad1ydata = d1[:,2]
#ad2ydata = d2[:,2]
#ad3ydata = d3[:,2]
#ad4ydata = d4[:,2]
#ad5ydata = d5[:,2]
#ad6ydata = d6[:,2]
#
#
#dy = adydata - ad5ydata

#ax1.plot(xdata,adydata)
#ax1.plot(xdata,ad1ydata)
#ax1.semilogx(xdata,adydata)
#ax1.semilogx(xdata,ad1ydata)
#
#ax1.loglog(xdata,adydata)
#ax1.loglog(xdata,ad1ydata)
#ax1.loglog(xdata,ad2ydata)
#ax1.loglog(xdata,ad3ydata)
#ax1.loglog(xdata,ad4ydata)
#ax1.loglog(xdata,ad5ydata)
#ax1.loglog(xdata,ad6ydata)
#ax1.legend(['D = $1\%$','D = $5\%$', 'D = $10\%$', 'D = $20\%$', 'D=$50\%$', 'No decaying mode'], loc='upper right')
#ax1.set_xlabel("$l$")
#ax1.set_ylabel("$C^{EE}_l l(l+1)$")


#ax2.plot(xdata,dy)
##ax2.axis([0, 2400, -400, 100])
##ax2.loglog(xdata,dy)
#ax2.legend(loc = 'upper right', prop={'size':10}, borderaxespad=0.)
#ax2.set_xlabel("$l$")
#ax2.set_ylabel("$\Delta C_l l(l+1)$")

#show()

#################################TE

#ax1 = subplot(1,1,1)

#xdata = d[:,0]
#adydata = d[:,3]
#ad1ydata = d1[:,3]
#ad2ydata = d2[:,3]
#ad3ydata = d3[:,3]
#ad4ydata = d4[:,3]
#ad5ydata = d5[:,3]
#ad6ydata = d6[:,3]
#
#
#dy = adydata - ad5ydata

#ax1.plot(xdata,adydata)
#ax1.plot(xdata,ad1ydata)
#ax1.semilogx(xdata,adydata)
#ax1.semilogx(xdata,ad1ydata)



#ax1.loglog(xdata,adydata)
#ax1.loglog(xdata,ad1ydata)
#ax1.loglog(xdata,ad2ydata)
#ax1.loglog(xdata,ad3ydata)
#ax1.loglog(xdata,ad4ydata)
#ax1.loglog(xdata,ad5ydata)
#ax1.loglog(xdata,ad6ydata)
#ax1.legend(['D = $1\%$','D = $5\%$', 'D = $10\%$', 'D = $20\%$', 'D=$50\%$', 'No decaying mode'], loc='upper right')
#ax1.set_xlabel("$l$")
#ax1.set_ylabel("$C^{TE}_l l(l+1)$")


#ax2.plot(xdata,dy)
##ax2.axis([0, 2400, -400, 100])
##ax2.loglog(xdata,dy)
#ax2.legend(loc = 'upper right', prop={'size':10}, borderaxespad=0.)
#ax2.set_xlabel("$l$")
#ax2.set_ylabel("$\Delta C_l l(l+1)$")

###########################################BB
#
#ax1 = subplot(1,1,1)
#
#t = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_tensCls_01.dat')
#t1 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_tensCls_05.dat')
#t2 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_tensCls_1.dat')
#t3 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_tensCls_2.dat')
#t4 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-master/test_tensCls_5.dat')
#t5 = np.genfromtxt('/Users/darshkodwani/Downloads/CAMB-Jan2017-2/back_tens.dat')
#
#xdata = t[:,0]
#adydata = t[:,3]
#ad1ydata = t1[:,3]
#ad2ydata = t2[:,3]
#ad3ydata = t3[:,3]
#ad4ydata = t4[:,3]
#ad5ydata = t5[:,3]
#


#dy = adydata - ad5ydata

#ax1.plot(xdata,adydata)
#ax1.plot(xdata,ad1ydata)
#ax1.semilogx(xdata,adydata)
#ax1.semilogx(xdata,ad1ydata)

#ax1.loglog(xdata,adydata)
#ax1.loglog(xdata,ad1ydata)
#ax1.loglog(xdata,ad2ydata)
#ax1.loglog(xdata,ad3ydata)
#ax1.loglog(xdata,ad4ydata)
#ax1.loglog(xdata,ad5ydata)
#ax1.legend(['D = $1\%$','D = $5\%$', 'D = $10\%$', 'D = $20\%$', 'D=$50\%$', 'No decaying mode'], loc='upper right')
#ax1.set_xlabel("$l$")
#ax1.set_ylabel("$C^{BB}_l l(l+1)$")


#ax2.plot(xdata,dy)
##ax2.axis([0, 2400, -400, 100])
##ax2.loglog(xdata,dy)
#ax2.legend(loc = 'upper right', prop={'size':10}, borderaxespad=0.)
#ax2.set_xlabel("$l$")
#ax2.set_ylabel("$\Delta C_l l(l+1)$")

show()
