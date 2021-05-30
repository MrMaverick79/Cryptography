# -*- coding: utf-8 -*-
"""
Created on 15th May

Caesar Cracker:
    Brute force crack for the Caesar Cypher
    Input: message coded using the cypher
    Prints strings cracked for each letter of the alphabet

@author: brendantuckerman
"""

def CaesarCrack(message):
    alpha =  'abcdefghijklmnopqrstuvwxyz'
    attempt = ' '
    encryptedAlpha  = ''
    
    for j in range(len(alpha)):
        encryptedAlpha += alpha[j:] + alpha[:j]
        for i in message:
            if i == ' ':
                attempt += ' '
            else:
                pos = alpha.index(i)
                letter = encryptedAlpha[pos]
                attempt += letter
        
        print('Crack with key ',encryptedAlpha[0], ':',  attempt)
        attempt = ''
        encryptedAlpha = ''
