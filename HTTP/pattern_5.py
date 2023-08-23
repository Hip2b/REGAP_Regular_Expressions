import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 3752 pcre:"/\x2ftahw\x3f[A-F0-9]{3,84}$/" 
Line 3753 pcre:"/\x2fkhc\x3f[A-F0-9]{3,84}$/" 
Line 3754 pcre:"/\x2fpser\x3f[A-F0-9]{3,84}(BBZ|BBY)/" 
"""

def generate_rand():
    selection = ["$", "(" + RandomFunctions.word_generate(3, "upper") + "|" +  RandomFunctions.word_generate(3, "upper") + ")"]
    return [RandomFunctions.word_generate(random.randint(3,4), "lower"), selection[random.randint(0,1)] ]

def regex(rand_var):    
    base = r"\x2f"
    base += rand_var[0]
    base += r"\x3f[A-F0-9]{3,84}"
    base += rand_var[1]
    
    return base

def input(rand_var, error_num):
    content = "|2f|"
    error_num = math.fmod(error_num - 1, 3)

    if (error_num == 0):
        content += "error"
    content += rand_var[0]
    content += "|3f|"
    if (error_num == 1):
        content += "\n"
    content += RandomFunctions.word_generate(random.randint(3,84), "", "ABCDEF0123456789")
    
    if (not rand_var[1] == "$"):
        choice = 1 + (random.randint(0,1) * 4)
        content += rand_var[1][choice:choice + 3]
    
    if (error_num == 2):
        content += "error"

    return content

def scale():
    return 3