#!/usr/bin/python
## get subprocess module 
import subprocess
import pprint
import re
 
## call date command ##
p = subprocess.Popen(["netstat", "-a"], stdout=subprocess.PIPE)
 
## Talk with date command i.e. read data from stdout and stderr. Store this info in tuple ##
## Interact with process: Send data to stdin. Read data from stdout and stderr, until end-of-file is reached.  ##
## Wait for process to terminate. The optional input argument should be a string to be sent to the child process, ##
## or None, if no data should be sent to the child.
(output, err) = p.communicate()
 
## Wait for date to terminate. Get return returncode ##
p_status = p.wait()
if p_status == 0:
    result = []
    output = output.decode("UTF-8")

    for zeile in output.split("\n"):
        if "STREAM" in zeile and "CONNECTED" in zeile:
           zeile = re.sub(r" +", " ", zeile) 
           zeile = zeile.strip().split(" ")
           result.append((zeile[4], zeile[6]))
    
    for zeile in result:
        print(zeile)
else:
    print("S.th. weird happened to netstat")
    exit(p_status)

