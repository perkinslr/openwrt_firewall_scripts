#!/usr/bin/micropython
import sys
import ure
from popen import popen

def exit(c):
	raise SystemExit(c)

tr = sys.argv[1]
name = sys.argv[2]
user = sys.argv[3]


s,o,e = popen('uci get firewall.@redirect[%s]'%tr)
if s:
	print("no such rule")
	exit(1)


s,o,e = popen('uci get firewall.@redirect[%s].name'%tr)

if s:
	print("broken rule")
	print(e.read())
	exit(1)

rule_name = o.read()

adding_user = ure.compile('[*]user=([0-9a-zA-Z]+)[*]').search(rule_name)
if not adding_user:
	print("rule not added by portforward-")
	exit(1)

adding_user = adding_user.group(1)

if adding_user != user:
	print("rule added by different user")
	exit(1)

rule_name = rule_name.split(' *user=', 1)[0]
if rule_name != name:
	print("wrong rule name, did you pick the wrong index?")
	exit(1)

popen('uci delete firewall.@redirect[%s]'%tr)
popen('uci commit firewall')
popen('/etc/init.d/firewall reload')
