'''
@author Finn Hurley
test_diffie_hellman is my own custom module for testing
the main functionality of my diffie hellman algorithm.

Not designed to be a super-amazing production grade unit test
just proving that my initial implementation of the algorithm is correct
'''

import sys
import time
import random
import string
sys.path.append('../Diffie_Hellman')
import dhCrypt as crypt
import diffie_hellman as dh

def run_tests():
    passedTests = 0
    failedTests = 0

    if test_xor_logic() == True:
        print("PASSED")
        passedTests += 1
    else:
        print("FAILED")
        failedTests += 1

    time.sleep(1)

    print("TESTS COMPLETE:", passedTests, "Passed", failedTests, "Failed!")

#Tests entire dhCrypt module
def test_xor_logic():
    print("-----Testing dhCrypt xor logic-----")

    time.sleep(0.5)
    alphabet = string.ascii_letters + string.digits
    testString = ''.join(random.choice(alphabet) for i in range(20))
    xorString = "10101010101"
    xorBytes = xorString.encode()
    print("Creating random string:", testString, "xoring with:", xorString)

    time.sleep(0.5)
    strXorEncrypt = crypt.strXor(xorString, testString)
    print("dh.strXor() Result:", strXorEncrypt, "Preparing dh.byteXor()...")

    time.sleep(0.5)
    byteXorEncrypt = crypt.byteXor(xorBytes, strXorEncrypt)

    print("Comparing strings:", testString, byteXorEncrypt.decode())
    return True if(testString == byteXorEncrypt.decode()) else False


def test_gen_numpair():
    print("-----Testing numPair generation-----")
    return True

def test_keyGen():
    print("-----Testing key generation-----")
    return True

def test_numGen():
    print("-----Testing numGen generation-----")
    return True

def test_exchange_keyOnly():
    print("-----Testing exchange logic-----")
    return True

def test_exchange_full():
    print("-----Testing exchange and encryption-----")
    return True

run_tests()