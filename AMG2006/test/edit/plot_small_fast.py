import pylab
from scipy import stats

V_1 = pylab.loadtxt("tol_0_V_small",skiprows=1)
V_1_fast = pylab.loadtxt("tol_0_V_small_fast",skiprows=1)
V_1_fast2 = pylab.loadtxt("tol_0_V_small_fast2",skiprows=1)
V_1_fast3 = pylab.loadtxt("tol_0_V_small_fast3",skiprows=1)
V_1_fast4 = pylab.loadtxt("tol_0_V_small_fast4",skiprows=1)


fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',label='V_1')
ax1.semilogy(V_1_fast[:,0],V_1_fast[:,1],color='g',linestyle='-',label='V_1_fast')
ax1.semilogy(V_1_fast2[:,0],V_1_fast2[:,1],color='g',linestyle='--',label='V_1_fast2')
ax1.semilogy(V_1_fast3[:,0],V_1_fast3[:,1],color='g',linestyle='-.',label='V_1_fast3')
ax1.semilogy(V_1_fast4[:,0],V_1_fast4[:,1],color='g',linestyle=':',label='V_1_fast4')
pylab.legend(loc=1)
ax1.set_ylabel("relative residual norm",fontsize=20)
ax1.set_xlim([0,100])
ax1.set_xlabel("#cycles",fontsize=20)

fig.tight_layout()
pylab.savefig('convergence_fast_small_norm.pdf')
pylab.clf()

fig, ax1 = pylab.subplots()
#ax1.scatter(V_1[:,0],V_1[:,2],color='r',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1[:,0],V_1[:,2])
ax1.plot(V_1[:,0],slope*V_1[:,0]+intercept,color='r',linestyle='-')
print slope,intercept
#ax1.scatter(V_1_fast[:,0],V_1_fast[:,2],color='g',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast[:,0],V_1_fast[:,2])
ax1.plot(V_1_fast[:,0],slope*V_1_fast[:,0]+intercept,color='g',linestyle='-')
print slope,intercept
#ax1.scatter(V_1_fast2[:,0],V_1_fast2[:,2],color='b',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast2[:,0],V_1_fast2[:,2])
ax1.plot(V_1_fast2[:,0],slope*V_1_fast2[:,0]+intercept,color='g',linestyle='--')
print slope,intercept
#ax1.scatter(V_1_fast3[:,0],V_1_fast3[:,2],color='y',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast3[:,0],V_1_fast3[:,2])
ax1.plot(V_1_fast3[:,0],slope*V_1_fast3[:,0]+intercept,color='g',linestyle='-.')
print slope,intercept
#ax1.scatter(V_1_fast4[:,0],V_1_fast4[:,2],color='k',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast4[:,0],V_1_fast4[:,2])
ax1.plot(V_1_fast4[:,0],slope*V_1_fast4[:,0]+intercept,color='g',linestyle=':')
print slope,intercept
ax1.set_ylabel("time (s)",fontsize=20)
ax1.set_ylim([0,2])
ax1.set_xlim([0,100])
ax1.set_xlabel("#cycles",fontsize=20)

fig.tight_layout()
pylab.savefig('convergence_fast_small_time.pdf')
pylab.clf()



time_V_1 = pylab.loadtxt("mi_inf_V_small",skiprows=1)
time_V_1_fast = pylab.loadtxt("mi_inf_V_small_fast",skiprows=1)
time_V_1_fast2 = pylab.loadtxt("mi_inf_V_small_fast2",skiprows=1)
time_V_1_fast3 = pylab.loadtxt("mi_inf_V_small_fast3",skiprows=1)
time_V_1_fast4 = pylab.loadtxt("mi_inf_V_small_fast4",skiprows=1)

pylab.semilogx(time_V_1[:,0],time_V_1[:,2],color='r',label='V_1')
pylab.semilogx(time_V_1_fast[:,0],time_V_1_fast[:,2],color='g',label='V_1_fast')
pylab.semilogx(time_V_1_fast2[:,0],time_V_1_fast2[:,2],color='g',linestyle='--',label='V_1_fast2')
pylab.semilogx(time_V_1_fast3[:,0],time_V_1_fast3[:,2],color='g',linestyle='-.',label='V_1_fast3')
pylab.semilogx(time_V_1_fast4[:,0],time_V_1_fast4[:,2],color='g',linestyle=':',label='V_1_fast4')
pylab.xlabel("relative residual norm",fontsize=20)
pylab.ylabel("time (s)",fontsize=20)
pylab.gca().invert_xaxis()
pylab.legend()
pylab.savefig("time_convergence_fast_small.pdf")

