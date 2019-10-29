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

#Runs the tests, counts the number of passes and failures
def run_tests():
    random.seed(a=None, version=2)

    passedTests = 0
    failedTests = 0

    tests = [test_dhCrypt(),
            test_dh_numPair(),
            test_dh_generateSelectedNo(),
            test_dh_exchange()]

    for t in tests:
        if t == True:
            passedTests += 1
        else:
            failedTests += 1
    
    print("TESTS COMPLETE:", passedTests, "Passed", failedTests, "Failed!")

#Tests entire dhCrypt module
def test_dhCrypt():
    print("-----Testing dhCrypt xor logic-----")

    time.sleep(0.5)
    alphabet = string.ascii_letters + string.digits
    secretKeyChars = string.digits
    testString = ''.join(random.choice(alphabet) for i in range(20))
    xorString = ''.join(random.choice(secretKeyChars) for i in range(3))
    xorBytes = xorString.encode()
    print("Creating random string:", testString, "xoring with random key:", xorString)

    time.sleep(0.5)
    strXorEncrypt = crypt.strXor(xorString, testString)
    print("dh.strXor() Result:", strXorEncrypt, "Preparing dh.byteXor()...")

    time.sleep(0.5)
    byteXorEncrypt = crypt.byteXor(xorBytes, strXorEncrypt)

    print("Comparing strings:", testString, byteXorEncrypt.decode())
    if testString == byteXorEncrypt.decode():
        print("TEST PASSED\n")
        return True
    else:
        print("TEST FAILED\n")
        return False

#Tests that the number pair are selected correctly according to algorithm
def test_dh_numPair():
    print("-----Testing dh.numPair()-----")

    time.sleep(0.5)
    intP, intG = dh.numPairGen()
    print("Ensuring P is always prime and G is always PRM P")
    print("Generated Number Pair:", intP, intG)

    time.sleep(0.5)
    if dh.primeNumber(intP)==True and dh.isPRM(intG, intP)==True:
        print("TEST PASSED\n")
        return True
    else:
        print("TEST FAILED\n")
        return False

#Tests that the selected number is in fact P-1
def test_dh_generateSelectedNo():
    print("-----Testing dh.generateSelectedNo-----")
    
    time.sleep(0.5)
    print("ensuring the generatedNo is always less than int P")
    print("testing 10 instances")
    for i in range(10):
        testInt = random.randint(1, 999)

        time.sleep(0.1)
        selectedNo = dh.generateSelectedNo(testInt)
        print("testInt: ", testInt, "selectedNo: ", selectedNo)

        if selectedNo >= testInt:
            print("TEST FAILED\n")
            return False
    
    print("TEST PASSED\n")
    return True

def test_dh_exchange():
    print("-----Testing exchange logic-----")

    time.sleep(0.1)
    print("1: Server makes key pair")
    intP, intG = dh.numPairGen()

    time.sleep(0.1)
    serverPrivNo = dh.generateSelectedNo(intP)
    print("2: Server's secret integer:", serverPrivNo)

    time.sleep(0.1)
    serverPubNo = dh.keyGen(intG, serverPrivNo, intP)
    print("3: Server generates public integer:", serverPubNo)

    time.sleep(0.1)
    clientPrivNo = dh.generateSelectedNo(intP)
    print("4: Client's secret integer:", clientPrivNo)

    time.sleep(0.1)
    clientPubNo = dh.keyGen(intG, clientPrivNo, intP)
    print("5: Client generates public integer:", clientPubNo)

    time.sleep(0.1)
    serverSecretKey = dh.keyGen(clientPubNo, serverPrivNo, intP)
    clientSecretKey = dh.keyGen(serverPubNo, clientPrivNo, intP)
    print("6: Server secret key:", serverSecretKey, "Client's secret key:", clientSecretKey)

    if serverSecretKey == clientSecretKey:
        print("TEST PASSED\n")
        return True
    else:
        print("TEST FAILED\n")
        return False

run_tests()