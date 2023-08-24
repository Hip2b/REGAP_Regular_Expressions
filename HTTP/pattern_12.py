from modules.RandomFunctions import word_gen
import random
import string
import math

"""
Line 1218 pcre:"/^Authorization\x3A\s*Basic\s+TERBUF9Bbm9ueW1vdXM6TGRhcFBhc3N3b3JkXzE=/ims" 
Line 1588 pcre:"/^Authorization\x3a(\s*|\s*\r?\n\s+)Basic\s+YWRtaW46cGFzc3dvcmQ/ims" 
Line 1852 pcre:"/^Authorization\x3a(\s*|\s*\r?\n\s+)Basic\s+=/ims" 
Line 1853 pcre:"/^Authorization\x3a(\s*|\s*\r?\n\s+)Basic\s+=/ims" 
"""

def generate_rand():
    ender = ["=", ""]
    choices = [ "", word_gen(10, 40, "a-zA-Z0-9")]
    selection = [r"\s*", r"(\s*|\s*\r?\n\s+)"]
    return [selection[random.randint(0,1)], choices[random.randint(0,1)] + ender[random.randint(0,1)]]

def regex(rand_var):    
    base = r"^Authorization\x3A"
    base += rand_var[0]
    base += r"Basic\s+"
    base += rand_var[1]
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)
    if (error_num == 0):
        content += word_gen(5, 5, "a-zA-Z")
    content += "Authorization|3A|"

    rand = random.randint(0,1)
    if (rand_var[0][0] == "("):
        rand = 0
    
    if (error_num == 1):
        content += "banana"
    
    content += word_gen(0, 5, "\s")
    if (rand == 1): 
        if (random.randint(0,1)):
            content += "\r"
        content += "\n" + word_gen(1, 5, "\s")

    content += "Basic"
    if (error_num != 2):
        content += word_gen(1, 5, "\s")
    content += rand_var[1]

    return content

def scale():
    return 4