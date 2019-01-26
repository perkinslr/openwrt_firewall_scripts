#!/usr/bin/python3.7 -I

import time
import os
import pwd

import re

import sys

me = pwd.getpwuid(int(os.environ['ouid'])).pw_name

if len(sys.argv) < 6:
	print("""Usage: portforward <proto> <src_port> <dest_ip> <dest_port> <name> [timeout]""")
	raise SystemExit(1)

		

proto = sys.argv[1]
src_port = sys.argv[2]
dest_ip = sys.argv[3]
dest_port = sys.argv[4]
name = sys.argv[5]

if len(sys.argv) < 7:
	timeout = time.strftime("%Y-%m-%d")
else:
	timeout = sys.argv[6]

timeout = str.join('-', map(str, time.strptime(timeout, '%Y-%m-%d')[:3]))





proto = list(filter(bool, ('tcp' in proto and 'tcp', 'udp' in proto and 'udp')))

if not proto:
	print("Protocol must be 'tcp' or 'udp' or 'tcp udp'")
	raise SystemExit(5)

proto = str.join(" ", proto)

src_port = int(src_port)
dest_port = int(dest_port)

if src_port < 1024 or dest_port < 1024:
	print("cannot forward restricted ports")
	raise SystemExit(6)

name = re.match('^[a-zA-Z0-9 _]+$', name)
if not name:
	print("Name must match ^[a-zA-Z0-9 _]+$")
	raise SystemExit(2)

name = name.group(0)

dest_ip = re.match('^192.168.1.([0-9]{1,3})$', dest_ip)
if not dest_ip:
	print("dest_ip must be an IPv4 address on the local network")
	raise SystemExit(3)

if not (1 < int(dest_ip.group(1)) < 255):
	print("dest_ip cannot be the router, or broadcast")
	raise SystemExit(4)

dest_ip = dest_ip.group(0)



name = name + f' *user={me}*'

with open('/var/portforwarder/add.log', 'a') as f:
	print(time.strftime("%Y-%m-%dT%H:%M:%S%z:"), "port forard add requested by", me, f'args: "{proto}" {src_port} {dest_ip} {dest_port} "{name}" {timeout}', file=f)
	os.system(f'ssh root@192.168.1.1 micropython add_forward.py \\"{proto}\\" {src_port} {dest_ip} {dest_port} \\"{name}\\" {timeout}')
