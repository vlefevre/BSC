import pylab
from scipy import stats

font = {'family' : 'normal',
        'size'   : 15}

pylab.rc('font', **font)

V_1 = pylab.loadtxt("../../MT/laplace/tol_0_orig_240_27",skiprows=1)
V_1_16d = pylab.loadtxt("tol_0_27_16d",skiprows=1)
V_1_16 = pylab.loadtxt("tol_0_27_16",skiprows=1)
V_1_32 = pylab.loadtxt("tol_0_27_32",skiprows=1)

fig, ax1 = pylab.subplots()
ax1.semilogy(V_1[:,0],V_1[:,1],color='r',linewidth=2,label='V_1')
ax1.set_ylabel("relative residual norm",fontsize=20)
ax1.set_xlabel("#cycles",fontsize=20)
ax1.set_xlim([0,30])
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_original.pdf')
ax1.semilogy(V_1_16[:,0],V_1_16[:,1],color='r',linestyle='--',label='V_1_16')
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_16.pdf')
ax1.semilogy(V_1_32[:,0],V_1_32[:,1],color='r',linestyle=':',label='V_1_32')
pylab.legend(loc=1)
fig.tight_layout()
pylab.savefig('convergence_27_32.pdf')
ax1.semilogy(V_1_16d[:,0],V_1_16d[:,1],color='r',linestyle='-',label='V_1_16d')
pylab.legend(loc=1)

fig.tight_layout()
pylab.savefig('convergence_27.pdf')
pylab.clf()
