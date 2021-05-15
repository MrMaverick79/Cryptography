# -*- coding: utf-8 -*-
"""
Created on 15th May 2021

Reverse Cypher: 
    Takes string as input
    Produces string in reverse as output

@author: brendantuckerman
"""

def revCypher(string):
    message = ''
    i = len(string)
    while i >= 1:
          message += string[i-1]
          i -= 1        
    return message

print(revCypher('This is a test'))