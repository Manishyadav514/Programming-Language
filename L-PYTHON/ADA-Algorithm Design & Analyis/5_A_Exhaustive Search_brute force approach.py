# to check whther element of b can be formed by linear combination of elements of A
n = int(input())
A = list(map(int,input().split()))
n = int(input())
B = list(map(int,input().split()))

# using brute force method
def solve(index, b):
    # b becomes zero because we subtract elements of A
    if b == 0:
        return True
    # conditions in which b can't be the linear combination
    elif  index >= len(A) or b>sum(A) or b < min(A) or b<0:
        return False
    # continue the recursion and returns True/False
    condition = solve(index+1, b) or solve(index+1, b-A[index])
    return condition
for b in B:
    if solve(0, b) == True:
        print('yes')
    else:
        print('no')



# brute force method
def solve(i,value):
  if value == 0:
    return True
  if i >= len(A) or value < 0 or sum(A[i:]) < value:
    return False
  res = solve(i+1, value) or solve(i+1, value-A[i])
  return res
ans = [solve(0,b) for b in B]
for a in ans:
    if solve(0,a) == True:
        print('yes')
    else:
        print('no')
  #print('yes') if a else print('no')







# combination method
from itertools import combinations
def check_combination(A,B):
    comb_list = []
    for i in range(1, len(A) + 1):
        for j in combinations(A, i):
            comb_list.append(sum(j))
    for b in B:
        if b in comb_list:
            print("yes")
        else:
            print("no")
check_combination(A,B)


# help
def solve(i, m):
	if m == 0:
		return True
	if i == n:
		return False
	return solve(i + 1, m) or solve(i + 1, m - A[i])

for m in M:
	if solve(0, m):
		print("yes")
	else:
		print("no")