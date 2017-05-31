import pylab
from scipy import stats

V_1 = pylab.loadtxt("tol_0_V",skiprows=1)
V_2 = pylab.loadtxt("tol_0_V_2",skiprows=1)
V_3 = pylab.loadtxt("tol_0_V_3",skiprows=1)
V_10 = pylab.loadtxt("tol_0_V_10",skiprows=1)
W_1 = pylab.loadtxt("tol_0_W",skiprows=1)
W_2 = pylab.loadtxt("tol_0_W_2",skiprows=1)
W_3 = pylab.loadtxt("tol_0_W_3",skiprows=1)
W_10 = pylab.loadtxt("tol_0_W_10",skiprows=1)


fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',label='V_1')
ax1.semilogy(V_2[:,0],V_2[:,1],color='g',label='V_2')
ax1.semilogy(V_3[:,0],V_3[:,1],color='black',label='V_3')
ax1.semilogy(V_10[:,0],V_10[:,1],color='yellow',label='V_10')
ax1.semilogy(W_1[:,0],W_1[:,1],color='b',label='W_1')
ax1.semilogy(W_2[:,0],W_2[:,1],color='cyan',label='W_2')
ax1.semilogy(W_3[:,0],W_3[:,1],color='pink',label='W_3')
ax1.semilogy(W_10[:,0],W_10[:,1],color='gray',label='W_10')
pylab.legend(loc=1)
ax1.set_ylabel("relative residual norm")
ax2 = ax1.twinx()
ax2.scatter(V_1[:,0],V_1[:,2],color='r',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_1[:,0],V_1[:,2])
ax2.plot(V_1[:,0],slope*V_1[:,0]+intercept,color='r',linestyle='--')
print slope,intercept
ax2.scatter(V_2[:,0],V_2[:,2],color='g',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_2[:,0],V_2[:,2])
ax2.plot(V_2[:,0],slope*V_2[:,0]+intercept,color='g',linestyle='--')
print slope,intercept
ax2.scatter(V_3[:,0],V_3[:,2],color='black',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_3[:,0],V_3[:,2])
ax2.plot(V_3[:,0],slope*V_3[:,0]+intercept,color='black',linestyle='--')
print slope,intercept
ax2.scatter(V_10[:,0],V_10[:,2],color='yellow',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(V_10[:,0],V_10[:,2])
ax2.plot(V_10[:,0],slope*V_10[:,0]+intercept,color='yellow',linestyle='--')
print slope,intercept
ax2.scatter(W_1[:,0],W_1[:,2],color='b',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(W_1[:,0],W_1[:,2])
ax2.plot(W_1[:,0],slope*W_1[:,0]+intercept,color='b',linestyle='--')
print slope,intercept
ax2.scatter(W_2[:,0],W_2[:,2],color='cyan',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(W_2[:,0],W_2[:,2])
ax2.plot(W_2[:,0],slope*W_2[:,0]+intercept,color='cyan',linestyle='--')
print slope,intercept
ax2.scatter(W_3[:,0],W_3[:,2],color='pink',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(W_3[:,0],W_3[:,2])
ax2.plot(W_3[:,0],slope*W_3[:,0]+intercept,color='pink',linestyle='--')
print slope,intercept
ax2.scatter(W_10[:,0],W_10[:,2],color='gray',marker='.',s=10,alpha=0.5)
slope, intercept, r_value, p_value, std_err = stats.linregress(W_10[:,0],W_10[:,2])
ax2.plot(W_10[:,0],slope*W_10[:,0]+intercept,color='gray',linestyle='--')
print slope,intercept
ax2.set_ylabel("time")
ax2.set_ylim([0,100])
ax1.set_xlim([0,100])
ax1.set_xlabel("#iterations")

fig.tight_layout()
pylab.savefig('convergence_1.pdf')
pylab.clf()



time_V_1 = pylab.loadtxt("mi_inf_V",skiprows=1)
time_V_2 = pylab.loadtxt("mi_inf_V_2",skiprows=1)
time_V_3 = pylab.loadtxt("mi_inf_V_3",skiprows=1)
time_V_10 = pylab.loadtxt("mi_inf_V_10",skiprows=1)
time_W_1 = pylab.loadtxt("mi_inf_W",skiprows=1)
time_W_2 = pylab.loadtxt("mi_inf_W_2",skiprows=1)
time_W_3 = pylab.loadtxt("mi_inf_W_3",skiprows=1)
time_W_10 = pylab.loadtxt("mi_inf_W_10",skiprows=1)

pylab.semilogx(time_V_1[:,0],time_V_1[:,2],color='r',label='V_1')
pylab.semilogx(time_V_2[:,0],time_V_2[:,2],color='r',linestyle='--',label='V_2')
pylab.semilogx(time_V_3[:,0],time_V_3[:,2],color='r',linestyle='-.',label='V_3')
pylab.semilogx(time_V_10[:,0],time_V_10[:,2],color='r',linestyle=':',label='V_10')
pylab.semilogx(time_W_1[:,0],time_W_1[:,2],color='b',label='W_1')
pylab.semilogx(time_W_2[:,0],time_W_2[:,2],color='b',linestyle='--',label='W_2')
pylab.semilogx(time_W_3[:,0],time_W_3[:,2],color='b',linestyle='-.',label='W_3')
pylab.semilogx(time_W_10[:,0],time_W_10[:,2],color='b',linestyle=':',label='W_10')
pylab.xlabel("tolerance")
pylab.ylabel("time")
pylab.legend()
pylab.savefig("time_convergence.pdf")

