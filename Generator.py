import getopt
import importlib
import sys

category_type = ""
generation_type = ""
repitions = 0

try:
    opts, args = getopt.getopt(sys.argv[1:], ":", ["category=", "generation=", "amount="])  
except:
    
    exit()


for opt, arg in opts:
    if opt in ["--category"] :    
        category_type = str(arg)
    elif opt in ["--generation"]:
        generation_type = str(arg)
    elif opt in ["--amount"]:
        repitions = int(arg)
    else:
        print("Invalid input on command line")
        exit()

for i in range(repitions):
    if (category_type == "SMTP"):
        for x in range(6):
            pattern_module = importlib.import_module("SMTP." + "pattern_" + str(x + 1))
            seed = pattern_module.seed
            if (generation_type == "regex"):
                print(pattern_module.regex(seed))
            else:
                print(pattern_module.input(seed, 1))