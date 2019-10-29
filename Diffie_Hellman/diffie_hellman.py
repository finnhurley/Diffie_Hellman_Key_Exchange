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
    P = random.randint(2, 9999)
    if not primeNumber(P):
        while not primeNumber(P):
            P = random.randint(1, 9999)

    G = random.randint(1, 9999)
    while not isPRM(G, P):
        G = random.randint(1, 9999)
    
    print("P:", P, "G:", G,)
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
            return True
    return False

#Function for checking if int G is primitive root modulo of int P
def isPRM(G, P):
    coPrimesofP = findCoPrimesOf(P)
    return True if hasIntK(G, P, coPrimesofP) else False

#Function that generates a random number from 1 to int P
def generateSelectedNo(P):
    return random.randint(1, P-1)

#Function for generating public and secret keys on both sides
def keyGen(X, N, P):
    return(X**N) % P