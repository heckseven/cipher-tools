import re
from collections import Counter

ciphertext = ""

def getContent():
    cipherType = input("Analyze 'string' or 'file'? ")
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

def removeWhitespace(string):
    if input("Remove spaces and newlines from cipher? (yes/no) ") == "yes":
        string = re.sub(r"[\s]*", "", string)
        return string
    else:
        return string

def analyze(cipher):
    ocipher = cipher
    cipher = removeWhitespace(cipher)
    count =  int(input("Enter the segment length to analyze: "))
    if count != 1:
        cipher = [cipher[i:i+count] for i in range(0, len(cipher), count)]
    content=Counter(cipher).most_common()
    readout = {}
    print("")
    for i in content:
        if i[1] in readout:
            readout[i[1]].append(i[0])
        else:
            readout[i[1]] = []
            readout[i[1]].append(i[0])
    for i in readout:
        print(str(i) + " - " + str(readout[i]))
    if input("\nContinue frequency analysis on this cypher? (yes/no) ") == "yes":
        analyze(ocipher)

analyze(getContent())
