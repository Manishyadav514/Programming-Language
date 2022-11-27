# first
dic = {}  # empty dictionary
n = int(input())   # user input
for _ in range(n):
    operands, value = map(str, input().split())
    # insert element in dictionary
    if operands == 'insert':
        dic[value] = 0    # adding value in dictionary
    # check whether value is in the dictionary
    elif operands == 'find':
        if value in dic.keys():
            print('yes')
        else:
            print('no')

# second
n = int(input())
dic = {}
for _ in range(n):
	s = input()
	if s[0] == "i":
		dic[s[7:]] = 0
	else:
		if s[5:] in dic:
			print("yes")
		else:
			print("no")