import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 2989 pcre:"/\)\r\nHost\x3a\x20[\d\x2e]{7,15}\r\nConnection\x3a\x20Keep\x2dAlive\r\n\r\n$/" 
Line 3028 pcre:"/\)\r\nHost\x3a\x20[a-z\d\x2e\x2d]{6,32}\r\nCache\x2dControl\x3a\x20no\x2dcache\r\n\r\n$/" 
Line 2695 pcre:"/\)\r\nHost\x3a\x20[a-z0-9\x2d\x2e]+\r\n(Cache\x2dControl|Pragma)\x3a\x20no-cache\r\n\r\n$/" 
Line 2588 pcre:"/\r\nHost\x3a\x20[a-z0-9\x2d\x2e]+\.com\x2d[a-z0-9\x2d\x2e]+(\x3a\d{1,5})?\r\n/i" 

Line 2530 pcre:"/\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2Einfo\r\n/i" 
Line 2818 pcre:"/\r\nHost\x3A\s+[^\r\n]*?[bcdfghjklmnpqrstvwxyz]{5,}[^\r\n]*?\x2Ebiz\r\n/i" 
"""

def generate_rand():
    ret_arr = [RandomFunctions.word_generate(10, "letters", "_")]
    first_addon = random.randint(1,4)
    second_addon = random.randint(1,4)
    if (first_addon == 1):
        ret_arr.append(r"(\x5f|%5f)")
        second_addon = 1
    
    if (second_addon == 1):
        if (random.randint(1,2) == 1):
            ret_arr.append(RandomFunctions.word_generate(3, "lower"))
        else:
            first_word = RandomFunctions.word_generate(random.randint(5,9),"upper")
            second_word = RandomFunctions.word_generate(random.randint(5,9),"upper")
            ret_arr.append("(" + first_word + "|" + second_word + ")")
    
    return ret_arr

def regex(rand_var):    
    base = r"[?&]"
    for x in rand_var:
        base += x
    base += r"=[^&]*?%26"
    
    return base

def input(rand_var, error_num):
    selection = ["?", "&"]
    content = selection[random.randint(0,1)]
    error_num = math.fmod(error_num - 1, 2)

    content += rand_var[0]
    if (error_num == 0):
        content += "errorOne"
    
    if (len(rand_var) > 1):
        split = rand_var[1].find("|")
        if (split > -1):
            selection = [rand_var[1][1:split], rand_var[1][split + 1:-1]]
            content += selection[random.randint(0,1)]

            split = rand_var[2].find("|")
            if (split > -1):
                selection = [rand_var[2][1:split], rand_var[2][split + 1:-1]]
                content += selection[random.randint(0,1)]
            else:
                content += rand_var[2]
        else:
            content += rand_var[1]
    
    if (error_num == 1):
        content += "&"
    content += RandomFunctions.word_generate(random.randint(0,5), "num_letter")

    content += "%26"

def scale():
    return 8