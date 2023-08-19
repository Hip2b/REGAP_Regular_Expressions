import getopt
import importlib
import sys

category_type = "SMTP"
generation_type = ""
total_regs = 0
file_rules = 0
input_rate = 5
num_patterns = 0

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

arbitrary_patterns_checked = 20
for x in range(arbitrary_patterns_checked):
    try:
        pattern_module = importlib.import_module(str(category_type) + ".pattern_" + str(x + 1))
    except:
        #whooops
        continue

    num_patterns += 1
    file_rules += pattern_module.scale()    

for x in range(num_patterns):
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