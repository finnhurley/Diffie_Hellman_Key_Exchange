'''
@author Finn Hurley
test_diffie_hellman is my own custom module for testing
the main functionality of my diffie hellman algorithm.

NOT DESIGNED TO BE A PRODUCTION-GRADE UNIT TEST,
This is just to prove that my main implementation of the algorithm is correct
and the functions for both the server and client generate the same key.

usage: python3 test_diffie_hellman.py <number of tests>
'''

import sys
sys.path.append('../Diffie_Hellman')
import diffie_hellman as dh

if len(sys.argv) != 2:
    sys.exit("usage: python3 test_diffie_hellman.py <number of tests>")

try:
    iterations = int(sys.argv[1])
    
    for i in range(iterations):
        print("------- TEST", i+1, "-------")
        dh.testDiffieHellman()
except:
    sys.exit("ERROR: argument must be integer.")