import random
import string
import getopt
import sys

#Regular Expression Generation Achieved through Patterns
#REGAP
reps = 1
"""
try:
    opts, args = getopt.getopt(sys.argv[1:], ":", ["num_regs="])  

    for opt, arg in opts:
        if opt in ["--num_regs"] :    
            reps = int(arg)
    
except:
    
    print("")
    print("This program requires you to put arguments onto the command line to specify the files that \n", 
          "you are using as inputs into your regular expression and the files containing your regular expressions\n",
          "themselves. Type --input (input file name) to choose an input file and --regex (regex file name)\n",
          "to choose a fil with your regular expressions.")
    exit()
    
"""
def word_generate(num_chars, case = ""):
    word = ""
    if (case == "lower"):
        alphabet = string.ascii_lowercase
    elif (case == "upper"):
        alphabet = string.ascii_uppercase
    elif (case == "start_upper"):
        word += random.choice(string.ascii_uppercase)
        alphabet = string.ascii_lowercase
        num_chars -= 1
    else:
        return "invalid u silly"

    for x in range(num_chars):
        word += random.choice(alphabet)

    return word

def random_presets():
    rand_regexes = [repr("/name=[^\r\n]*?\.(mim|uue|uu|b64|bhx|hqx|xxe)/ims"),
                   repr("/(name|id|number|total|boundary)=\s*[^\r\n\x3b\s\x2c]{300}/ims"),
                   repr("/name=\s*[^\r\n\x3b\s\x2c]{300}/ims"),
                   repr("/^\s*Content-Type\s*\x3A\s*[^\r\n]{300}/im" ),
                   repr("/^\s*Content-Encoding\s*\x3A\s*[^\r\n]{300}/im"),
                   repr("/^\s*Content-Transfer-Encoding\s*\x3A[^\n]{100}/im")]
    
    rand_pre = random.randint(0,len(rand_regexes - 1))

    print(rand_regexes[rand_pre])
