import numpy
from lmfit import Model

def gaussian(x, a, alpha, beta):

    u = x[:, 0]
    v = x[:, 1]
    return (1.0*a*u**alpha/v**beta)

data = numpy.empty((12,3))
x = numpy.arange(1,3,1)
y = numpy.array([2**i for i in range(0,6)])
xx, yy = numpy.meshgrid(x, y)
data[:,0] = xx.flatten()
data[:,1] = yy.flatten()
print data[:,0:2]
#data[:, 2]= numpy.array([2.1853,  2.6874, 1.3912,  1.6476, 0.8544,  0.9943, 0.5393, 0.6935, 0.3255, 0.3802, 0.2542, 0.2815]) #HGSS

#data[:,2] = numpy.array([1.3731,1.6986,0.9028,1.1481,0.593,0.7015,0.3762,0.5316,0.2447,0.2681,0.2032,0.2362]) #jacobi

#data[:,2] = numpy.array([1.9023, , 1.2943, , 0.8383, , 0.5470, , 0.2879, , 0.1966, ]) #jacobi-up

#data[:,2] = numpy.array([, 3.1196, , 2.1218, , 1.4808, , 1.0014, , 0.6630, , 0.5241]) #HGSS-up

#data[:,2] = numpy.array([3.1845,3.7667,1.8628,2.4115,1.1137,1.5876,0.6579,1.0211,0.2106,0.4707,0.1995,0.2526]) #laplace
#data[:,2] = numpy.array([3.9022,4.7051,2.3652,3.1020,1.5438,2.2007,1.0032,1.5072]) #27pt
#data[:,2] = numpy.array([]) #jumps

data[:,2] = numpy.array([2.1393,2.6016,1.3061,1.7421,0.7973,1.1603,0.4878,0.7630,0.2515,0.3621,0.1433,0.1936]) #laplace-up
#data[:,2] = numpy.array([]) #27pt-up
#data[:,2] = numpy.array([]) #jumps-up

print 'xx\n', xx
print 'yy\n',yy
print 'data to be fit\n', data[:, 2]

a = 1
alpha = 0.3
beta = 1
#c = 0
gmod = Model(gaussian)

gmod.set_param_hint('a', value=a, min=0, max=10)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=0.5)
gmod.set_param_hint('beta', value=beta, min=0.1, max=1)
#gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[:, 2], x=data[:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
print result.best_values
print result.best_fit
