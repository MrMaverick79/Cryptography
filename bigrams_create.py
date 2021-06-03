# -*- coding: utf-8 -*-
"""
Created on 3rd June 2021

    Produces a lists of bigrams in txt from source
    creates a txt file with list of occurence

@author: brendantuckerman
"""
import string
import time
alpha = string.ascii_lowercase

def bigrams(file):
    """ creates bigrams.txt which counts the occurence 
    of each letter. Changes all caps to lower. only counts alpha"""
    
    with open(file, 'r', encoding = 'ISO-8859-1') as f: 
    #might need to change encoding to 'utf-8' for other files
        
        contents = f.read() 
        contents.lower()
        for i in alpha:
            for j in alpha:
                bi = i + j
                c = contents.count
                c = contents.count(bi) #counts each alpha
       
                with open('bigrams.txt', 'a') as file_object: #write results to file
                    file_object.write(bi)
                    file_object.write (':  ')
                    file_object.write(str(c))
                    file_object.write("\n")
                    file_object.close()
               
    f.close()

#test
start = time.time()
file = 'swanns_way.txt' #this is the source txt. 
bigrams(file) 
end = time.time()
print('Finished in ',  end-start, ' seconds.')
        
