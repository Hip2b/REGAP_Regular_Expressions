from modules.RandomFunctions import word_gen
import random
import string
import math

"""
Line 1951,1952,1968,1969,1975,1976,1980,1985,1987,1988,2003,2004,2006,2008,2013,2018,2020,2024,2025,2054,2057,
2078,2087,2088,2099,2100,2103,2104,2107,2118-2121 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(sname|oname)[\r\n\s]*=>[\r\n\s]*\2|(sname|oname)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2014,2062,2064,2066,2126,2130 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gname|gowner)[\r\n\s]*=>[\r\n\s]*\2|(gname|gowner)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 
 
Line 2029,2032,2067,2076,2133,2135-2138 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gname|gowner)[\r\n\s]*=>[\r\n\s]*\2|(gname|gowner)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*((\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*){2}(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 1954,2060,2122 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gname|gowner)[\r\n\s]*=>[\r\n\s]*\2|(gname|gowner)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*((\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*){3}(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2132,2065,2016 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gname|gowner)[\r\n\s]*=>[\r\n\s]*\2|(gname|gowner)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*((\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*){4}(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2073 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(sname|oname|gname)[\r\n\s]*=>[\r\n\s]*\2|(sname|oname|gname)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 1970 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gowner|gname)[\r\n\s]*=>[\r\n\s]*\2|(gowner|gname)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 1979 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(gname|fname)[\r\n\s]*=>[\r\n\s]*\2|(gname|fname)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*((\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*){4}(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2022 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(object_type|user_name)[\r\n\s]*=>[\r\n\s]*\2|(object_type|user_name)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2023 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*(refresh_template_name|user_name)[\r\n\s]*=>[\r\n\s]*\2|(refresh_template_name|user_name)\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 
"""


def generate_rand():
    ret_arr = []
    for x in range(random.randint(2,3)):
        ret_arr.append(word_gen("a-z", 5, 10))
    return [ret_arr, random.randint(1,4)]

def regex(rand_var):    
    base = r"((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*("
    for rand in rand_var[0]:
        base += rand + "|"
    base = base[:-1] + ")"

    base += r"[\r\n\s]*=>[\r\n\s]*\2|("
    for rand in rand_var[0]:
        base += rand + "|"
    base = base[:-1]

    base += r")\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*"
    if (int(rand_var[1]) > 1):
        base += r"((\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*){" 
        base += str(rand_var[1])
        base += r"}(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))"
    else: 
        base += r"\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]*\x27|\x22[^\x22]+\x22)\s*,\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))" 
    
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 2)
    error_num = -1
    low_lim = 1075
    rand = random.randint(0,3)
    x27 = "|27|"
    x22 = "|22|"

    if (error_num == 0):
        low_lim = 500
    elif (error_num == 1):
        x27 = "error"
        x22 = "alsoError"
    
    if (rand == 3):
        content += "(" + word_gen(" ", 0, 5)
        for x in range(rand_var[1]):
            if (random.randint(0,1) == 1):
                content += x27 + word_gen("A-z",0,25) + x27
            else:
                content += x22 + word_gen("A-z",0,25) + x22
            content += word_gen(" ", 0, 5) + "," + word_gen(" ", 0, 5)
        
        if (random.randint(0,1) == 1):
            content += x27 + word_gen("A-z",low_lim, low_lim + 25) 
        else:
            content += x22 + word_gen("A-z",low_lim, low_lim + 25) 
        
    elif (rand == 2):
        starter = word_gen("a-zA-Z",1, 10)
        content += starter
        content += word_gen("\r\n ",0,4) + "|3a|=" + word_gen("\r\n ",0,4)
        if (random.randint(0,1) == 1):
            content += x27 + word_gen("A-z",low_lim, low_lim + 25) + x27
        else:
            content += x22 + word_gen("A-z",low_lim, low_lim + 25) + x22
        content += word_gen("\r\n ",0,4) + "|3b|" + word_gen("a-Z",0,5)

        ran_word = random.randint(0,len(rand_var[0]) - 1)
        content += rand_var[0][ran_word]

        content += word_gen("\r\n ",0,4) + "=>" + word_gen("\r\n ",0,4)
        content += starter    
    elif (rand == 1):
        ran_word = random.randint(0,len(rand_var[0]) - 1)
        content += rand_var[0][ran_word]
        content += word_gen(" ", 0,4) + "=>" + word_gen(" ", 0, 4)
        if (random.randint(0,1) == 1):
            content += x27 + word_gen("A-z",low_lim, low_lim + 25) 
        else:
            content += x22 + word_gen("A-z",low_lim, low_lim + 25) 
    else:
        content += "(" + word_gen(" ", 0, 5)
        if (random.randint(0,1) == 1):
            content += x27 + word_gen("A-z",low_lim, low_lim + 25) 
        else:
            content += x22 + word_gen("A-z",low_lim, low_lim + 25) 
    
    return content
 
def scale():
    return 59