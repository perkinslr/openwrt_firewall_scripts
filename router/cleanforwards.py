#!/usr/bin/micropython
from popen import popen

from count_forwards import count

import sys

import ure

date_pattern = ure.compile('exp=([0-9][0-9][0-9][0-9])-([0-1]?[0-9])-([0-9][0-9])')

import time

today = time.localtime()[:3]

idx=count()

for i in reversed(range(idx)):
	r = popen('uci get firewall.@redirect[%i].name' % i)
	if r[0]:
		print('uci get firewall.@redirect[%i].name' % i)
		print(r[0])
		print(r[1].read())
		print(r[2].read())
		sys.exit(1)
	name = r[1].read().strip()
	match = date_pattern.search(name)
	if match:
		date = int(match.group(1)), int(match.group(2)), int(match.group(3))
		if date < today:
			print("Removing:", name)
			popen('micropython remove_forward.py %i' %i)
