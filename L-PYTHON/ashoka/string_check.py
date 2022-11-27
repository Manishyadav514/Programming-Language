import re
string = "aabaab"
Acceptable =  True
index = 0
while Acceptable:
    # checks if the string is of unit length
    if len(string) == 1 and string[0] == 'b':
        print('acceptable')
        Acceptable = False
    elif len(string) == 3 and string == 'aab':
        print('acceptable')
        Acceptable = False
    elif re.search("^aab", string):
        string = string[3: len(string)]
        #print("string", string)
    elif re.search("^aa", string):
        string = string[2: len(string)]
        #print("string", string)
    else:
        print('not acceptable')
        Acceptable = False