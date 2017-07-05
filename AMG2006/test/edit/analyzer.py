import pylab
import subprocess
import sys, getopt
from os import system
from os import listdir
from os.path import isfile, join
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import numpy as np

#Default parameters
max_prec = 53
thr = 0.5
tolerance = 1e-8
alpha = 2.0
exe="./time_estimator"

colors={3:'red',2:'blue',1:'black',4:'green',7:'purple',13:'yellow',14:'orange',17:'cyan',46:'#999999',5:'#00CC55'}

#Parse command-line
try:
	opts,args = getopt.getopt(sys.argv[1:],"ht:a:s:","")
except getopt.GetoptError:
	print 'analyzer.py -t tolerance -a alpha_exponent -s threshold (0.5 or 0.8)'
	sys.exit(2)
for opt,arg in opts:
	if opt == "-h":
		print 'analyzer.py -t tolerance -a alpha_exponent -s threshold (0.5 or 0.8)'
		sys.exit()
	elif opt == "-t":
		tolerance = float(arg)
	elif opt == "-a":
		alpha = float(arg)
	elif opt == "-s":
		if arg == "0.5":
			thr = 0.5
		elif arg == "0.8":
			thr = 0.8
		else:
			print 'No existing data for threshold '+arg+'. Exiting.'
			sys.exit(1)
	
src_dir = "../PREC_INCR_"+str(thr)+"/evaluation/"
result = []
files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]

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
	print len(labeltab)
	#retrieve cost of reaching tolerance under model alpha
	cmd_string = exe+" "+join(src_dir,f)+" tmp "+str(alpha)
	system(cmd_string)
	#print cmd_string
	data = np.loadtxt("tmp")
	data = data[data[:,3]<tolerance]
	value=data[0,2]
	print value
	#label = ",".join(str(x) for x in labeltab)
	label = "_".join(ftab[1:])
	result.append([label,value,len(labeltab)])
	i = i+1
print "Found "+str(i)+" files."

result.sort(key=lambda x: int((x[0].split("_"))[0])) #sort by increasing starting precision
#result.sort(key=lambda x: x[1]) #sort by increasing time
resultplot = np.array(result)
yval = np.array(resultplot[:,1],dtype='f8')
cval = np.array(resultplot[:,2],dtype='i8')
bar = plt.bar(np.arange(0,len(result)),yval,0.4)
i=0
for column in bar:
	print cval[i]
	print colors[cval[i]]
	column.set_color(colors[cval[i]])
	i = i+1

plt.xticks(pylab.arange(0,len(result)),resultplot[:,0],rotation='vertical')
plt.tight_layout()

output_file = "timemodel_"+str(thr)+"_"+str(tolerance)+"_"+str(alpha)+".pdf"
plt.savefig(output_file)
print "File "+output_file+" saved."
system("rm tmp")
