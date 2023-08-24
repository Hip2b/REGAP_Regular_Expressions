import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""

Line 3459 pcre:"/[?&]ping_IPAddr=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3471 pcre:"/[?&]host_name=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3529 pcre:"/[?&]pingAddr=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3616 pcre:"/[?&]ping_ip=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3621 pcre:"/[?&]SMB_(LOCATION|USERNAME)=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3661 pcre:"/[?&]path=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3665 pcre:"/[?&]url=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3682 pcre:"/[?&]command_data=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 


kind of :
Line 3606 pcre:"/[?&]ping_(ip|size|times)=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)/i" 
Line 3437 pcre:"/[?&]arg=[^&]*?([\x60\x3b\x7c]|\x24\x28)/i" 
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
    base += r"=[^&]*?([\x60\x3b\x7c]|[\x3c\x3e\x24]\x28)"

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

    if (random.randint(1,2) == 1):
        selection = ["|60|","|3b|", "|7c|"]
    else:
        selection = ["|3c 28|", "|3e 28|","|24 28|"]
    
    content += selection[random.randint(0,2)]

    return content

def scale():
    return 8