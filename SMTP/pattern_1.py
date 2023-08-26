import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Legitimate examples of regular expressions of this type found in the snort community rules file
(by the way the line numbers listed here in the smtp folder are one smaller than their actual line numbers 
in snort3 communtiy.rules, this mistake wasn't made for the http folders or the sql folder but its present in the 
patterns in smtp)
#Line 2334 
filename=[^\n]*\x2eemf
#Line 2341 
filename=[^\n]*\x2epdf
#Line 2351 
filename=[^\n]*\x2exsl 
#Line 2354 
filename=[^\n]*\x2exslt
#Line 2360 
filename=[^\n]*\x2epaq8o
#Line 2370 
filename=[^\n]*\x2exml
#Line 2373 
filename=[^\n]*\x2epng
#Line 2376 
filename=[^\n]*\x2esmi
#Line 2378
filename=[^\n]*\x2esami
#Line 2381 
filename=[^\n]*\x2eani
#Line 2384 
filename=[^\n]*\x2ejpg 
#Line 2386
filename=[^\n]*\x2ejpeg
#Line 2388 
filename=[^\n]*\x2epjpeg
#Line 2390 
filename=[^\n]*\x2ejpe
#Line 2392
filename=[^\n]*\x2ejif
#Line 2394 
filename=[^\n]*\x2ejfi
#Line 2396
filename=[^\n]*\x2ertf
#Line 2431 
filename=[^\n]*\x2ezip
#Line 2433 
filename=[^\n]*\x2eexe 
#Line 2437 
filename=[^\n]*\x2exm
"""

def generate_rand():
    return RandomFunctions.word_generate(random.randint(3,5), "lower")

def regex(rand_var):    
    base = r"filename=[^\n]*\x2e"
    base += rand_var
    
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 2)

    for extra_lets in range(random.randint(0,5)):
        content += random.choice(string.ascii_letters) 
    content += "filename="   
    for extra_lets in range(random.randint(0,5)):
        content += random.choice(string.ascii_letters) 
    
    if (error_num == 0):
        content += "|0A|"
    content += "|2e|"

    if (error_num == 1):
        content += RandomFunctions.word_generate(random.randint(4,7), "lower")     
    else:
        content += rand_var
    
    content += RandomFunctions.word_generate(random.randint(0,5), "lower")     

    return content

def scale():
    return 20