#!/usr/bin/env python3

import subprocess
import sys
import re

cmd = "/bin/netstat"
cmd_arg = "-a"

proc = subprocess.Popen([cmd, cmd_arg], stdout=subprocess.PIPE)

output, err = proc.communicate()

re_compiled = re.compile('STREAM\s+CONNECTED\s+(\d+)')

proc_state = proc.wait()

lines = output.decode('UTF-8').split("\n")
#print('\n'.join(lines))


for l in lines:
    m = re_compiled.search(l.strip())
    if m:
        print(m.group(1))

