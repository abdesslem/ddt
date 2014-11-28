#from scapy.all import *
from scapy.all import sniff
import os, sys
import socket
packetCount = 0

def getIp(url):
    dname = url.split("/")[0]
    ip = socket.gethostbyname(dname)
    return ip 
def customAction(packet):
    global packetCount
    packetCount += 1
    return "Packet #%s: %s ==> %s" % (packetCount, packet[0][1].src, packet[0][1].dst)

## Setup sniff, filtering for IP traffic
if not os.geteuid()==0:
   sys.exit("\n Only root can run this script\n")
#prn: function to apply to each packet. If something is returned,
#             it is displayed. Ex:
#           ex: prn = lambda x: x.summary()
ip=str(getIp("www.facebook.com"))
#sniff(filter=ip,prn=customAction)
#build_filter = "src host " + ip
#sniff(filter=build_filter,prn=customAction)
