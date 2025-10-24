ip route del default
ip route add default via 192.168.12.1

iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
#python3 /elocal/Client.py
