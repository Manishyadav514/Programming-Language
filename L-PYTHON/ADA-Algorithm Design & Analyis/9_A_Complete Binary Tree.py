n = int(input())
s = list(map(int, input().split()))

def Complete_Binary_tree(s):
    for i in range(len(s)):
        result = 'node ' + str(i+1) + ': ' + 'key = ' + str(s[i])+', '
        if i!= 0:
            result += 'parent key = ' + str(s[(i-1)//2]) + ', '
        if 2*i+1 < len(s):
            result += 'left key = ' + str(s[2*i+1]) + ', '
        if 2*i+2 < len(s):
            result += 'right key = ' + str(s[2*i+2]) + ', '
        print(result)

Complete_Binary_tree(s)