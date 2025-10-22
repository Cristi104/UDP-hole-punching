FROM ubuntu:latest

RUN apt-get update && apt-get install -y iptables dnsmasq iproute2 net-tools iputils-ping
RUN #rm -rf /var/lib/apt/lists/*

#COPY dnsmasq.conf /etc/dnsmasq.conf
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

#ENTRYPOINT ["/entrypoint.sh"]