import pylab

d8 = pylab.loadtxt("tol_0_8",skiprows=1)
d23 = pylab.loadtxt("tol_0_23",skiprows=1)
d16 = pylab.loadtxt("tol_0_16",skiprows=1)
d32 = pylab.loadtxt("tol_0_32",skiprows=1)
d64 = pylab.loadtxt("tol_0_64",skiprows=1)

pylab.semilogy(d8[:,0],d8[:,1],color='r',label='8 bits')
pylab.semilogy(d16[:,0],d16[:,1],color='g',label='16 bits')
pylab.semilogy(d23[:,0],d23[:,1],color='y',label='24 bits (float)')
pylab.semilogy(d32[:,0],d32[:,1],color='b',label='32 bits')
pylab.semilogy(d64[:,0],d64[:,1],color='k',label='64 bits')
pylab.xlabel("#iterations")
pylab.ylabel("relative residual norm")
pylab.legend()
pylab.savefig('bits_convergence.pdf')
