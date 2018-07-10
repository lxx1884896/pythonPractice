import os

import subprocess


cmdlist=[]
#aa=("cd new-text-detection-ctpn-master && python ctpn/demo.py" )
#cmdlist.append("python ctpn/demo.py")


#for a in cmdlist:
    #subprocess.call(a)

a="cd new-text-detection-ctpn-master"
b="python ctpn/demo.py"


cmd = "{0} && {1}".format(a, b)
print cmd 
os.system(cmd)
