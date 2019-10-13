#!/usr/bin/env python3

"""
@author Finn Hurley
Diffie Hellman Key Exchange Server in Python

dhServer opens up a socket on a port for the dhClient to connect to in
order to share encrypted messages using the Diffie-Hellman Algorithm.
"""

import traceback
import socket
import sys
sys.path.append('../Diffie_Hellman')

#custom modules for xor encryption and the diffie_hellman algorithm itself
import dhKey as key
import diffie_hellman as dh

#Using localhost for test purposes
HOST = '127.0.0.1'
PORT = 12722

#sending a simple string to confirm that it can send messages both ways...
message = "message from server"

#Opening the socket on port PORT and establishing a connection
try:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()

        while True:
            conn, addr = s.accept()
            with conn:
                print("------ BEGIN COMMUNICATION ------")

                #sending the number pair over to the client
                numP, numG = dh.numPairGen()
                conn.send(str(numP).encode())

                print("Sent number pair:", numP, numG)

                conn.send(str(numG).encode())

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    break

                cPubNo = int(data.decode())
                print("Client public number", cPubNo)

                serverPrivNo = dh.generateSelectedNo(numP)
                serverPubNo = dh.serverPublicIntGen(numG, serverPrivNo, numP)
                conn.send(str(serverPubNo).encode())
                print("Server sends public int: ", serverPubNo)

                serverSecretKey = dh.serverSecretKeyGen(cPubNo, serverPrivNo, numP)
                print("Secret Key Generated:", serverSecretKey)

                print("\nDiffie Hellman Key Exchange Complete! Preparing to Recieve message...")

                while True:
                    data = conn.recv(1024)
                    if not data:
                        break
                    break

                clientMessage = key.byteXor(str(serverSecretKey).encode(), data)
                print("Client Sent:", data.decode())
                print("Which decrypts to:", clientMessage.decode())

                encodedSrvMsg = key.strXor(str(serverSecretKey), message)
                conn.send(encodedSrvMsg)
                print("Server sending back message: ", message)

                print("------END COMMUNICATION------")

except(KeyboardInterrupt):
    sys.exit("Connection closed...")

except(Exception):
    traceback.print_exc()
    sys.exit()