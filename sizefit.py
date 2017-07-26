import numpy
from lmfit import Model

def gaussian(x, a, alpha, c):

    u = x[:, 0]
    n = x[:, 1]
    return (1.0*a*n**3*u**alpha+c)

data = numpy.empty((40,3))
x = numpy.arange(1,3,1)
y = numpy.array([5*i for i in range(1,21)])
#y = numpy.array([8*i for i in range(1,16)])
xx, yy = numpy.meshgrid(x, y)
data[:,0] = xx.flatten()
data[:,1] = yy.flatten()

#data[:,2] = numpy.array([0.0038,0.0041,0.0154,0.0165,0.0423,0.0461,0.0941,0.1069,0.1830,0.2038,0.3089,0.3487,0.5040,0.5641,0.7506,0.8606,1.0796,1.2356,1.4908,1.7447,2.0038,2.3330,2.6233,3.0913,3.3105,3.8916,4.1498,4.9213,5.1477,6.0703,6.1977,7.3968,7.4637,8.8413,8.9285,10.6754,10.4677,12.4491,12.3124,14.7764]) #laplace
#data[:,2] = numpy.array([0.0032,0.0032,0.0152,0.0161,0.0444,0.0479,0.1129,0.1235,0.2026,0.2224,0.3575,0.4008,0.5675,0.6663,0.9216,1.0901,1.2721,1.5156,1.7765,2.1278,2.3576,2.8379,3.1811,3.8405,3.9585,4.7867,4.9639,6.0235,6.0772,7.4179,7.6125,9.2464,8.9206,10.8792,10.7645,13.1394,12.4796,15.2699,14.9004,18.2638]) #27pt

#data[:,2] = numpy.array([0.0032,0.0034,0.0110,0.0118,0.0287,0.0318,0.0638,0.0738,0.0123,0.1394,0.2070,0.2377,0.3387,0.3883,0.5050,0.5978,0.7274,0.8563,1.0041,1.2067,1.3495,1.6022,1.7627,2.1316,2.2240,2.6695,2.7866,3.3815,3.4513,4.1458,4.1549,5.0648,4.9945,6.0295,5.9722,7.2965,7.0027,8.4761,8.2404,10.1081]) #laplace-up
#data[:,2] = numpy.array([0.0025,0.0028,0.0110,0.0119,0.0304,0.0334,0.0761,0.0848,0.1364,0.1521,0.2404,0.2752,0.3824,0.4604,0.6222,0.7515,0.8587,1.0399,1.1953,1.4558,1.5854,1.9358,2.1358,2.6216,2.6587,3.2579,3.3307,4.0997,4.0789,5.0503,5.0958,6.2835,5.9690,7.3975,7.1833,8.9093,8.3525,10.3773,9.9739,12.39]) #27pt-up

#data[:,2] = numpy.array([0.0076,0.0079,0.0433,0.0466,0.1322,0.1453,0.2997,0.3428,0.5929,0.6952,1.0431,1.2576,1.6874,2.0164,2.5240,3.0961,3.7078,4.4712,4.9265,6.1216,6.6668,8.2959,8.6897,10.8456,11.0985,13.8625,13.9045,17.3034,17.3149,21.4352]) #classic-up
#data[:,2] = numpy.array([0.0101,0.0105,0.0639,0.0675,0.1987,0.2147,0.4530,0.5067,0.8897,1.0209,1.5675,1.8585,2.5380,2.9987,3.8121,4.6221,5.5891,6.7021,7.4658,9.1906,10.1077,12.5133,13.1937,16.3747,16.8687,20.9378,21.1622,26.2971,26.3926,32.3284]) #classic

#data[:,2] = numpy.array([0.0083,0.0083,0.0444,0.0470,0.1339,0.1448,0.3011,0.3387,0.5931,0.6893,1.0458,1.2559,1.6970,2.0129,2.5433,3.0819,3.7294,4.4430,4.9499,6.0802,6.7052,8.2310,8.705710.7513,11.1138,13.7201,,,,])

print 'xx\n', xx
print 'yy\n',yy
print 'data to be fit\n', data[:, 2]

a = 0.00001
alpha = 0.3
c = 0
gmod = Model(gaussian)

print 'data to be fit\n', data[:, 2]
gmod.set_param_hint('a', value=a, min=0, max=0.001)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=1)
gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[0:, 2], x=data[0:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
gmod = Model(gaussian)
print 'data to be fit\n', data[10:, 2]
gmod.set_param_hint('a', value=a, min=0, max=0.001)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=1)
gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[10:, 2], x=data[10:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
gmod = Model(gaussian)
print 'data to be fit\n', data[20:, 2]
gmod.set_param_hint('a', value=a, min=0, max=0.001)
gmod.set_param_hint('alpha', value=alpha, min=0.1, max=1)
gmod.set_param_hint('c',value=c,min=-10,max=10)
params = gmod.make_params()
result = gmod.fit(data[20:, 2], x=data[20:, 0:2], params=params)
print result.fit_report(min_correl=0.25)
#print result.best_values
#print result.best_fit
