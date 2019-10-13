'''
@author Finn Hurley
diffie_hellman is my own custom library for implementing
the diffie hellman algorithm
'''

import random
from math import gcd

#Function used by server that generates a pair of numbers
#P = prime number, G = primitive root modulo P
def numPairGen():
    P = random.randint(1, 999)
    if not primeNumber(P):
        while not primeNumber(P):
            P = random.randint(1, 999)

    G = random.randint(1, 999)
    while not isPRM(G, P):
        G = random.randint(1, 999)
    
    return P, G

#Function for checking if a number is a prime number
def primeNumber(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n%i is 0:
            return False
        else:
            continue
    return True

'''
Quote from Assignment Specs:
"Note that C is a coprime of P if their greatest common divisor is 1: 
(P, C)= gcd(P, C) = 1."
'''
#Function that returns a list of all ints that are co-primes of P
def findCoPrimesOf(P):
    coPrimeList = []
    for i in range(P):
        if gcd(i, P) is 1:
            coPrimeList.append(i)
    return coPrimeList

#Function that finds out if int C has int K such that G**K % P == C
def hasIntK(G, P, coPrimesofP):
    for C in range(len(coPrimesofP)):
        if (G**coPrimesofP[C]) % P == coPrimesofP[C]:
            #print("G**K % P ==", (G**coPrimesofP[C]) % P)
            return True
    return False

'''
Quote from Assignment Specs:
A number G is a primitive root modulo P if:
For every integer C that is a coprime of P,
There exists an integer K such that G**K mod P = C.
'''
#Function for checking if int G is primitive root modulo of int P
def isPRM(G, P):
    coPrimesofP = findCoPrimesOf(P)
    return True if hasIntK(G, P, coPrimesofP) else False

#Function that generates a random number from 1 to int P
def generateSelectedNo(P):
    return random.randint(1, P-1)

#Function for generating the server's public integer
def serverPublicIntGen(G, N, P):
    return (G**N) % P

#Function for generating the client's public integer
def clientPublicIntGen(G, N, P):
    return (G**N) % P

#Function for generating the server's secret key
def serverSecretKeyGen(B, N, P):
    return (B**N) % P

#Function for generating the client's secret eky
def clientSecretKeyGen(A, N, P):
    return (A**N) % P

#Function for testing the Diffie Hellman Logic (see ../test_DH/ for usage)
def testDiffieHellman():
    p, g = numPairGen()
    print("int P =", p, "int G = ", g)

    serverNo = generateSelectedNo(p)
    clientNo = generateSelectedNo(p)
    print("\nserver number = ", serverNo, "| client number = ", clientNo)

    serverPublicInt = serverPublicIntGen(g, serverNo, p)
    clientPublicInt = clientPublicIntGen(g, clientNo, p)
    print("\nserver sends to client:", serverPublicInt)
    print("client sends to server:", clientPublicInt)

    serverKey = serverSecretKeyGen(clientPublicInt, serverNo, p)
    clientKey = clientSecretKeyGen(serverPublicInt, clientNo, p)
    print("\nserver secret key: ", serverKey)
    print("client secret key: ", clientKey)

    if serverKey == clientKey:
        print("\nTEST PASSED!!!")
    else:
        print("\nTEST FAILED... secret keys were not same")