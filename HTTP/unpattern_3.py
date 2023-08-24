import modules.RandomFunctions as RandomFunctions
import random
import string
import math

"""
Line 3992 pcre:
"/%24%7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 3993 pcre:
"/\x24\x7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 3997 pcre:
"/%2524%257b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 3998 pcre:
"/%24\x7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 3999 pcre:
"/%2524\x7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 4000 pcre:
"/%24%257b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 4001 pcre:
"/\x24%7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 4002 pcre:
"/\x24%257b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
Line 4003 pcre:
"/%2524%7b.{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])/i" 
"""

def generate_rand():
    options = ["%24", "%25", "24", "7b", r"\x7b", r"\x24"]
    ret_string = ""
    for x in range(random.randint(1,4)):
        ret_string += options[random.randint(0,5)]
    return ret_string

def regex(rand_var): 
    base = ""   
    base += rand_var
    base += r".{0,200}(%(25)?24|\x24)(%(25)?7b|\x7b).{0,200}(%(25)?3a|\x3a)(%(25)?(27|2d|5c|22)|[\x27\x2d\x5c\x22])*([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}(%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])"
    
    return base

def input(rand_var, error_num):
    content = ""
    error_num = math.fmod(error_num - 1, 3)

    content += RandomFunctions.word_generate(random.randint(0,4), "lower")

    index = 0
    rand_list = list(rand_var)
    for x in rand_list:
        if(index < len(rand_list)):
            if(not rand_list[index] == "x"):
                content += rand_list[index]
            else:
                content += rand_list[index + 1] + rand_list[index + 2]
                index += 2
    
        index += 1
    
    if (error_num == 0):
        content += "|0A|"

    for x in range(random.randint(0,200)):
        content += random.choice(string.ascii_letters)

    if (random.randint(1,2) == 1):
        content += "%"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "24"
    else:
        content += "|24|"

    if (random.randint(1,2) == 1):
        content += "%"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "7b"
    else:
        content += "|7b|"

    start_range = 0
    end_range = 200
    if (error_num == 1):
        start_range = 201
        end_range = 220
    
    for x in range(random.randint(start_range,end_range)):
        content += random.choice(string.ascii_letters)
    
    if (random.randint(1,2) == 1):
        content += "%"
        if (random.randint(1,2) == 1):
            content += "25"
        content += "3a"
    else:
       content += "|3a|"
    
    selection = ["27", "2d", "5c", "22"]

    for x in range(random.randint(1,4)):
        if (random.randint(1,2) == 1):
            content += "%"
            if (random.randint(1,2) == 1):
                content += "25"
            content += selection[random.randint(0,3)]
        else:
            content += "|" +  selection[random.randint(0,3)] + "|"

    if (random.randint(1,2) == 1):
        selection = ["j", "n", "d", "i" "7d","3a", "2d"]

        if (random.randint(1,2) == 1):
            index = random.randint(0,3)
            if (index > 3):
                content += "|" + selection[index] + "|"
            else:
                content += selection[index]
        else:
            content += "%"
            if (random.randint(1,2) == 1):
                content += "25"
            content += selection[random.randint(1,3)]
    else:
        for x in range(random.randint(1,4)):
            content += "%"
            if (random.randint(1,2) == 1):
                content += "25"
            if(random.randint(1,2) == 1):
                content += "5c"
            else:
                content += "|5c|"
            content += "u00"
            variety = "abcdef1234567890"
            content += random.choice(variety) + random.choice(variety)
    
    if (random.randint(1,2)):
        selection = ["22", "27"]
        if (random.randint(1,2)):
            content += "%"
            if (random.randint(1,2)):
                content += "25"
            content += selection[random.randint(0,1)]
        else:
            content += "|" + selection[random.randint(0,1)] + "|"

    if (error_num == 2):
        content += "errorstuff"

    selection = ["3a", "7d", "j", "n", "d", "i"]
    if (random.randint(1,2)):
        content += "%"
        if (random.randint(1,2)):
            content += "25"
        content += selection[random.randint(0,1)]
    else:
        index = random.randint(0,2)
        if (index < 2):
            content += "|" + selection[index] + "|"
        else:
            content += selection[index]

    return content

#([jndi\x7d\x3a\x2d]|(%(25)?(7d|3a|2d))|(%(25)?5c|\x5c)u00[a-f0-9]{2}){1,4}
# (%(25)?(22|27)|[\x22\x27])?(%(25)?(3a|7d)|[\x3a\x7djndi])"
    

def scale():
    return 7