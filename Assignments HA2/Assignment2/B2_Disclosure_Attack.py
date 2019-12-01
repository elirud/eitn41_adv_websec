from pcapfile import savefile
from ipaddress import ip_address

abu_ipaddress = "160.66.13.37"  # input("Please enter Abu Nazir's IP-address: ")
mix_ipaddress = "204.177.242.216"  # input("Please enter Mix's IP-address: ")
n_partners = 15  # input("Please enter number of partners of Abu Nazir: ")
with open('test.pcap', 'rb') as traffic:
    capfile = savefile.load_savefile(traffic, layers=2, verbose=True)

inputs = []
outputs = []
for pkt in capfile.packets:
    ip_dst = pkt.packet.payload.dst.decode('UTF8')

    if ip_dst == mix_ipaddress:
        inputs.append(pkt)
    else:
        outputs.append(pkt)

out_timestamps = sorted(set(map(lambda x: x.timestamp, outputs)))
outputs = [[y.packet.payload.dst.decode('utf8') for y in outputs if y.timestamp == x] for x in out_timestamps]

new_inputs = [[] for i in range(len(out_timestamps))]

for i in inputs:
    prev_out_timestamp = 0
    for timestamp in out_timestamps:
        if prev_out_timestamp <= i.timestamp < timestamp:
            new_inputs[out_timestamps.index(timestamp)].append(i.packet.payload.src.decode('UTF8'))
        prev_out_timestamp = timestamp

in_out_sets = list(zip(new_inputs, outputs))

i = 0
while i < len(in_out_sets) - 1:
    if abu_ipaddress not in in_out_sets[i][0]:
        del in_out_sets[i]
    else:
        i += 1

outputs.clear()
for i in range(len(in_out_sets)):
    outputs.append(in_out_sets[i][1])

unique_outputs = []

for in_out_set1 in in_out_sets:
    unique_output1 = False
    unique_output2 = False
    for in_out_set2 in in_out_sets:
        if set(in_out_set1[1]).isdisjoint(in_out_set2[1]):
            unique_output1 = True
            unique_output2 = True
        if unique_output1:
            if len(unique_outputs) == 0:
                unique_outputs.append(in_out_set1[1])
                unique_outputs.append(in_out_set2[1])
            else:
                for already_unique in unique_outputs:
                    if not set(already_unique).isdisjoint(in_out_set1[1]):
                        unique_output1 = False
                    if not set(already_unique).isdisjoint(in_out_set2[1]):
                        unique_output2 = False
                if unique_output1:
                    unique_outputs.append(in_out_set1[1])
                if unique_output2:
                    unique_outputs.append(in_out_set2[1])
            break
    if len(unique_outputs) >= n_partners:
        break

for i in range(len(unique_outputs)):
    unique_outputs[i] = set(unique_outputs[i])

print(unique_outputs)
sizes = []
for sets in outputs:
    sizes.append(len(sets))

found_addresses = []

for output in outputs:
    for i in range(len(unique_outputs)):
        if len(unique_outputs[i] & set(output)) == 0:
            continue
        other_intersects = [len(unique_outputs[j] & set(output)) == 0 for j in range(len(unique_outputs)) if j != i]
        if not all(other_intersects):
            continue
        unique_outputs[i] = unique_outputs[i] & set(output)
        if len(unique_outputs[i]) == 1 and list(unique_outputs[i])[0] not in found_addresses:
            found_addresses.append(list(unique_outputs[i])[0])
            break
    if len(found_addresses) == n_partners:
        break

print(found_addresses)

print(sum(list(map(lambda x: int(ip_address(x)), found_addresses))))
