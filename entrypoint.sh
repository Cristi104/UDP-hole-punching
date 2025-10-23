set -e

sleep 1

for iface in $(ls /sys/class/net | grep -E '^eth[0-9]+'); do
    ip addr show "$iface" | grep -q "192.168." && ip link set "$iface" down && ip link set "$iface" name eth_lan && ip link set eth_lan up
    ip addr show "$iface" | grep -q "10.42." && ip link set "$iface" down && ip link set "$iface" name eth_wan && ip link set eth_wan up
done

echo "Interfaces renamed:"
ip link

UPSTREAM_IFACE=${UPSTREAM_IFACE:-eth_wan}
LAN_IFACE=${LAN_IFACE:-eth_lan}

echo 1 > /proc/sys/net/ipv4/ip_forward

#iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP && \
#iptables -t nat -A POSTROUTING -j MASQUERADE

#iptables -F
#iptables -t nat -F
#iptables -P INPUT DROP
#iptables -P FORWARD DROP
#iptables -P OUTPUT ACCEPT
#
iptables -t nat -A POSTROUTING -o $UPSTREAM_IFACE -s 192.168.0.0/16 -j MASQUERADE
iptables -A FORWARD -i $LAN_IFACE -o $UPSTREAM_IFACE -j ACCEPT
iptables -A FORWARD -i $UPSTREAM_IFACE -o $LAN_IFACE -m state --state ESTABLISHED,RELATED -j ACCEPT

#iptables -A INPUT -i $LAN_IFACE -p udp --dport 53 -j ACCEPT
#iptables -A INPUT -i $LAN_IFACE -p udp --dport 67:68 -j ACCEPT
#
#iptables -A INPUT -i lo -j ACCEPT

echo "Router started — upstream=$UPSTREAM_IFACE, LAN=$LAN_IFACE"

