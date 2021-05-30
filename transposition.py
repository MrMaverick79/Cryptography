# -*- coding: utf-8 -*-
"""
Created on 17th May 2021

Transposition cypher

    Message is encoded using position in array and then returned based
    on their position in their array (0th element followed by 1st element etc).
        
    So 'Secret', 3 would encode as:
        
        S e c 
        r e t
        
    and return 
    
    'Sreect'
    
    Takes a string as an argument 
    Take array length (int < length of message)
    Returns a message encrypted in an array determined by length

@author: brendantuckerman
"""
# TODO
# Add in word as instead of length. The len of this word is the length
# Code is then sorted by alpha based on the word
#  Should make it much harder to crack

def transpo(message, key):
    "Returns a list of lists based on the \
    length provided. "
    length = len(key)
    arr = []
    new_l = []
    message_list = []
    
    for m in message:
        message_list.append(m)
    
    
    while len(message_list) > 0:
        try:
            for l in range(0, length):
                new_l.append(message_list[0])
                message_list.pop(0)
                
            arr.append(new_l)   
            new_l = []
        except:
            for l in range (len(message_list)):
                new_l.append(message_list[l])
                message_list.pop(0)
            arr.append(new_l)
            new_l = []
            
    return arr


def encodeTranspo(message, key):
    " Returns an encoded message using positon in array \
        length should be she same as in transpo"
    
    length = len(key)
    encode = ''
    j = 0
    #need to make each list same length
    for i in message:
        
        while len(i) < length:
                i.append(' ')
        #print(i)
    
    while j < length:
        for i in range(len(message)):
               encode += message[i][j]
        j += 1
    
    #TODO
    # need to sort the key inot alpha...then change each of the lists
    # to do the same
    #split key? enumerate, then sort?
    
    print(encode)
        
        
    

#test
key = 'cab'
code  = transpo('Now I should be able to encode anything!', key)
encodeTranspo(code, key)

        