# -*- coding: utf-8 -*-
"""
Created on 3rd June 2021

    Produces a lists of mono, bi, tri, and quadgrams in txt from source
    creates a txt file for each

@author: brendantuckerman
"""
import string
import time

alpha = string.ascii_lowercase

def monograms(file):
    """ creates monograms.txt which counts the occurence 
    of each letter. Changes all caps to lower. only counts alpha"""
    
    with open(file, 'r', encoding = 'ISO-8859-1') as f: #might need to change 
    # encoding to 'utf-8' for other files
        
        contents = f.read() 
        contents.lower()
        for i in alpha:
            c = contents.count(i) #counts each alpha
       
            with open('monograms.txt', 'a') as file_object: #write results to file
                file_object.write(i)
                file_object.write (':  ')
                file_object.write(str(c))
                file_object.write("\n")
                file_object.close()
               
    f.close()


#test
start= time.time()
file = 'swanns_way.txt' #this is the source txt. 
monograms(file)          
end = time.time()
print('Finished in ',  end-start, ' seconds.')