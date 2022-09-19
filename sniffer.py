import socket
from pcap import Pcap



  
s = socket.socket(socket.PF_PACKET, socket.SOCK_RAW, socket.ntohs(0x0800))

    # Create Object
p = Pcap('temp.pcap')

while True:

        # Sniff Packet
        packets = s.recvfrom(65565)
        
        # Save captured packets into pcap file
        p.write(packets[0])

        # flush data
        p.pcap_file.flush()
