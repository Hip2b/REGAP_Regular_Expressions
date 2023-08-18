import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Legitimate examples of regular expressions of this type found in the snort community rules file
Line 3977 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)jndi(%(25)?3a|\x3a)/i" 
Line 3981 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)lower(%(25)?3a|\x3a)/i" 
Line 3983 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)upper(%(25)?3a|\x3a)/i" 
Line 3985 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)jndi(%(25)?3a|\x3a)/i" 
Line 3986 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)lower(%(25)?3a|\x3a)/i" 
Line 3987 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)upper(%(25)?3a|\x3a)/i" 
Line 3988 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)jndi(%(25)?3a|\x3a)/i" 
Line 3989 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)upper(%(25)?3a|\x3a)/i" 
Line 3990 pcre:
"/(%(25)?24|\x24)(%(25)?7b|\x7b)lower(%(25)?3a|\x3a)/i" 
"""

def generate_rand():
    return RandomFunctions.word_generate(random.randint(4,5), "lower")

def regex(rand_var):    
    base = r"(%(25)?24|\x24)(%(25)?7b|\x7b)"
    base += rand_var
    base += r"(%(25)?3a|\x3a)"
    
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)

    content += RandomFunctions.word_generate(random.randint(0,4),"lower")

    if (random.randint(1,2) == 1):
        content += "%"
        if (error_num == 0):
            content += "trash"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "24"
    else:
        if (error_num == 0):
            content += "trash"
        else: 
            content += "|24|"

    if (random.randint(1,2) == 1):
        content += "%"
        if (error_num == 1):
            content += "garbage"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "7b"
    else:
        if (error_num == 1):
            content += "garbage"
        content += "|7b|"

    content += rand_var

    if (error_num == 2):
        content += "rubbish"

    if (random.randint(1,2) == 1):
        content += "%"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "3a"
    else:
        content += "|3a|"
    
    return content

def scale():
    return 9