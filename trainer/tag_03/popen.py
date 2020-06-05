#!/usr/bin/python
import subprocess, sys
## command to run - tcp only ##
cmd = "/bin/netstat"
 
## run it ##
p = subprocess.Popen(cmd, stdout=subprocess.PIPE)
 
## But do not wait till netstat finish, start displaying output immediately ##
while True:
    out = p.stdout.read(1).decode("utf-8") 
    
    if out == '' and p.poll() != None:
        break
    if out != '':
        sys.stdout.write(out)
        sys.stdout.flush()