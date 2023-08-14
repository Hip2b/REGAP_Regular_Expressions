from dataclasses import dataclass
import sys
import getopt

class CatgInfo:
    """CatgInfo is meant for storing relevant information about the rules in a certain category."""

    categ: str # name of the category
    both: int # number of rules with both pcre and content in them
    neith:int # number of rules with no pcre and no content in them
    pcre: int # number of rules with only pcre in them
    cont: int # number of rules with only content in them
    doub_pcre: int # number of rules with more than one pcre in them
    cont_aft: int # number of lines with content after pcre

    def __init__(self, name = "", both = 0, neither = 0, pcre = 0, content = 0, double_pcre = 0, cont_after = 0) -> None:
        self.categ = name
        self.both = both
        self.neith = neither
        self.pcre = pcre
        self.cont = content
        self.doub_pcre = double_pcre
        self.cont_aft = cont_after
        self.rule_list = [] # the line numbers of every rule in the category 

    def total(self) -> int:
        return self.both + self.neith + self.pcre + self.cont
    
class RuleCheck:

    pcre = False
    cont = False
    pcre_doub = False
    aft_cont = False

    def __init__(self, word_list):
        for word in word_list:
            split = word[0:5]
            if (split == "pcre:"):
                if(self.pcre):
                    self.pcre_doub = True   
                self.pcre = True  

            split = word[0:8]        
            if(split == "content:"):
                if(self.pcre):
                    self.aft_cont = True
                self.cont = True 

def full_adr(word_list) -> str:
    '''Building category name with protocol type, port numbers, and port names'''

    ret = ""
    for subj in word_list[1:7]:
        ret += subj
        ret += " " 
    return ret

def port_adr(word_list) -> str:
    '''Building category name with protocol type and port numbers'''

    ret = ""
    ret += word_list[1] + " "
    ret += word_list[3] + " "
    ret += word_list[4] + " "
    ret += word_list[6]
    return ret

def categ_sort_key(element) -> int:
    return element.total()

def increment_counts(counts, check_info) -> None:
    if(check_info.pcre_doub):
        counts.doub_pcre += 1
    
    if(check_info.aft_cont):
        counts.cont_aft += 1
    
    if (check_info.pcre and check_info.cont):
        counts.both += 1
    elif(check_info.cont):
        counts.cont += 1
    elif(check_info.pcre):
        counts.pcre += 1
    else:
        counts.neith += 1

def sort_info(rule_list) -> tuple:
    categ_arr = []
    order_dict = {}
    file_total = CatgInfo("",0,0,0,0)

    for index in range(len(rule_list)):
        rule = rule_list[index]

        pos = 0
        category = ""

        word_list = rule.split()

        if(catg_type == "Full"):
            category = full_adr(word_list)
        else: # catg_type == "Port"
            category = port_adr(word_list)
    
        if order_dict.get(category, -1) == -1:
            categ_arr.append(CatgInfo(category, 0, 0, 0, 0))
            pos = len(categ_arr) - 1
            order_dict[category] = pos
        else:
            pos = order_dict[category]

        rule_properties = RuleCheck(word_list)

        increment_counts(categ_arr[pos], rule_properties)
        increment_counts(file_total, rule_properties)

        categ_arr[pos].rule_list.append(index)
    
    categ_arr.sort(key=categ_sort_key)

    return (categ_arr, file_total)

def overall_print(categ_arr, file_total, num_lines):
    index = len(categ_arr) - 1

    for ind in categ_arr:
        print("Index:", index, "\tCounts:", ind.total(), "\t", ind.both, ind.cont, ind.pcre, ind.neith,"\t", 
              ind.doub_pcre, ind.cont_aft, "\t Category:" , ind.categ)
        index -= 1

    print("\nFile Stats by the amount of line types in this file:")
    print("(The counts are printed below in the same category type order as they are shown above)")
    print("Total Lines:", num_lines)
    print("Both PCRE and Content:", file_total.both, " Content:", file_total.cont, " PCRE:",
           file_total.pcre, " Neither PCRE or Content:", file_total.neith)
    print("Over One PCRE in a line:", file_total.doub_pcre, " Content after a PCRE:", file_total.cont_aft)

def index_print(categ_arr, line_list):
    index = (len(categ_arr) - 1) - spcf_index 
    line = categ_arr[index]

    for rule in line.rule_list:
        
        if (stat_type == "All"):
            pickout(line_list, rule)

        elif (stat_type == "Both"):
            pickout(line_list, rule, ["pcre", "content"])

        else: # pcre
            pickout(line_list, rule, ["pcre"])

    print("Index:", spcf_index, "\tCounts:", line.total(), "\t" ,line.both, line.cont, line.pcre, line.neith,"\t",
           line.doub_pcre, line.cont_aft,  "\t Category:" , line.categ)

def pickout(line_list ,rule = -1, exclusives = -1):
    word_list = []

    if (exclusives == -1):
        for item in line_list[rule].split()[7:]:
            word_list.append(item)
    else:
        items = line_list[rule].split("; ")

        for item in items[1:]:
            for specifier in exclusives:                  
                if(item[:len(specifier)] == specifier):
                    word_list.append(item)
        
    if (len(word_list) > 0):
        print("Line", rule + 1, end = ' ')
        for word in word_list:
            print(word, end = ' ')
        
        print('')
    

catg_type = "Full"
spcf_index = -1
stat_type = -1
file_name = "snort3-community.rules"

try:
        opts, args = getopt.getopt(sys.argv[1:], ":", ["catg_type=","index=","stat_type=","file_name="])
      
except:
    print("This program requires you to put arguments onto the command line to specify how you want your information\n",
          " to be printed. You must put the --catg_type prefix with options 'Full' and 'Port' after to specifiy\n ",
          "how you want your rule categories to be definied. You can also use the --index prefix with a number after\n",
          " to get more from a specific category type you've found. You can also put the prefix \n",
          "--stat_type with the options 'All', 'Some' or 'Min' to show what type of data you want shown from that\n",
          "specific rule category. The final and most important argument on the command line is the file name\n",
          "Typing '--file_name (your file name here)' will let you read from a specific file in the directory you're\n",
          "calling this program from. If the file name is not specified it will default to 'snort3-community.rules'")
    exit()

for opt, arg in opts:
    if opt in ["--catg_type"] :
        if (arg != "Full" and arg != "Port"):
            print("Category Definition", arg," passed into command line is invalid. 'Full' or 'Port' are your options")
            exit()
        else:
            catg_type = arg
    elif opt in ['--index']:
        spcf_index = int(arg)
    elif opt in ['--stat_type']:
        stat_type = arg
    elif opt in ["--file_name"]:
        file_name = arg
    else:
        print("Invalid input on command line")
        exit()

line_list = open(file_name).readlines()

(categ_arr, file_total) = sort_info(line_list)

if (spcf_index < 0):
    overall_print(categ_arr, file_total, len(line_list))
   
else:
    index_print(categ_arr, line_list)
