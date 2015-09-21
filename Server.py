import sys
from scapy.all import *

#Look for the specific IP addresses for the covert traffic
def parse(pkt):
    src_ip = pkt[IP].src
    #Array of IP that should be looked for
    randIP = ["192.168.0.12", "192.168.0.124", "192.168.0.64",
              "192.168.0.88", "192.168.0.232"]
    for i in randIP:
        if src_ip == i:
            msg = chr(pkt['TCP'].sport)
            sys.stdout.write(msg)
            
#Main
sniff(filter="ip", prn=parse)
