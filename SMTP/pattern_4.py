import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
#Line 347
^expn\s+decode
#Line 348 
^expn\s+root
#Line 359
^vrfy\s+decode 
#Line 895
^vrfy\s+root
"""
def generate_rand():
    return [RandomFunctions.word_generate(4,"lower"),
            RandomFunctions.word_generate(6,"lower")]

def regex(rand_vars):
    base = "^"
    mid = r"\s+"
    
    base += rand_vars[0] 
    base += mid
    base += rand_vars[1]
    return base

def input(rand_vars, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)
    num_spaces = random.randint(1,6)
    first = rand_vars[0]

    if(error_num == 0):
        num_spaces = 0
    if(error_num == 1):
        content += " "
    if(error_num == 2):
        first = RandomFunctions.word_generate(4,"lower")

    content += first
    for x in range(num_spaces):
        content += " "
    content += rand_vars[1]

    return content