# Based on jameslyons caesarCipher.py
# And heavily hecked up by moi
# Original source: https://gist.github.com/jameslyons/8701593

import re

# we need 2 helper mappings, from letters to ints and the inverse
L2I = dict(zip("ABCDEFGHIJKLMNOPQRSTUVWXYZ",range(26)))
I2L = dict(zip(range(26),"ABCDEFGHIJKLMNOPQRSTUVWXYZ"))

def whichWay():
    direction = input("Do you want to 'encipher' or 'decipher'? ")
    if direction == 'encipher':
        hecktext = heckinGet()
        key = keyfinder()
        if key == "all":
            key = 1
            while key <= 26:
                output = encipher(hecktext, key)
                print( "rot" + str(key) + " " + output)
                key += 1
        else:
            output = encipher(hecktext, key)
            print( "rot" + str(key) + " " + output)
    else:
        hecktext = heckinGet()
        key = keyfinder()
        if key == "all":
            key = 1
            while key <= 26:
                output = decipher(hecktext, key)
                print( "rot" + str(key) + " " + output)
                key += 1
        else:
            output = decipher(hecktext, key)
            print( "rot" + str(key) + " " + output)

def heckinGet():
    cipherType = input("Input 'string' or 'file'? ")
    if cipherType == "string":
        return input("Enter the string to evaluate: ")
    elif cipherType == "file":
        file = open(input("Enter the file path: "), "r")
        ciphertext = file.read()
        file.close()
        return ciphertext
    else:
        print("Please enter 'string' or 'file':")
        getContent()

def keyfinder():
    gimme = input("Enter key from 1-26 or type 'all' to run through all combinations: ")
    if re.match("all+", gimme) is not None:
        return "all"
    elif re.match("\d+", gimme) is not None:
        return int(float(gimme))
    else:
        print("Please enter a number or 'all'")
        keyfinder()

def encipher(str, key):
    ciphertext = ""
    for c in str.upper():
        if c.isalpha(): ciphertext += I2L[ (L2I[c] + key)%26 ]
        else: ciphertext += c
    return ciphertext

def decipher(str, key):
    plaintext2 = ""
    for c in str.upper():
        if c.isalpha(): plaintext2 += I2L[ (L2I[c] - key)%26 ]
        else: plaintext2 += c
    return plaintext2

whichWay()
