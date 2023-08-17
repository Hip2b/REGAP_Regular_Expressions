import getopt
import importlib
import sys
import re
import modules.InputConverter as InputConverter


regex_file = ""
input_file = ""

try:
    opts, args = getopt.getopt(sys.argv[1:], ":", ["regex=", "input="])  
except:
    exit()

for opt, arg in opts:
    if opt in ["--regex"] :    
        regex_file = str(arg)
    elif opt in ["--input"]:
        input_file = str(arg)
    else:
        print("Invalid input on command line")
        exit()

if (regex_file == "" or input_file == ""):
    print("Both comandline parameters must be filled")
    exit()

regex_arr = open(regex_file).readlines()
input_arr = open(input_file).readlines()

for regex in regex_arr:
    regex = regex[:-1]
    print("\nReporting results for regex: " + regex)
    for input in input_arr:
        input = input[:-1]
        decoded = InputConverter.hex_conversion(input)
        if (re.search(regex, decoded)):
            print("Successful Match:", input)
        else:
            print("Failed Match:", input)