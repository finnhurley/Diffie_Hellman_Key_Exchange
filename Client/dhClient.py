#!/use/bin/env python3

"""
@author Finn Hurley
Diffie Hellman Key Exchange Client in Python

dhClient connects to the port the dhServer listens on and starts the 
diffie hellman key exchange
"""

import traceback
import socket
import string
import sys
sys.path.append('../Diffie_Hellman')

#custom modules for xor encryption and the diffie_hellman algorithm itself
import dhKey as key
import diffie_hellman as dh

HOST = '127.0.0.1'
PORT = 12722

if len(sys.argv) != 2 or not isinstance(sys.argv[1], str):
    sys.exit("Usage: python dhClient.py <message to encrypt>")

toEncrypt = sys.argv[1]
if len(toEncrypt) > 20:
    sys.exit("Error: maximum char size = 20")


try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        print("------ BEGIN COMMUNICATION ------")


        s.connect((HOST, PORT))

        data = s.recv(1024)
        numP = int(data.decode())

        print("received int P: ", numP)

        data = s.recv(1024)
        numG = int(data.decode())

        print("received int G: ", numG)
        
        clientPrivNo = dh.generateSelectedNo(numP)
        clientPubNo = dh.clientPublicIntGen(numG, clientPrivNo, numP)
        print("Private num:", clientPrivNo, "public num:", clientPubNo)

        s.send(str(clientPubNo).encode())

        data = s.recv(1024)
        sPubNo = int(data.decode())
        print("Server sent public int:", sPubNo)

        clientSecretKey = dh.clientSecretKeyGen(sPubNo, clientPrivNo, numP)
        print("Secret Key Generated:", clientSecretKey)

        print("\nDiffie Hellman Key Exchange Complete! Preparing Message: ", toEncrypt)

        xorMessage = key.strXor(str(clientSecretKey), toEncrypt)
        s.send(xorMessage)

        data = s.recv(1024)
        decodedSrvMsg = key.byteXor(str(clientSecretKey).encode(), data)

        print("Server Sent: ", data.decode())
        print("Which decrypts to: ", decodedSrvMsg.decode())

        print("------ END COMMUNICATION ------")

        s.close()

except(KeyboardInterrupt):
    sys.exit("Connection closed...")

except(Exception):
    traceback.print_exc()
    sys.exit()