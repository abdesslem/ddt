import struct,socket,sys,time, os
from icmplib import Packet

def main(addr):
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW)
    s.connect((addr,))

datalen = 56
BUFSIZE = 1500


def ping(addr):
    print ("PING (%s): %d data bytes" % (addr,datalen))

    ## create socket
    s = socket.socket(socket.AF_INET,socket.SOCK_RAW,
                        socket.getprotobyname('icmp'))
    s.connect((addr,22))

    ## setuid back to normal user
    os.setuid(os.getuid())

    seq_num = 0
    packet_count = 0
    process_id = os.getpid()
    base_packet = Packet((8,0))

    while 1:
    ## create ping packet 
        seq_num += 1
        pdata = struct.pack("!HHd",process_id,seq_num,time.time())
    
    ## send initial packet 
        base_packet.data = pdata
        s.send(base_packet.packet)
    
        ## recv packet
        buf = s.recv(BUFSIZE)
        current_time = time.time()

        ## parse packet; remove IP header first
        r = Packet.parse(buf[20:])

        ## parse ping data
        (ident,seq,timestamp) = struct.unpack("!HHd",r.data)

        ## calculate rounttrip time
        rtt =  current_time - timestamp
        rtt *= 1000
        print ("%d bytes from %s: id=%s, seq=%u, rtt=%.3f ms" % (len(buf),
                                                        addr, ident, seq, rtt))
        time.sleep(1)
        
if __name__=='__main__':
    import sys
    ping(sys.argv[1])
