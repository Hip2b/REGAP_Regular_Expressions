import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Legitimate examples of regular expressions of this type found in the snort community rules file
Line 2673 pcre:
"/\/jorg\.html$/" 
Line 2674 pcre:
"/\/jlnp\.html$/" 
Line 2675 pcre:
"/\/jovf\.html$/" 
"""


def generate_rand():
    return RandomFunctions.word_generate(4, "lower")

def regex(rand_var):    
    base = r"\/"
    base += rand_var
    base += r"\.html$"
    
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)

    content += r"/"