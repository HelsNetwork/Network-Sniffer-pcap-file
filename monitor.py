import pyshark



packets_array = []


cap = pyshark.FileCapture('temp.pcap', keep_packets=False)



def counter(*args):
 packets_array.append(args[0])
 
def count_packets():
    cap.apply_on_packets(counter, timeout=10000)
    return len(packets_array)

print("Total packets number:"+str(count_packets()))
