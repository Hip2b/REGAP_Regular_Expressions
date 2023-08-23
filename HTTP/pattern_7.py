import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 3469 pcre:"/[?&]host_name=[^&]*?%26/i" 
Line 3457 pcre:"/[?&]ping_IPAddr=[^&]*?%26/i" 
Line 3529 pcre:"/[?&]pingAddr=[^&]*?%26/i" 
Line 3469 pcre:"/[?&]host_name=[^&]*?%26/i" 
Line 3665 pcre:"/[?&]url=[^&]*?%26/i" 
Line 3661 pcre:"/[?&]path=[^&]*?%26/i" 
Line 3621 pcre:"/[?&]SMB(\x5f|%5f)(LOCATION|USERNAME)=[^&]*?%26/i" 
Line 3616 pcre:"/[?&]ping(\x5f|%5f)ip=[^&]*?%26/i" 

Line 3437 pcre:"/[?&]arg=[^&]*?%26/i" 
"""

def generate_rand():
    ret_arr = [RandomFunctions.word_generate(random.randint(4,12), "letters", "_")]
    first_addon = random.randint(1,4)
    second_addon = random.randint(1,4)
    if (first_addon == 1):
        ret_arr.append(r"(\x5f|%5f)")
        second_addon = 1
    else:
        ret_arr.append("")
    
    element_two = ""
    if (second_addon == 1):
        if (random.randint(1,2) == 1):
            element_two = RandomFunctions.word_generate(random.randint(2,3), "lower")
        else:
            first_word = RandomFunctions.word_generate(random.randint(5,9),"upper")
            second_word = RandomFunctions.word_generate(random.randint(5,9),"upper")
            element_two = [first_word, second_word]
    
    ret_arr.append(element_two)
    
    return ret_arr

def regex(rand_var):    
    base = r"[?&]"
    for x in rand_var:
        if (isinstance(x,list)):
            base += "(" + x[0] + "|" + x[1] + ")"
        else:
            base += x
    base += r"=[^&]*?%26"
    
    return base

def input(rand_var, error_num):
    content = ""
    content += RandomFunctions.word_generate(random.randint(0,4), "letters")
    
    selection = ["?", "&"]
    content += selection[random.randint(0,1)]
    error_num = math.fmod(error_num - 1, 3)

    content += rand_var[0]
    if (error_num == 0):
        content += "errorOne"
    
    if (not rand_var[1] == ""):
        selection = ["|5f|", r"%5f"]
        content += selection[random.randint(0,1)]

    if (error_num == 1):
        content += "errorTwo"

    if (isinstance(rand_var[2], list)):
        content += rand_var[2][random.randint(0,1)]
    else:
        content += rand_var[2]

    if (error_num == 2):
        content += "&"
    content += "=" + RandomFunctions.word_generate(random.randint(0,5), "num_letter")

    content += "%26"

    return content

def scale():
    return 8