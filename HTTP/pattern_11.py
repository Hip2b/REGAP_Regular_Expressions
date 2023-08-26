from modules.RandomFunctions import word_gen
import random
import string
import math

"""
Line 2531 pcre:"/\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2Einfo\r\n/i" 
Line 2819 pcre:"/\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2Ebiz\r\n/i" 
"""

def generate_rand():
    return word_gen("a-z", 3, 5)

def regex(rand_var):    
    base = r"\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2E"
    base += rand_var
    base += r"\r\n"
    
    return base

def input(rand_var, error_num):
    content = word_gen("a-z A-Z 0-9", 0, 20)
    content += "|0D 0A|Host|3A|"
    error_num = math.fmod(error_num - 1, 3)

    if (error_num != 0):
        content += word_gen(" /09", 1, 5)
    content += word_gen("a-zA-Z0-9", 0, 8)
    
    selection = "b-df-hj-np-tv-z"
    if (error_num == 1):
        selection = "a-zA-Z"

    if (error_num != 2):
        content += word_gen(selection, 5, 10)
    
    content += word_gen("a-zA-Z0-9", 0, 8)
    content += "|2E|" + rand_var + "|0D 0A|"
    return content

def scale():
    return 2