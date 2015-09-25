import sys
import time
import random
from scapy.all import *

#Command line argument needed to run the program
def usage():
    if len(sys.argv) != 2:
        print "To use: ", sys.argv[0], "Server IP"
        sys.exit()

#Craft the packet with the hidden message to send
def craft(Message):
    global pkt
    global dest
    dest = str(sys.argv[1])
    #converts Message from words to their respective decimal value in ASCII
    hmsg = ord(Message)
	#Encrypts the message to make it harder to see
	encryptedMsg = hmsg*4+5381
    #Array of random IP's to choose from as source IP address
    randIP = ["192.168.0.12", "192.168.0.124", "192.168.0.64",
              "192.168.0.88", "192.168.0.232"]
    pkt = IP(src=random.choice(randIP), dst=dest)/TCP(sport=encryptedMsg, dport=80, flags="C")
    return pkt

#Send the message to the server
def msgsend():
    while True:
        message = raw_input('Write your message: ')
        message += "\n"
        print "You will be sending: " + message
        for msg in message:
            craft_pkt = craft(msg)
            send(craft_pkt)
            time.sleep(random.randint(1,5))

#Main
usage()
msgsend()
