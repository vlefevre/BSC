import pylab
import subprocess
import sys, getopt
from os import system
from os import listdir
from os.path import isfile, join
import matplotlib.cm as cm
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import numpy as np
import math

font = {'family' : 'normal',
        'size'   : 12}

pylab.rc('font', **font)

#Default parameters
max_prec = 53
thr = 0.5
tolerance = 1e-8
alpha = 2.0
exe="./time_estimator"
order_incr = False
coeff=1

colors={1:'black',2:'blue',3:'red',4:'green',5:'#00CC55',7:'purple',13:'yellow',14:'orange',17:'cyan',46:'#999999'}

#Parse command-line
try:
	opts,args = getopt.getopt(sys.argv[1:],"ht:a:s:i","")
except getopt.GetoptError:
	print 'analyzer.py -t tolerance -a alpha_exponent -s threshold (0.5 or 0.8) [-i]'
	sys.exit(2)
for opt,arg in opts:
	if opt == "-h":
		print 'analyzer.py -t tolerance -a alpha_exponent -s threshold (0.5 or 0.8) [-i]'
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
		elif arg == "0.6":
			thr = 0.6
                        coeff = 2./3.
		else:
			print 'No existing data for threshold '+arg+'. Exiting.'
			sys.exit(1)
	elif opt == "-i":
		order_incr = True

src_dir = "../PREC_INCR_"+str(thr)+"/evaluation/"
result = []
files = [f for f in listdir(src_dir) if isfile(join(src_dir, f))]


print "Found "+str(len(files))+" files."

minVal=100000000
minLabel=""
maxValue=0
for f in files:
	ftab = f.split("_")
	precision = int(ftab[1])
	labeltab = [precision]
	while precision < max_prec:
		if ftab[2][0] == "x":
			precision *= float(ftab[2][1:])
			precision = math.floor(precision)
		else:
                        if int(ftab[2]) == 0:
                            break
			precision += int(ftab[2])
		if precision > max_prec:
			precision = max_prec
		labeltab += [precision]
	#print len(labeltab)
	#retrieve cost of reaching tolerance under model alpha
	cmd_string = exe+" "+join(src_dir,f)+" tmp "+str(alpha)
	system(cmd_string)
	#print cmd_string
	data = np.loadtxt("tmp")
	data = data[data[:,3]<tolerance]
        if data.shape != (0,4):
            value=coeff*data[0,2]
            #print value
            #label = ",".join(str(x) for x in labeltab)
            label = "_".join(ftab[1:])
            result.append([label,value,len(labeltab)])
            print label+" "+str(value)
            if value < minVal:
                    minVal = value
                    minLabel = label
            if value > maxValue:
                    maxValue = value

print "Minimum time is "+str(minVal)+", for "+minLabel+"."

if order_incr:
	result.sort(key=lambda x: x[1]) #sort by increasing time
else:
	result.sort(key=lambda x: int((x[0].split("_"))[0])) #sort by increasing starting precision
resultplot = np.array(result)
yval = np.array(resultplot[:,1],dtype='f8')
cval = np.array(resultplot[:,2],dtype='i8')
bar = plt.bar(np.arange(0,len(result)),yval,0.4,align='edge')
i=0
for column in bar:
	column.set_color(colors[cval[i]])
	i = i+1
handles = []
for key in sorted(colors):
	rpatch = mpatches.Patch(color=colors[key], label=str(key))
	handles.append(rpatch)
plt.legend(loc=2,handles=handles,ncol=(len(colors)+1)/2,prop={'size':10},title='Number of precisions used')
plt.ylabel("Units of time",fontsize=16)
plt.xlabel("Precision sets",fontsize=16)
plt.xticks(pylab.arange(0,len(result)),resultplot[:,0],rotation='vertical')
#manual coloring of sets with one precision available for pmbs
#plt.gca().get_xticklabels()[18].set_color("red") 
plt.title(r"Time to reach accuracy "+str(tolerance)+"\nfor different strategies with threshold "+str(thr)+"\nand time model is $T(b)=b^{"+str(alpha)+"}$.")
plt.xlim([0,len(files)])
plt.ylim([0,maxValue+3])
plt.tight_layout()

output_file = "timemodel_"+str(thr)+"_"+str(tolerance)+"_"+str(alpha)+".pdf"
plt.savefig(output_file)
print "File "+output_file+" saved."
system("rm tmp")
