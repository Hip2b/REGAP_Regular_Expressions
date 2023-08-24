import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 2901 pcre:"/^[a-z\d\x2f\+\x3d]{10,98}$/i" 
Line 2908 pcre:"/^[a-z\d\x2b\x2f\x3d]{48,256}$/i" 
Line 3111 pcre:"/[a-z\d\x2f\x2b\x3d]{100}/AGi" 
Line 3112 pcre:"/[a-z\d\x2f\x2b\x3d]{100}/AGi" 
Line 3162 pcre:"/[a-z\d\x2f\x2b\x3d]{100,300}/i" 
"""

def generate_rand():
    ret_arr = ["", "", 0]
    if (random.randint(0,1) == 1):
        ret_arr[0] = "^"
    if (random.randint(0,1) == 1):
        ret_arr[1] += "$"
    rand_param = random.randint(10,150)
    ret_arr[2] = rand_param
    if (random.randint(0,1) == 1):
        ret_arr.append(random.randint(rand_param + 1, 350))
    return ret_arr

def regex(rand_var):  
    base = rand_var[0]  
    base += r"[a-z\d\x2f\x2b\x3d]{" + str(rand_var[2])
    if (len(rand_var) == 4):
        base += "," + str(rand_var[3])
    base += r"}"
    base += rand_var[1]

    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 1)

    param_one = rand_var[2]
    param_two = param_one
    if (len(rand_var) == 4):
        param_two = rand_var[3]

    if (error_num == 0):
        param_one = int(rand_var[2]/3)
        param_two = int(rand_var[2]/2)
    
    if (error_num == 1):
        param_one = param_two + 5
        param_two = param_two + 20

    content = RandomFunctions.word_generate(random.randint(param_one, param_two), "num_lower", r"=+/")

    return content

def scale():
    return 5