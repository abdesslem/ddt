from scapy.all import *

pkts=sniff(count=10)
wrpcap('traffic.pcap',pkts)
wrpcap('traffic.pcap',pkts)
for pkt in pkts:
   print pkt.src, pkt.type
