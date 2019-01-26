import sys
from popen import popen

from count_forwards import count

proto = sys.argv[1]
src_port = sys.argv[2]
dest_ip = sys.argv[3]
dest_port = sys.argv[4]
name = sys.argv[5]
timeout = sys.argv[6]

if timeout:
	name = name + " exp="+timeout

idx=count()

popen('uci add firewall redirect')
popen('uci set firewall.@redirect[%i]="redirect"'%idx)
popen('uci set firewall.@redirect[%i].target="DNAT"'%idx)
popen('uci set firewall.@redirect[%i].src="wan"'%idx)
popen('uci set firewall.@redirect[%i].dest="lan"'%idx)
popen('uci set firewall.@redirect[%i].proto="%s"'%(idx, proto))
popen('uci set firewall.@redirect[%i].src_dport="%s"'%(idx, src_port))
popen('uci set firewall.@redirect[%i].dest_ip="%s"'%(idx, dest_ip))
popen('uci set firewall.@redirect[%i].dest_port="%s"'%(idx, dest_port))
popen('uci set firewall.@redirect[%i].name="%s"'%(idx, name))

popen('uci commit firewall')
popen('/etc/init.d/firewall reload')
