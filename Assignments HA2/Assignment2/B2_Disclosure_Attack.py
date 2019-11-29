from pcapfile import savefile


abu_ipaddress = "159.237.13.37"  # input("Please enter Abu Nazir's IP-address: ")
mix_ipaddress = "94.147.150.188"  # input("Please enter Mix's IP-address: ")
n_partners = 2  # input("Please enter number of partners of Abu Nazir: ")
with open('test.pcap', 'rb') as traffic:
    capfile = savefile.load_savefile(traffic, layers=2, verbose=True)


# print the packets
print ('timestamp\t\teth src\t\t\t\teth dst\t\t\t\tIP src\t\t\tIP dst')
for pkt in capfile.packets:
    timestamp = pkt.timestamp
    # all data is ASCII encoded (byte arrays). If we want to compare with strings
    # we need to decode the byte arrays into UTF8 coded strings
    eth_src = pkt.packet.src.decode('UTF8')
    eth_dst = pkt.packet.dst.decode('UTF8')
    ip_src = pkt.packet.payload.src.decode('UTF8')
    ip_dst = pkt.packet.payload.dst.decode('UTF8')
    print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
