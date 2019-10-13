'''
@author Finn Hurley
dhKey is a custom library for generating keys and xor encryption logic
'''

import random
import string

#Function that makes a mock private key to demonstrate the key exchange
#DEPRECATED - used in Part 1 of Assignment
def privateKeyGen():
    privKeyLen = 50
    keyChars = string.ascii_letters + string.digits

    return ''.join(random.choice(keyChars) for i in range(privKeyLen))

#Function that makes a mock public key to demonstrate the key exchange
#DEPRECATED - used in Part 1 of Assignment
def publicKeyGen():
    pubKeyLen = 20
    keyChars = string.ascii_letters + string.digits

    return ''.join(random.choice(keyChars) for i in range(pubKeyLen))

#Function that does a bitwise xor on 2 strings and returns result in bytes
def strXor(s1, s2):
    s1 = str.encode(s1)
    s2 = str.encode(s2)
    while(len(s1) < len(s2)):
        s1 += s1
    return (bytes(a ^ b for (a,b) in zip(s1, s2)))

#Function that does the same but takes bytes instead of strings
def byteXor(b1, b2):
    while(len(b1) < len(b2)):
        b1 += b1

    return (bytes(a ^ b for (a,b) in zip(b1, b2)))
