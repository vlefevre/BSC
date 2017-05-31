import pylab
from scipy import stats

V_1 = pylab.loadtxt("tol_0_original_5",skiprows=1)
V_1_fast4 = pylab.loadtxt("tol_0_fast4_5",skiprows=1)
V_1_up = pylab.loadtxt("tol_0_up_5",skiprows=1)

fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',label='V_1')
ax1.semilogy(V_1_fast4[:,0],V_1_fast4[:,1],color='g',label='V_1_fast4')
ax1.semilogy(V_1_up[:,0],V_1_up[:,1],color='b',label='V_1_up')
pylab.legend(loc=1)
ax1.set_ylabel("relative residual norm")
ax2 = ax1.twinx()
ax2.scatter(V_1[:,0],V_1[:,2],color='r',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1[:,0],V_1[:,2])
ax2.plot(V_1[:,0],slope*V_1[:,0]+intercept,color='r',linestyle='--')
print slope,intercept
ax2.scatter(V_1_fast4[:,0],V_1_fast4[:,2],color='g',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_fast4[:,0],V_1_fast4[:,2])
ax2.plot(V_1_fast4[:,0],slope*V_1_fast4[:,0]+intercept,color='g',linestyle='--')
print slope,intercept
ax2.scatter(V_1_up[:,0],V_1_up[:,2],color='b',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1_up[:,0],V_1_up[:,2])
ax2.plot(V_1_up[:,0],slope*V_1_up[:,0]+intercept,color='b',linestyle='--')
print slope,intercept
ax2.set_ylabel("time")
ax1.set_xlabel("#iterations")
ax1.set_xlim([0,80])

fig.tight_layout()
pylab.savefig('convergence_fast.pdf')
pylab.clf()


pylab.semilogx(V_1[:,1],V_1[:,2],color='r',label='V_1')
pylab.semilogx(V_1_fast4[:,1],V_1_fast4[:,2],color='g',label='V_1_fast4')
pylab.semilogx(V_1_up[:,1],V_1_up[:,2],color='b',label='V_1_up')
pylab.ylim([0,0.3])
pylab.xlabel("relative residual norm")
pylab.ylabel("time")
pylab.legend()
pylab.savefig("time_convergence_fast.pdf")

