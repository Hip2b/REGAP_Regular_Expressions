import modules.RandomFunctions as RandomFunctions
import random
import string
import math


"""
Line 555 pcre:"/\x2ehtr([\?\x5c\x2f]|$)/ims" 
Line 1757 pcre:"/\x2eram?([\?\x5c\x2f]|$)/ims" 
Line 1758 pcre:"/\x2ermp([\?\x5c\x2f]|$)/ims" 
Line 1759 pcre:"/\x2ert([\?\x5c\x2f]|$)/ims" 
Line 1760 pcre:"/\x2erp([\?\x5c\x2f]|$)/ims" 
Line 1772 pcre:"/\x2eemf([\?\x5c\x2f]|$)/ims" 
Line 1773 pcre:"/\x2ewmf([\?\x5c\x2f]|$)/ims" 
Line 2299 pcre:"/\x2ertf([\?\x5c\x2f]|$)/ims" 
Line 2300 pcre:"/\x2epdf([\?\x5c\x2f]|$)/ims" 
Line 2301 pcre:"/\x2edoc([\?\x5c\x2f]|$)/ims" 
Line 2302 pcre:"/\x2ebmp([\?\x5c\x2f]|$)/ims" 
Line 2304 pcre:"/\x2ejpg([\?\x5c\x2f]|$)/ims" 
Line 2305 pcre:"/\x2ejpeg([\?\x5c\x2f]|$)/ims" 
Line 2306 pcre:"/\x2eexe([\?\x5c\x2f]|$)/ims" 
Line 2309 pcre:"/\x2epjpeg([\?\x5c\x2f]|$)/ims" 
Line 2311 pcre:"/\x2epng([\?\x5c\x2f]|$)/ims" 
Line 2312 pcre:"/\x2exml([\?\x5c\x2f]|$)/ims" 
Line 2315 pcre:"/\x2ezip([\?\x5c\x2f]|$)/ims" 
Line 2319 pcre:"/\x2esmi([\?\x5c\x2f]|$)/ims" 
Line 2333 pcre:"/\x2ejar([\?\x5c\x2f]|$)/ims" 
Line 2336 pcre:"/\x2edib([\?\x5c\x2f]|$)/ims" 
Line 2337 pcre:"/\x2esami([\?\x5c\x2f]|$)/ims" 
Line 2338 pcre:"/\x2ejpe([\?\x5c\x2f]|$)/ims" 
Line 2339 pcre:"/\x2ejif([\?\x5c\x2f]|$)/ims" 
Line 2340 pcre:"/\x2ejfif?([\?\x5c\x2f]|$)/ims" 
Line 2350 pcre:"/\x2exsl([\?\x5c\x2f]|$)/ims" 
Line 2353 pcre:"/\x2exslt([\?\x5c\x2f]|$)/ims" 
Line 2359 pcre:"/\x2epaq8o([\?\x5c\x2f]|$)/ims" 
Line 2380 pcre:"/\x2eani([\?\x5c\x2f]|$)/ims" 
Line 2436 pcre:"/\x2exm([\?\x5c\x2f]|$)/ims" 
Line 2858 pcre:"/\x2eair([\?\x5c\x2f]|$)/ims" 
"""

def generate_rand():
    return RandomFunctions.word_generate(random.randint(3,5), "num_letter")

def regex(rand_var):    
    base = r"\x2e"
    base += rand_var
    base += r"([\?\x5c\x2f]|$)"
    
    return base

def input(rand_var, error_num):
    content = "|2e|"
    error_num = math.fmod(error_num - 1, 3)

    if (error_num == 0):
        content += "error"
    content += rand_var

    if (error_num == 1):
        content += "error"
    
    selection = ["?", "|5c|", "|2f|", ""]

    if (error_num == 2):
        content += "error"

    content += selection[random.randint(0,3)]
    
    return content

def scale():
    return 15