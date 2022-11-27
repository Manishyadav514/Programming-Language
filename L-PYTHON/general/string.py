# STRING
s = "manish udsyid hdioshod hidh"
for x in s[:].split():
    s = s.replace(x, x.capitalize())
print(s)

p="codeblocks"
string='youtube'
print("1.0:", 'string'+p)
print("1.1:", string[-2])
print("1.2:", string[0:])
print("1.3:", string[1:5], p[0:9:2])
print("1.4:", string[2:]+'p')
print("1.5:", 'A''B')
print("10z.6:", 'ce' in 'race')
print("1.7:", '-'* 10, 'MANISH'*5)
# CONVERSION
print("1.8:", "MANISH yadav".upper(), p.upper())
print("1.9:", "Hello".lower(), p.lower())
print("2.0:", "manish".capitalize())
print("2.1:", "MAN123@,/=9ish".swapcase())                          # SWAP LOWER CASE LETTERS INTO UPPERCASE AND VICE-VERSA
# CONTENT TEST FUNCION
print("2.2:", "hello".islower(), "HELLO".isupper())                 # CHECKS ALL CHARACTERS ARE LOWER/UPPER CASE
print("2.3:", "12HELLO".casefold() )                                # CHECKS ALL CHARACTERS ARE
print("2.4:", "Hello".isalpha())                                    # CHECKS ALL CHARACTERS ARE
print("2.5:", "Hello23".isascii())                                  #
print("2.6:", "Hell123".isalnum())                                  # ALPHANUMERIC--CHECKS ALL CHARACTERS ARE DIGITS OR ALPHABETS
print("2.7:", "123HEKL".isdigit())                                  # CHECKS ALL CHARACTERS ARE DIGITS
print("2.8:", "MANISH".startswith("MA"))                            # CHECKS IF STARTS WITH A VALUE RESPECTIVELY
print("2.9:", "MANISH".endswith('ISH'))                             # CHECKS IF END WITH A VALUE RESPECTIVELY
# SEARCH AND REPLACE
print("3.0:", "Manish__Yadav".split('__'))                          #  ['Manish', 'Yadav']
print("3.1:", "Manish\\Yadav".partition('\\'))                      # ('Manish', '\\', 'Yadav')
print("3.2:", "ABC"<"ABD", "ABC"<"B", "e"<"ABC")                    # ALPHABETIC ORDER CHECKED, LOWERCASE>UPPERCASE
print("3.3:", ord('A'), ord('B'), ord('Y'), ord('Z'))                # GIVES UNICODE VALUE
print("3.4:", chr(65), chr(1), chr(2), chr(90) )
print("3.5:", "MANish YADav".lstrip())
print("3.6:", "MANish YADav".rstrip())
print("3.7:", "ManishYadav".find('Y') )
print("3.8:", "ManishYadav".replace('Yadav','Kumar'))
print("3.9:", len('MANISH'))
print("4.0:", 'MANISHYADAV'.count('A'))
x="MANISH"
print("4.1:", [*x])
# MULTILINE STRING
msg1="good"
msg1=msg1+'man'
print(msg1)
print('He said,\'are you ok?\'.',  'PyPy:\\D\\drive')    # ESCAPE SEQUENCE
# RAW STERING PREPEND R
print(r'PyPy:\D\drive')
print('Go,\ run')
print("""See, that's me.""")
print(("What!" "that's done"))
#####
# let us create a test string

testString1 = "Hello World!"
print("Original String: "+ testString1)
# Print this string in lower case

# Converting a string to lower case
print("Converting to LowerCase")
print(testString1.lower())

# Converting a string to upper case
print("Converting to Upper Case")
print(testString1.upper())

# Capitalizing a string
# Only the first letter in the string will be capitalized
print("Capitalizing the String")
print(testString1.capitalize())

# Trying to slice out a substring between given indexes
print("Substring from index 1 to 7")
print(testString1[1:8])

#Substring from the start till character at index = 7 (start of string is index 0)
print("Substring from the start till character at index = 7 (start of string is index 0): ")
print(testString1[:8])

#Substring from the character at index = 7, till the end of the string (remember: start of string is index 0)
print("Substring from the character at index = 7, till the end of the string (remember: start of string is index 0): ")
print(testString1[7:])


#Find the position of a  substring within the string
#This gives us the first index during a left to right scan. If the string is not found, it returns -1
print("Find the index from which the substring 'llo' begins within the test string")
print(testString1.find('llo'))

print("Now, let's look for a substring which is not a part of the given string")
print(testString1.find('xxy'))

# Now, trying to find the index of a substring between specified indexes only
print("Now, trying to find a substring between specified indexes only: looking for 'l' between 4 and 9")
print(testString1.find('l',4,9))

# rfind is used, to find the index from the reverse
# So, testString1.rfind('l') will look for the last index of l in the string
print("find('l') on the given string returns the following index (scanning the string from left to right):")
print(testString1.find('l'))

print("rfind('l') on the given string returns the following index (this scans the string from right to left):")
print(testString1.rfind('l'))

# Now let us try to replace/substitute a substring of this string with another string
print("Replacing World with Planet")
print(testString1.replace("World","Planet"))


# Now let us try to split the string, into separate words
# let us split it wherever there is a space
print("Splitting the string into words, wherever there is a space")
print(testString1.split(" "))
print(testString1.rsplit(" "))

# Remove leading and trailing whitespace characters
testString2 = "Hello World!  "
print("Current Test String=" + testString2)
print("Length (there are whitespaces at the end):" + "len(testString2)")
print("Length after stripping "+ "len(testString2.strip())")


print(ord(x))     # asciiz to 
print(chr(96))    # number to asciiz