import modules.RandomFunctions as RandomFunctions
import random
import string
import math
"""
#Line 2292 
^\s*Content-Type\s*\x3A\s*[^\r\n]{300}
#Line 2293 
^\s*Content-Encoding\s*\x3A\s*[^\r\n]{300}
#Line 1547 
^\s*Content-Transfer-Encoding\s*\x3A[^\n]{100}
"""
def generate_rand():
    rand_string = "Content"
    for x in range(random.randint(1,2)):
        rand_string += "-" + RandomFunctions.word_generate(random.randint(4,8), "start_upper")

    return [rand_string, random.randint(0,1), 50 * random.randint(2,6)]

def regex(rand_vars):
    base = r"^\s*"
    two_ops = [r"\s*[^\r", r"[^"]
    base += rand_vars[0]   
    base += r"\s*\x3A" + two_ops[rand_vars[1]] + r"\n]{" 
    base += str(rand_vars[2]) + "}"
    return base

def input(rand_vars, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)
    chars_num = rand_vars[2]
    alphabet = string.ascii_letters

    if (error_num == 0):
        content += "q"
    for x in range(random.randint(0,5)):
        content += " "

    content += rand_vars[0]
    content += "\x3A"

    if (error_num == 1):
        if (rand_vars[1] == 0):
            content += "x|0D|"
        elif(rand_vars[1] == 1):
            content += "|0A|"
    
    if (error_num == 2):
        chars_num -= 50
    
    for x in range(chars_num):
        content += random.choice(alphabet)

    return content

def scale():
    return 3