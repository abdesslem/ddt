#from scapy.all import *
from scapy.all import sniff
import os 
packetCount = 0

def customAction(packet):
    global packetCount
    packetCount += 1
    return "Packet #%s: %s ==> %s" % (packetCount, packet[0][1].src, packet[0][1].dst)

## Setup sniff, filtering for IP traffic
if not os.geteuid()==0:
   sys.exit("\n Only root can run this script\n")
sniff(filter="ip",prn=customAction)
