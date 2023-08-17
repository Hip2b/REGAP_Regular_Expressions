import modules.RandomFunctions as RandomFunctions
import random
import string
import math
"""
#Line 992 
^HELO\s[^\n]{500}
#Line 993
^ETRN\s[^\n]{500}
#Line 345 
^HELP\s[^\n]{500} 
#Line 1614
^EXPN[^\n]{255}
#Line 1615
^VRFY[^\n]{255}
"""
def generate_rand():
    return [RandomFunctions.word_generate(4, "upper"), random.randint(0,1), 50 * (random.randint(6,10)) ]

def regex(rand_vars):
    base = "^" + rand_vars[0]
    space_or_not = [r"\s", ""]

    base += space_or_not[rand_vars[1]]
    base += r"[^\n]{" + str(rand_vars[2]) + "}"
    return base

def input(rand_vars, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 4)
    space_or_not = [" ", ""]
    space_num = rand_vars[1]
    alphabet = string.ascii_letters + " @"
    num_chars = rand_vars[2]

    if (error_num == 0):
        content += " "
    content += rand_vars[0]
    if (error_num == 1):
        space_num = abs(1 - space_num)
    content += space_or_not[space_num]
    if(error_num == 2):
        content += "|0A|"
    if(error_num == 3):
        num_chars -= 5
    for x in range(num_chars):
        content += random.choice(alphabet)  

    return content

