#!/usr/bin/micropython
from count_forwards import count

from popen import popen

import os

idx=count()
for i in range(idx):
	print("Forward rule:",i)
	os.system('uci show firewall.@redirect[%i]'%i)
