def recursive(string,i, n):
    if (i == n):
        return True
    if string[i].lower() != string[n].lower() or string[i].isdigit():
        return False
    if (i < n + 1):
        return recursive(string, i + 1, n - 1);
    return True


def Check_Palindrome(string):
    n = len(string)
    if (n == 0):
        return True
    return recursive(string,0, n -1);


string = input("Enter your string : ")
def String_Compress(string):
    b = ''
    for a in string.split(" "):
        b = b + a
    return b.lower()

string = String_Compress(string)
if (Check_Palindrome(string)):
    print("Why am I am doing this?")
else:
    new_string = ""
    i = len(string) - 1
    while i >= 0:
        new_string = new_string + string[i]
        i = i - 1
    print(new_string)















# second method
def recursive(string,i, n):
    if (i == n):
        return True
    if string[i].lower() != string[n].lower() or string[i].isdigit():
        return False
    if (i < n + 1):
        return recursive(string, i + 1, n - 1);
    return True


def Check_Palindrome(string):
    n = len(string)
    if (n == 0):
        return True
    return recursive(string,0, n -1);


string = input("Enter your string : ")
def String_Compress(string):
    b = ''
    for a in string.split(" "):
        b = b + a
    return b.lower()

string = String_Compress(string)
if (Check_Palindrome(string)):
    print("Why am I am doing this?")
else:
    new_string = ""
    i = len(string) - 1
    while i >= 0:
        new_string = new_string + string[i]
        i = i - 1
    print(new_string)





string = "Do geese see God"
new_string = ""

i = len(string) - 1
while i>=0:
    new_string = new_string + string[i]
    i = i-1

def String_Compress(string):
    b = ''
    for a in string.split(" "):
        b = b + a
    return b.lower()

if String_Compress(new_string).isdigit():
    print(new_string)
elif String_Compress(string) == String_Compress(new_string):
    print("why am I doing this?")
else:
    print(new_string)





