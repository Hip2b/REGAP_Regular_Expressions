import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 2778 pcre:
"/\/(?:[^\/]+?\/[a-z]{2,24}|closest\/[a-z0-9]{15,25})\.php\?[ab10]+=[ab10]+&[ab10]+=[ab10]+$/" 
Line 2782 pcre:
"/\/(?:[^\/]+?\/[a-z]{2,24}|closest\/[a-z0-9]{15,25})\.php\?[ab10]+=[ab10]+&[ab10]+=[ab10]+&[ab10]+=[ab10]+&[ab10]+=[ab10]+&[ab10]+=[ab10]+$/" 
"""

def generate_rand():
    ret_arr = []
    for x in range(random.randint(6,12)):
        if (random.randint(1,2) == 1):
            ret_arr.append("[ab10]+=")
        else:
            ret_arr.append("[ab10]+&")
    return ret_arr

def regex(rand_var):    
    base = r"\/(?:[^\/]+?\/[a-z]{2,24}|closest\/[a-z0-9]{15,25})\.php\?"
    for x in rand_var:
        base += x
    
    return base

def input(rand_var, error_num):
    content = "/"
    error_num = math.fmod(error_num - 1, 2)

    if (error_num == 0):
        content += "////"

    if (random.randint(1,2) == 1):
        if (random.randint(1,2) == 1):
            content += RandomFunctions.word_generate(random.randint(1,5),"num_letter")
        content += "/"

        rand_num = random.randint(2,24)
        if (error_num == 1):
            rand_num = 25

        content += RandomFunctions.word_generate(rand_num, "lower")
    else:
        content += "closest/"
        rand_num = random.randint(15,25)
        if (error_num == 1):
            rand_num = 29
        content += RandomFunctions.word_generate(rand_num, "num_lower")
        
    content += ".php?"

    for x in rand_var:
        content += RandomFunctions.word_generate(random.randint(1,5),"filler","ab10")

        if(x == "[ab10]+="):
            content += "="
        else:   
            content += "&"
        
    return content

def scale():
    return 3