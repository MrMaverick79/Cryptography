# -*- coding: utf-8 -*-
"""
Created on 15th May 2021

Caesar Cypher:
    Inputs:
        message - string to be encoded
        key - string;  the ketter used as the key to the code
    Returns:
        encoded message using key 
        

@author: brendantuckerman
"""

def CaesarCypher(message, key):
    alpha =  'abcdefghijklmnopqrstuvwxyz'
    code = ''
    lock = alpha.index(key)
    encodedAlpha = ''
    encodedAlpha += alpha[lock:] + alpha[:lock] #creates encoded alpha
    message = message.lower() #turns to lowercase
    
    for i in message:
        if i == ' ':
            code += ' '
        else:
            j = alpha.index(i)
            code += encodedAlpha[j]
    return code
   

print(CaesarCypher('this is a secret message', 'k'))

    

    