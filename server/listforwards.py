#!/usr/bin/python3.7 -I

import time
import os
import pwd

me = pwd.getpwuid(int(os.environ['ouid'])).pw_name

os.environ['HOME']='/var/portforwarder'
os.environ['USER']='portforwarder'


with open('/var/portforwarder/list.log', 'a') as f:
	print(time.strftime("%Y-%m-%dT%H:%M:%S%z:"), "port forard list requested by", me, file=f)
	os.system('ssh -i $HOME/.ssh/id_rsa root@192.168.1.1 micropython list_forwards.py')
