# -*- coding: utf-8 -*-
"""
Created on 16th May 2021

ROT13 Encryptor
    Input: message (string)
            key (single letter indicating the key )
    Returns string encoded using ROT13 where the cypher shifts 13 places

@author: brendantuckerman
"""

def rot13(message, key):
    alpha = 'ABCDEFGHIJKLMONPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@##$%^&*()-+'
    encryptedAlpha = ''
    encryptedMes = ''
    
    lock = alpha.index(key) +13
    encryptedAlpha += alpha[lock:] + alpha [:lock]
    
    for m in message:
        if m == '  ':
            encryptedMes  += ' '
        elif m not in alpha:
                encryptedMes += m
        else:
            j = alpha.index(m)
            encryptedMes += encryptedAlpha[j]
    
    return encryptedMes


