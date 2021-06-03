# -*- coding: utf-8 -*-
"""
Created on 3rd June 2021

    Produces a lists of quadgrams in txt from source
    creates a txt file with list of occurence
    omits 0 instances
    also produces time taken

@author: brendantuckerman
"""
import string
import time
alpha = string.ascii_lowercase

def quadgrams(file):
    """ creates bigrams.txt which counts the occurence 
    of each letter. Changes all caps to lower. only counts alpha"""
    
    with open(file, 'r', encoding = 'ISO-8859-1') as f: 
    #might need to change encoding to 'utf-8' for other files
        
        contents = f.read() 
        contents.lower()
        for i in alpha:
            for j in alpha:
                for k in alpha:
                    for l in alpha:
                    
                        quad = i + j + k + l
                        
                        c = contents.count(quad) #counts each alpha
                        if c == 0: #lots of trigrams don't exist so no need to record
                            pass
                        else:
                            with open('quadgrams.txt', 'a') as file_object: #write results to file
                                file_object.write(quad)
                                file_object.write (':  ')
                                file_object.write(str(c))
                                file_object.write("\n")
                                file_object.close()
               
    f.close()

#test
start = time.time()
file = 'swanns_way.txt' #this is the source txt. 
quadgrams(file) 
end = time.time()
print('Finished in ',  end-start, ' seconds.')
        
