import importlib
import modules.RandomFunctions as RandomFunctions
import re
import modules.InputConverter as InputConverter
import random
import getopt
import sys

patterns = []
reps = []
adder = -1

try:
    opts, args = getopt.getopt(sys.argv[1:], ":", ["folder=","pattern=", "lines="])  
except:
    print("To use this program you need to input files from the command line that you want to run\n",
          "to specify this type --pattern (file name of pattern) to generate a random regular expression and \n",
          "random inputs based on the pattern outlined in that file. \n",
          "After that type --lines (number of random inputs), this will decide how many different random\n",
          "inputs will be generated and tested through your regular expression. The first input will always\n",
          "successfully evalute and the following inputs will fail in around 3 alternating ways depending on\n",
          " the pattern.")
    exit()

for opt, arg in opts:
    if opt in ["--pattern"] :    
        patterns.append(str(arg))
    elif opt in ["--lines"]:
        reps.append(int(arg))
    elif opt in ["--folder"]:
        adder = arg
    else:
        print("Invalid input on command line")
        exit()

if (len(reps) != len(patterns)):
     print("Have equal number of line inputs and pattern inputs on commandline")
     exit()

if (adder != -1):
    for i in range(len(patterns)):
        patterns[i] = str(adder) + "." + patterns[i]

for num in range(len(patterns)):
    
    pattern_module = importlib.import_module(patterns[num])
    seed = pattern_module.generate_rand()
    regex = pattern_module.regex(seed)

    for i in range(reps[num]):
        input = pattern_module.input(seed, i)
        converted = InputConverter.hex_conversion(input)
        if (re.search(regex, converted)):
            print("Succesfull Match: ", regex, "\n", input)
        else:
            print("Failure to Match: ", regex, "\n", input)

        print("")