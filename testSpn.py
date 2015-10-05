''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
' Author: Nisarga Patel
' Document: testSpn.py
' Description: This is a test file for the Substitution Permutation
' Network module created to encrypt binary plaintext strings. The
' exact key for this test is defined at the top of the SPNencrypt
' module. This test file was created in order to look for cipher
' text attacks in this specific Substitution Permutation Network.
'
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

import SPNencrypt

def main():
    
    plain = "0010011010110111"
    SPNencrypt.spn(plain)
    
    plain = "1111111111111111"
    SPNencrypt.spn(plain)
    
    plain = "0000000000000000"
    SPNencrypt.spn(plain)
    
    plain = "1111111111111110"
    SPNencrypt.spn(plain)
    
    plain = "1110111111011110"
    SPNencrypt.spn(plain)
    
    plain = "1110101011011110"
    SPNencrypt.spn(plain)

    plain = "1110101000011110"
    SPNencrypt.spn(plain)
    
    plain = "0101010101010101"
    SPNencrypt.spn(plain)
    
    plain = "0101010101010101"
    SPNencrypt.spn(plain)
    
    plain = "0101000000000101"
    SPNencrypt.spn(plain)
    
    plain = "0101000010100101"
    SPNencrypt.spn(plain)
    
    plain = "1110111111110101"
    SPNencrypt.spn(plain)
    
    plain = "0000000100001000"
    SPNencrypt.spn(plain)
    
    plain = "0001000100001001"
    SPNencrypt.spn(plain)
    
    plain = "0110111001110111"
    SPNencrypt.spn(plain)
    
    plain = "1111011111011101"
    SPNencrypt.spn(plain)
    
main()