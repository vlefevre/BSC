import pylab
import subprocess

from os import system
from os import listdir
from os.path import isfile, join

max_prec = 53
src_dir = "../PREC_INCR_0.8/evaluation/"
tolerance = 1e-15
alpha = 2.0
exe="./time_estimator"


result = []
files = [join(src_dir,f) for f in listdir(src_dir) if isfile(join(src_dir, f))]

i=0
for f in files:
	ftab = f.split("_")
	precision = int(ftab[1])
	labeltab = [precision]
	while precision < max_prec:
		if ftab[2][0] == "x":
			precision *= int(ftab[2][1:])
		else:
			precision += int(ftab[2])
		if precision > max_prec:
			precision = max_prec
		labeltab += [precision]
	print labeltab
	#retrieve cost of reaching tolerance under model alpha
	cmd_string = exe+" "+f+" tmp "+str(alpha)
	system(cmd_string)
	print cmd_string
	data = pylab.loadtxt("tmp")
	data = data[data[:,3]<tolerance]
	value=data[0,2]
	print value
	#label = ",".join(str(x) for x in labeltab)
	label = "_".join(ftab[1:])
	result.append([label,value])
	i = i+1

result.sort(key=lambda x: x[1])
resultplot = pylab.array(result)
pylab.plot(pylab.arange(0,len(result)),resultplot[:,1])
pylab.xticks(pylab.arange(0,len(result)),resultplot[:,0],rotation='vertical')
pylab.tight_layout()
pylab.savefig("timemodel_0.8_"+str(tolerance)+"_"+str(alpha)+".pdf")
system("rm tmp")
