n = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))
print("symmetric difference", len(a.difference(b).union(b.difference(a))))





H = set("Hacker")
R = set("Rank")
#result = H.intersection_update(R)
#result = H.update() (R)
#result = H.difference_update(R)
result = H-=  (R)
#result = H.symmetric_difference_update(R)
print(H)
