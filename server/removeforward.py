#!/usr/bin/python3.7 -I
import re
import time
import os
import pwd
import sys


me = pwd.getpwuid(int(os.environ['ouid'])).pw_name



idx = int(sys.argv[1])
name = sys.argv[2]

name = re.match('^[a-zA-Z0-9 _]+$', name)
if not name:
	print("Name must match ^[a-zA-Z0-9 _]+$")
	raise SystemExit(2)

name = name.group(0)
#name = name + f' *user={me}*'


with open('/var/portforwarder/remove.log', 'a') as f:
	print(time.strftime("%Y-%m-%dT%H:%M:%S%z:"), "port forard remove requested by", me, f'args: {idx}, "{name}"', file=f)
	os.system(f'ssh root@192.168.1.1 micropython remove_forward.py {idx} \\"{name}\\" \\"{me}\\"')
