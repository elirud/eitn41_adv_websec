from pcapfile import savefile


abu_ipaddress = input("Please enter Abu Nazir's IP-address: ")
mix_ipaddress = input("Please enter Mix's IP-address: ")
n_partners = input("Please enter number of partners of Abu Nazir: ")
traffic = open('test.pcap', 'rb')
capfile = savefile.load_savefile(traffic, layers=2, verbose=True)


# print the packets
print ('timestamp\teth src\t\t\teth dst\t\t\tIP src\t\tIP dst')
for pkt in capfile.packets:
    timestamp = pkt.timestamp
    # all data is ASCII encoded (byte arrays). If we want to compare with strings
    # we need to decode the byte arrays into UTF8 coded strings
    eth_src = pkt.packet.src.decode('UTF8')
    eth_dst = pkt.packet.dst.decode('UTF8')
    ip_src = pkt.packet.payload.src.decode('UTF8')
    ip_dst = pkt.packet.payload.dst.decode('UTF8')
    print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
