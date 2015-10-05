''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Nisarga Patel
' Document: SPNencrypt.py
' Description: This is the module for a Substitution Permutation
' Network which is similar to the ones seen in AES and various
' other block ciphers. I apologize for the short variable names
' though these are the standard variable names given in the algorithm.
' Learn more: https://en.wikipedia.org/wiki/Substitution-permutation_network
'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# s-box values
piS = [14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7]

# s-box with redundant keys piS = [0, 1,1,1,4,5,6,7,8,9,10,11,12,13,14,15]
piP = ['placeholder', 1, 5, 9, 13, 2, 6, 10, 14, 3, 7, 11, 15, 4, 8, 12, 16]

# I decided not to make an actual function that converted decimal to binary since there were only 16 values
getBin = ["0000","0001","0010","0011","0100","0101","0110","0111", "1000", "1001", "1010", "1011", "1100", "1101", "1110", "1111"]

# the key schedule for this specific problem is defined below
k = "00111010100101001101011000111111"
k4 = k[12:28]
k5 = k[16:32]

# key schedule dedined as [k1,k2,k3]
k = [k[0:16],k[4:20],k[8:24]]



def xor(a,b):
    
    # the binary xor operation
    
    if a == "1" and b == "1":
        return 0
    elif a == "0" and b == "1":
        return 1
    elif a == "1" and b == "0":
        return 1
    else:
        return 0
    
def getU(w, k):
    
    # gets the u value for the SPN
    
    u = ""
    
    for i in range(len(w)):
        u += str(xor(w[i], k[i]))
        
    return u

def getV(u):
    uSplit = [int(u[0:4],2), int(u[4:8],2), int(u[8:12],2), int(u[12:16],2)]
    newSplit = ""
    
    for num in uSplit:
        newSplit += getBin[piS[num]]
        
    return newSplit

def getW(v):
    
    # preconditions: valid v
    # postconditions: valid w
    
    w = ""
    for i in range(1,17):
        w += v[piP[i]]
    return w
def getCipherText(v):
    
    # preconditions: valid v
    # postconditions: correct ciphertext
    # gets the ciphertext
    
    y = ""
    for i in range(len(v)):
        y += str(xor(v[i], k5[i]))
    return y

def spn(plain):
    # preconditions: valid plain
    # postconditions: correct ciphertext
    # performs the Substitution Permutation Network algorithm on a given binary plaintext
    
    w = plain
    for key in k:
        u = getU(w, key)
        v = getV(u)
        v = "x" + v
        w = getW(v)

    u = getU(w, k4)
    v = getV(u)
    y = getCipherText(v)
    
    print("Ciphertext:", y[0:4], y[4:8], y[8:12], y[12:16])
    print("----------------------------------------")
