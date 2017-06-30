import pylab
from scipy import stats

V_1 = pylab.loadtxt("../../MT/laplace/tol_0_orig_240_27",skiprows=1)
V_1_16d = pylab.loadtxt("tol_0_27_16d",skiprows=1)
V_1_16 = pylab.loadtxt("tol_0_27_16",skiprows=1)
V_1_32 = pylab.loadtxt("tol_0_27_32",skiprows=1)

fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',label='V_1')
ax1.set_ylabel("relative residual norm")
ax1.set_xlabel("#iterations")
ax1.set_xlim([0,30])
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_original.pdf')
ax1.semilogy(V_1_16[:,0],V_1_16[:,1],color='g',label='V_1_16')
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_16.pdf')
ax1.semilogy(V_1_32[:,0],V_1_32[:,1],color='k',label='V_1_32')
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_32.pdf')
ax1.semilogy(V_1_16d[:,0],V_1_16d[:,1],color='b',label='V_1_16d')
pylab.legend(loc=1)

fig.tight_layout()
pylab.savefig('convergence_27.pdf')
pylab.clf()
