set -e

UPSTREAM_IFACE=${UPSTREAM_IFACE:-eth0}
LAN_IFACE=${LAN_IFACE:-eth1}

#iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP && \
#iptables -t nat -A POSTROUTING -j MASQUERADE

iptables -F
iptables -t nat -F
iptables -P INPUT DROP
iptables -P FORWARD DROP
iptables -P OUTPUT ACCEPT

iptables -A FORWARD -i $LAN_IFACE -o $UPSTREAM_IFACE -j ACCEPT
iptables -A FORWARD -i $UPSTREAM_IFACE -o $LAN_IFACE -m state --state ESTABLISHED,RELATED -j ACCEPT
iptables -t nat -A POSTROUTING -o $UPSTREAM_IFACE -j MASQUERADE

iptables -A INPUT -i $LAN_IFACE -p udp --dport 53 -j ACCEPT
iptables -A INPUT -i $LAN_IFACE -p udp --dport 67:68 -j ACCEPT

iptables -A INPUT -i lo -j ACCEPT

echo "Router started — upstream=$UPSTREAM_IFACE, LAN=$LAN_IFACE"

