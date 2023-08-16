import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
#Line 1617 
^SEND FROM\x3a\s+[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}
#Line 1619
^SAML FROM\x3a\s+[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}
#Line 1621
^SOML FROM\x3a\s+[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}
#Line 1623
^MAIL FROM\x3a\s+[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}
#Line 1625 
^RCPT TO\x3a\s*[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}
"""
def generate_rand():
    options = ["TO", "FROM"]
    return [RandomFunctions.word_generate(4, "upper"), options[random.randint(0,1)]]


def regex(rand_vars):
    base = "^"
    base += rand_vars[0]
    base += " " + rand_vars[1]
    base += r"\x3a\s+[\w\s@\.]{200,}\x3b[\w\s@\.]{200,}\x3b[\w\s@\.]{200}"

    return base

def input(rand_vars, error_num):
    content = rand_vars[0] +" " + rand_vars[1] + "\x3a"
    char_choices = string.ascii_letters + " @"
    error_num = math.fmod(error_num - 1, 3)
    rand_spaces = random.randint(1,5)
    rand_words = random.randint(200,230)
    rand_chars = 200
 
    if (error_num == 0):
        rand_spaces -= rand_spaces
    if (error_num == 1):
        rand_words = random.randint(150,198)
    if (error_num == 2):
        rand_chars = 170

    for x in range(rand_spaces):
        content += " "
    for b in range(rand_words):
        content += random.choice(char_choices)
    content += "\x3b"
    for b in range(rand_words):
        content += random.choice(char_choices)
    content += "\x3b"
    for b in range(rand_chars):
        content += random.choice(char_choices)

    return content
