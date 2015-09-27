##########################################################################################################
#Created by: Elton Sia A00800541
#
#File: Server.py
#The server sniffs for all the IP addresses and send it to the parse method
#The parse method checks for the IP and if it matches with an allow IP from the array,
#It then grabs the source port from that IP address and decrypts the message before printing it out
#
#Functions:
#parse(pkt)
#Main
##########################################################################################################

import sys
from scapy.all import *

#Look for the specific IP addresses for the covert traffic
def parse(pkt):
    src_ip = pkt[IP].src
    #Array of IP that should be looked for
    randIP = ["192.168.0.12", "192.168.0.124", "192.168.0.64",
              "192.168.0.88", "192.168.0.232"]
	#If the IP address matches with an IP in the array, grab the source port and decrypt it then print the message
    for i in randIP:
        if src_ip == i:
			#grabs the source port
            msg = chr(pkt['TCP'].sport)
			#decrypts the message by subtracting the current source port to 5381 then dividing by 4
			decryptMsg = (msg-5381)/4
			#Change the decimal value back to its ASCII character value
			decryptedMsg = chr(decryptMsg)
            sys.stdout.write(decryptedMsg)
            
#Main
sniff(filter="ip", prn=parse)
