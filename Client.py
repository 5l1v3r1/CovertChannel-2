##########################################################################################################
#Created by: Elton Sia A00800541
#
#File: Client.py
#The client asks for user input regarding what message they wish to send to the server
#It loops through the message and grabbing each character and sending it to the craft method
#the craft method first grabs the Server address from the user when they run the program as a command 
#line argument, then when a character is received, each character is converted into its ASCII decimal 
#value. After that, it is encrypted by multiplying by 4 then adding 5381 to it
#An array of spoofed IP addresses is created and when creating the packet, the source IP is chosen 
#randomly from the array. The source port will be the encrypted message and the destination port 
#will always be 80. I chose 80 because the assumption is that the compromised machine is a web server so 
#that it will make my covert messages less noticeable. I also set the flag to C which means Congestion 
#Window Reduction which is rarely used but all it does is tell the server host to slow down the 
#transfer of data. I then send it back to the msgsend method to send the packet to the server
#I created a random timer between 1 and 5 before sending the packet so that it won't have a specific
#time pattern.
#
#Functions:
#usage()
#craft(Message)
#msgsend()
#Main
#
##########################################################################################################

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
		#User input for what message they want to send
        message = raw_input('Write your message: ')
        message += "\n"
        print "You will be sending: " + message
		#Loop through each character and send it to the craft method before sending the packet to the server
        for msg in message:
            craft_pkt = craft(msg)
            send(craft_pkt)
			#wait a random amount of time between 1 and 5 before sending the next packet
            time.sleep(random.randint(1,5))

#Main
usage()
msgsend()
