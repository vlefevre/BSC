import pylab
from scipy import stats

V_1 = pylab.loadtxt("tol_0_V",skiprows=1)
V_1_fast = pylab.loadtxt("tol_0_V_fast",skiprows=1)
V_1_fast3 = pylab.loadtxt("tol_0_V_fast3",skiprows=1)
V_1_fast4 = pylab.loadtxt("tol_0_V_fast4",skiprows=1)


fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',label='V_1')
ax1.semilogy(V_1_fast[:,0],V_1_fast[:,1],color='g',label='V_1_fast')
ax1.semilogy(V_1_fast3[:,0],V_1_fast3[:,1],color='y',label='V_1_fast3')
ax1.semilogy(V_1_fast4[:,0],V_1_fast4[:,1],color='k',label='V_1_fast4')
pylab.legend(loc=1)
ax1.set_ylabel("relative residual norm")
ax2 = ax1.twinx()
ax2.scatter(V_1[:,0],V_1[:,2],color='r',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1[:,0],V_1[:,2])
ax2.plot(V_1[:,0],slope*V_1[:,0]+intercept,color='r',linestyle='--')
print slope,intercept
ax2.scatter(V_1_fast[:,0],V_1_fast[:,2],color='g',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast[:,0],V_1_fast[:,2])
ax2.plot(V_1_fast[:,0],slope*V_1_fast[:,0]+intercept,color='g',linestyle='--')
print slope,intercept
ax2.scatter(V_1_fast3[:,0],V_1_fast3[:,2],color='y',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast3[:,0],V_1_fast3[:,2])
ax2.plot(V_1_fast3[:,0],slope*V_1_fast3[:,0]+intercept,color='y',linestyle='--')
print slope,intercept
ax2.scatter(V_1_fast4[:,0],V_1_fast4[:,2],color='k',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast4[:,0],V_1_fast4[:,2])
ax2.plot(V_1_fast4[:,0],slope*V_1_fast4[:,0]+intercept,color='k',linestyle='--')
print slope,intercept
ax2.set_ylabel("time")
ax2.set_ylim([0,16])
ax1.set_xlim([0,100])
ax1.set_xlabel("#iterations")

fig.tight_layout()
pylab.savefig('convergence_fast.pdf')
pylab.clf()



time_V_1 = pylab.loadtxt("mi_inf_V",skiprows=1)
time_V_1_fast = pylab.loadtxt("mi_inf_V_fast",skiprows=1)
time_V_1_fast3 = pylab.loadtxt("mi_inf_V_fast3",skiprows=1)
time_V_1_fast4 = pylab.loadtxt("mi_inf_V_fast4",skiprows=1)

pylab.semilogx(time_V_1[:,0],time_V_1[:,2],color='r',label='V_1')
pylab.semilogx(time_V_1_fast[:,0],time_V_1_fast[:,2],color='g',label='V_1_fast')
pylab.semilogx(time_V_1_fast3[:,0],time_V_1_fast3[:,2],color='g',linestyle='-.',label='V_1_fast3')
pylab.semilogx(time_V_1_fast4[:,0],time_V_1_fast4[:,2],color='g',linestyle=':',label='V_1_fast4')
pylab.xlabel("tolerance")
pylab.ylabel("time")
pylab.legend()
pylab.savefig("time_convergence_fast.pdf")

