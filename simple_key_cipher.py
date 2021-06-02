# -*- coding: utf-8 -*-
"""
Created on 2nd June 2021

Simple key cipher:
    Takes a message (str) to be encoded and a key (str)
    Uses the key to change the letters by i amount, where i is 
    the position of the letter of the key in the alphabet
    
    So key C A T
    Message Secret
    Would match
    
                    s e c  r e t
                    c a t  c a t
    position plus  3 1 20 3 1 20
    
    output would be vfwufn
    
@author: brendantuckerman
"""

def key_cipher(message, key):
            
    alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
    encoded = ''
    message = message.lower() #make all lowercase
    message = message.replace(' ','') #remove spaces
    #key needs to be made as long as message
    stretch_key = ''
    while len(stretch_key) < len(message):
        for i in range(len(key)):
            stretch_key += key[i]
   
    #once the key and the message are the same length, 'add' each together
    while len(encoded) < len(message):
        for i in range(len(message)):
            k = alpha.find(message[i])
            l = alpha.find(stretch_key[i])
            encoded += alpha[k +l]
        
    return encoded

#test
secret = key_cipher('This is a secret message', 'lock')
print(secret)

def key_cipher_decode(message, key):
        
        alpha = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
        decoded = ''
        stretch_key = ''
        
        while len(stretch_key) < len(message):
            for i in range(len(key)):
                stretch_key += key[i]
                
        while len(decoded) < len(message):
            for i in range(len(message)):
                k = alpha.find(message[i])
                l = alpha.find(stretch_key[i])
                decoded += alpha[k - l]
        
        return decoded

#test  
unlock = key_cipher_decode(secret, 'lock')
print(unlock)
