from pcapfile import savefile
from ipaddress import ip_address

def intersection(lst1, lst2):
    lst3 = [list(filter(lambda x: x in lst1, sublist)) for sublist in lst2]
    return lst3



nazir_ipaddress = "161.53.13.37"  # input("Please enter Abu Nazir's IP-address: ")
mix_ipaddress = "11.192.206.171"  # input("Please enter Mix's IP-address: ")
n_partners = 12  # input("Please enter number of partners of Abu Nazir: ")


with open('test2.pcap', 'rb') as traffic:
    capfile = savefile.load_savefile(traffic, layers=2, verbose=True)


nazir_batches = []
temp = []
nazir_hasSent = False
mix_hasSent = False

# print the packets
print ('timestamp\t\teth src\t\t\t\teth dst\t\t\t\tIP src\t\t\tIP dst')
for pkt in capfile.packets:
    eth_src = pkt.packet.src.decode('UTF8')
    eth_dst = pkt.packet.dst.decode('UTF8')
    ip_src = pkt.packet.payload.src.decode('UTF8')
    ip_dst = pkt.packet.payload.dst.decode('UTF8')
    timestamp = pkt.timestamp

    prev_mix_hasSent = mix_hasSent
    if ip_src != mix_ipaddress:
        mix_hasSent = False
        temp = []
    if ip_src == mix_ipaddress:
        mix_hasSent = True
        temp.append(ip_dst)
    if ip_src == nazir_ipaddress:
        nazir_hasSent = True
    if not prev_mix_hasSent and mix_hasSent:
        if nazir_hasSent and mix_hasSent:
            nazir_batches.append(temp)
            nazir_hasSent = False


    # all data is ASCII encoded (byte arrays). If we want to compare with strings
    # we need to decode the byte arrays into UTF8 coded strings

    # print ('{}\t\t{}\t{}\t{}\t{}'.format(timestamp, eth_src, eth_dst, ip_src, ip_dst))
print(nazir_batches)
nazir_set_batches = []
nazir_unique_batches = []

for batch in nazir_batches:
    nazir_set_batches.append(set(batch))

for i in range(0, len(nazir_set_batches) - 1):
    batchi = nazir_set_batches[i]
    for j in range(i + 1, len(nazir_set_batches)):
        batchj = nazir_set_batches[j]
        if batchi.isdisjoint(batchj):
            unique_batchi = True
            unique_batchj = True
            for k in range(len(nazir_unique_batches)):
                batch = nazir_unique_batches[k]
                if not batchi.isdisjoint(batch):
                    unique_batchi = False
                if not batchj.isdisjoint(batch):
                    unique_batchj = False
            if unique_batchi:
                nazir_unique_batches.append(batchi)
            if unique_batchj:
                nazir_unique_batches.append(batchj)
        if len(nazir_unique_batches) == n_partners:
            break
    if len(nazir_unique_batches) == n_partners:
        break

oneMatch = True
recipients = []

for batchu in nazir_unique_batches:
    for batchi in nazir_set_batches:
        if len(batchu) == 1:
            recipients.append(list(batchu)[0])
            break
        if not len(batchu.intersection(batchi)) == 0:
            for batchj in nazir_unique_batches:
                if batchu == batchj:
                    continue
                if not len(batchi.intersection(batchj)) == 0:
                    oneMatch = False
                    break
            if oneMatch:
                batchu.intersection_update(batchi)
            oneMatch = True

print(recipients)
print(sum(list(map(lambda x: int(ip_address(x)), recipients))))
