import numpy
from lmfit import Model

def gaussian(x, a, alpha, beta,c):

    u = x[:, 0]
    v = x[:, 1]
    return (1.0*a*u**alpha/v**beta+c)

data = numpy.empty((12,3))
x = numpy.arange(1,3,1)
y = numpy.array([2**i for i in range(0,6)])
xx, yy = numpy.meshgrid(x, y)
data[:,0] = xx.flatten()
data[:,1] = yy.flatten()
print data[:,0:2]
data[:, 2]= numpy.array([2.1853,  2.6874, 1.3912,  1.6476, 0.8544,  0.9943, 0.5393, 0.6935, 0.3255, 0.3802, 0.2542, 0.2815]) #HGSS
#data[:,2] = numpy.array([1.3731,1.6986,0.9028,1.1481,0.593,0.7015,0.3762,0.5316,0.2447,0.2681,0.2032,0.2362]) #jacobi

print 'xx\n', xx
print 'yy\n',yy
print 'data to be fit\n', data[:, 2]

a = 1
alpha = 1
beta = 1
c = 0
gmod = Model(gaussian)

gmod.set_param_hint('a', value=a, min=0, max=10)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=5)
gmod.set_param_hint('beta', value=beta, min=0.1, max=1)
gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[:, 2], x=data[:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
print result.best_values
print result.best_fit
