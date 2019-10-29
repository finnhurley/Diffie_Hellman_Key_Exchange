'''
@author Finn Hurley
dhCrypt is a custom library for xor encryption logic
'''
#Function that does a bitwise xor on 2 strings and returns result in bytes
#S1 MUST BE THE COMMON KEY
def strXor(s1, s2):
    s1 = str.encode(s1)
    s2 = str.encode(s2)
    while(len(s1) < len(s2)):
        s1 += s1
    return (bytes(a ^ b for (a,b) in zip(s1, s2)))

#Function that does the same but takes bytes instead of strings
#B1 MUST BE THE COMMON KEY
def byteXor(b1, b2):
    while(len(b1) < len(b2)):
        b1 += b1

    return (bytes(a ^ b for (a,b) in zip(b1, b2)))
