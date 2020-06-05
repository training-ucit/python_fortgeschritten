#!/usr/bin/python3
import subprocess
r = subprocess.call(["ping", "-c 2", "www.cyberciti.biz"])
print(r)