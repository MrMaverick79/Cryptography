# -*- coding: utf-8 -*-
"""
Created on 3rd June 2021

    Produces a lists of trigrams in txt from source
    creates a txt file with list of occurence

@author: brendantuckerman
"""
import string
import time
alpha = string.ascii_lowercase

def trigrams(file):
    """ creates bigrams.txt which counts the occurence 
    of each letter. Changes all caps to lower. only counts alpha"""
    
    with open(file, 'r', encoding = 'ISO-8859-1') as f: 
    #might need to change encoding to 'utf-8' for other files
        
        contents = f.read() 
        contents.lower()
        for i in alpha:
            for j in alpha:
                for k in alpha:
                    
                    tri = i + j + k
                    c = contents.count
                    c = contents.count(tri) #counts each alpha
                    if c == 0: #lots of trigrams don't exist so no need to record
                        pass
                    else:
                        with open('trigrams.txt', 'a') as file_object: #write results to file
                            file_object.write(tri)
                            file_object.write (':  ')
                            file_object.write(str(c))
                            file_object.write("\n")
                            file_object.close()
               
    f.close()

#test
start = time.time()
file = 'swanns_way.txt' #this is the source txt. 
trigrams(file) 
end = time.time()
print('Finished in ',  end-start, ' seconds.')
        
