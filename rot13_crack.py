# -*- coding: utf-8 -*-
"""
Created on 16th May 2021

Input:  Takes a string which has been encoded using ROT13
Returns a brute force series of strings to decrypt

@author: brendantuckerman
"""

def rot13Crack(message):
    alpha = 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@##$%^&*()-+'
    encryptedAlpha = ''
    decrypt = ''

    for i in range(len(alpha)):
        encryptedAlpha += alpha[i:] + alpha [:i]
        for m in message:
             if m == '  ':
                 decrypt  += ' '
             elif m not in alpha:
                decrypt += m
             else:
                key = encryptedAlpha.index(m)
                decrypt += alpha[key]
        
        print('Decrypting using key of ', encryptedAlpha[0] , ':', decrypt)  
        decrypt  = ''
        encryptedAlpha = ''
            

