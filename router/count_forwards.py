#!/usr/bin/micropython
from popen import popen

def count():
	idx=0
	while True:
        	if popen('uci get firewall.@redirect[%i]' % idx)[0]:
                	return idx
	        idx += 1


