import getopt
import importlib
import sys

category_type = ""
generation_type = ""
repetions = 0

regex_text = "testRegex.txt"
input_text = "testInput.txt"

try:
    opts, args = getopt.getopt(sys.argv[1:], ":", ["category=", "amount=", "regexes_file=", "inputs_file="])  
except:
    exit()

for opt, arg in opts:
    if opt in ["--category"] :    
        category_type = str(arg)
    elif opt in ["--inputs_file"]:
        input_text = str(arg)
    elif opt in ["--regexes_file"]:
        regex_text = str(arg)
    elif opt in ["--amount"]:
        if (int(arg) > 0):
            repetions = int(arg)
        else:
            print("invalid num")
            exit()
    else:
        print("Invalid input on command line")
        exit()

regex = open(regex_text, "w")
input = open(input_text, "w")

"""
SMTP_patterns=[["pattern_1",3],["pattern_2",5],["pattern_3",1]]
default_num_rules = ....
scaling_factor = repetitions/default_num_rules
"""
if (category_type == "SMTP"):
    for x in range(2):
        pattern_module = importlib.import_module("SMTP." + "pattern_" + str(x + 1))
        seed = pattern_module.generate_rand()
        regex.write(pattern_module.regex(seed) + "\n")

        for i in range(repetions):
            input.write(pattern_module.input(seed, i) + "\n")

regex.close()
input.close()