from modules.RandomFunctions import word_gen
import random
import string
import math
"""
Line 1930,1932-1936,1939-1950,1953,1955-1965,1967,1971-1974,1977,1981-1984,1986,1990-2001,2005,2009-2012,2015,
2017,2019,2021,2027,2028,2030,2031,2048,2050,2052,2053,2055,2056,2058,2059,2075,2079-2086,2089-2098,2101,2102,
2105,2106,2108,2117,2139 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*gname[\r\n\s]*=>[\r\n\s]*\2|gname\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 1966 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*userid[\r\n\s]*=>[\r\n\s]*\2|userid\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 

Line 2125,2128,2131 pcre:
"/((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*sname[\r\n\s]*=>[\r\n\s]*\2|sname\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))/is" 
"""

def generate_rand():
    return word_gen("a-z", 5, 10)

def regex(rand_var):    
    base = r"((\w+)[\r\n\s]*\x3a=[\r\n\s]*(\x27[^\x27]{1075,}\x27|\x22[^\x22]{1075,}\x22)[\r\n\s]*\x3b.*"
    base += rand_var
    base += r"[\r\n\s]*=>[\r\n\s]*\2|"
    base += rand_var
    base += r"\s*=>\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,})|\(\s*(\x27[^\x27]{1075,}|\x22[^\x22]{1075,}))"
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 2)
    low_lim = 1075
    rand = random.randint(0,2)
    x27 = "|27|"
    x22 = "|22|"

    if (error_num == 0):
        low_lim = 500
    elif(error_num == 1):
        x27 = "error"
        x22 = "alsoError"

    if (rand == 2):
        starter = word_gen("a-zA-Z",1, 10)
        content += starter
        content += word_gen("\r\n ",0,4) + "|3A|=" + word_gen("\r\n ",0,4)
        if (random.randint(0,1) == 1):
            content += x27 + word_gen("A-z",low_lim, low_lim + 25) + x27
        else:
            content += x22 + word_gen("A-z",low_lim, low_lim + 25) + x22
        content += word_gen("\r\n ",0,4) + "|3b|" + word_gen("a-Z",0,5)
        content += rand_var
        content += word_gen("\r\n ",0,4) + "=>" + word_gen("\r\n ",0,4)
        content += starter    
    elif (rand == 1):
        content += rand_var
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
    return 112