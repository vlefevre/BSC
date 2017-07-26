import numpy
from lmfit import Model

def gaussian(x, a, alpha, c):

    u = x[:, 0]
    n = x[:, 1]
    return (1.0*a*n**3*u**alpha+c)

data = numpy.empty((40,3))
x = numpy.arange(1,3,1)
y = numpy.array([5*i for i in range(1,21)])
xx, yy = numpy.meshgrid(x, y)
data[:,0] = xx.flatten()
data[:,1] = yy.flatten()
print data[:,0:2]

data[:,2] = numpy.array([0.0038,0.0041,0.0154,0.0165,0.0423,0.0461,0.0941,0.1069,0.1830,0.2038,0.3089,0.3487,0.5040,0.5641,0.7506,0.8606,1.0796,1.2356,1.4908,1.7447,2.0038,2.3330,2.6233,3.0913,3.3105,3.8916,4.1498,4.9213,5.1477,6.0703,6.1977,7.3968,7.4637,8.8413,8.9285,10.6754,10.4677,12.4491,12.3124,14.7764]) #laplace

print 'xx\n', xx
print 'yy\n',yy
print 'data to be fit\n', data[:, 2]

a = 1
alpha = 1 
c = 0
gmod = Model(gaussian)

gmod.set_param_hint('a', value=a, min=0, max=0.001)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=1)
gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[10:, 2], x=data[10:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
print result.best_values
print result.best_fit
