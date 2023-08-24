import re
import getopt
import sys

def hex_conversion(input):
    hex_pipe = False
    start_ind = -1
    end_ind = -1
    hex_arr = []
    decoded = ""
    for i in range(len(input)):
        if (input[i] == "|"):
            if (hex_pipe == False):
                hex_pipe = True
                start_ind = i
            else:
                hex_pipe = False
                end_ind = i
                hex_arr = input[start_ind + 1:end_ind].split()
                
                for hex in hex_arr:
                    if (len(hex) != 2):
                        print("invalid syntax for hexadecimals in input |0A 2f|")
                        exit()
                    else:
                        char = chr(int(hex,16))
                        decoded += char 
        else:
            if(not hex_pipe):
                decoded += input[i]
    
    return decoded

"""

input_file = -1
pcre_file = -1

try:
        opts, args = getopt.getopt(sys.argv[1:], ":", ["input=","regex="])  
except:
    print("")
    print("This program requires you to put arguments onto the command line to specify the files that \n", 
          "you are using as inputs into your regular expression and the files containing your regular expressions\n",
          "themselves. Type --input (input file name) to choose an input file and --regex (regex file name)\n",
          "to choose a fil with your regular expressions.")
    exit()

for opt, arg in opts:
    if opt in ["--regex"] :    
        pcre_file = arg
    elif opt in ['--input']:
        input_file = arg
    else:
        print("Invalid input on command line")
        exit()

if (pcre_file == -1 or input_file == -1):
    print("", end = "")
    print("Did not give file names for both the input file and the regular expression file\n",
          "You can do this with --input (input file name)  and --regex (regex file name)")
    #exit()
else:
    input_list = open(input_file).readlines()

    pcre_list = open(pcre_file).readlines()


#print(input_list)
#print(pcre_list)

    for raw_pcre in pcre_list:
        if (raw_pcre[-1] == "\n"):
            pcre = raw_pcre[:len(raw_pcre) - 1]
        else:
            pcre = raw_pcre
        if(pcre[0] == "#"):    
            continue

        for raw_input in input_list:
            if (raw_input[-1] == "\n"):
                input = raw_input[:len(raw_input) - 1]
            else:
                input = raw_input
            if(input[0] == "#"):
                continue

            decoded = hex_conversion(input)
            #print(pcre, decoded)        

            match = re.search(r"" + pcre,decoded)

            if (match):
                print("bobo", end = ' ')
            else:
                print("nein", end = ' ')

            print(pcre, input)
        
        print('')
"""