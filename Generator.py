import getopt
import importlib
import sys

category_type = "SMTP"
generation_type = ""
total_regs = 0
file_rules = 10
input_rate = 5

regex_text = "testRegex.txt"
input_text = "testInput.txt"

try:
    opts, args = getopt.getopt(sys.argv[1:], ":", 
                               ["category=", "regexes=", "inputs_per_reg=", "regexes_file=", "inputs_file="])  
except:
    exit()

for opt, arg in opts:
    if opt in ["--category"] :    
        category_type = str(arg)
    elif opt in ["--inputs_file"]:
        input_text = str(arg)
    elif opt in ["--regexes_file"]:
        regex_text = str(arg)
    elif opt in ["--regexes"]:
        if (int(arg) > 0):
            total_regs = int(arg)
        else:
            print("invalid regexes num")
            exit()
    elif opt in ["--inputs_per_reg"]:
        if (int(arg) > 0):
            input_rate = int(arg)
        else:
            print("invalid inputs_per_reg num")
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
    file_rules = 42
if (category_type == "HTTP"):
    file_rules = 20

for x in range(6):
    pattern_module = importlib.import_module(str(category_type) + ".pattern_" + str(x + 1))

    reps_decimal = total_regs * (pattern_module.scale()/file_rules)
    reps = int(round(reps_decimal, 0))
    for n in range(reps):
        seed = pattern_module.generate_rand()
        regex.write(pattern_module.regex(seed) + "\n")

        for i in range(input_rate):
            input.write(pattern_module.input(seed, i) + "\n")

regex.close()
input.close()