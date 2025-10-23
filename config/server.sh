set -e

iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP
ip route add 192.168.11.0/24 via 10.42.0.3
ip route add 192.168.12.0/24 via 10.42.0.4
