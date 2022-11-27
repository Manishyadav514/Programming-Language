dic = {}  # empty dictionary
dic["value"] = 0
dic["vue"] = 0
print(dic.keys())

dic={'manish':{"phone":'samsng',"colour":'blue'},"deepak":{"phone":'redmi',"colour":'black'}}
print(dic)

d = {'navin':'samsng','manish':'redmi'}
print("1:", d)
print("2:", d.keys())                                 # dictionay.keys()
print("3:", d.values())                               # RETURNS VALUE SAMSANG AND REDMI
print("4:", d['manish'])                              # RETURNS VALUE OF KEY MANISH
print("5:", d.get('navin'))                           # RETURNS VALUE OF KEY MANISH

dictionary["Deepak"]="realmi"                         # ADD NEW KEY-VALUE
print(d.get("rahul", "anything"))                     #  RETURNS VALUE ANYTHING IF THE GIVEN KEY IS NOT IN THRE DIC
dictionary["manish"]="redminote 7s"                   # MODIFYT THE VALUE FOR A KEY
del(d["navin"])                                       # DELETE KEY-VALUE,
print(d)
print(len(d))
print(max(d))                                         # CHECKS ALPHABETICAL ORDER OF KEYS
print(min(d))
print("manish" in d)                                  #  CHECKS WHETHER THIS KEY/VALUE IS IN D OR NOT
lst=[2,3,4,4,4,4,4,4,4,4]                             #   DICTIONARY DOESN'T CONTAIN DUPLICATE ITEMS
a=dict.fromkeys(lst,25)                               # IT SETS VALUE 25 TO EACH KEY
print(a)
dic={'manish':{"phone":'samsng',"colour":'blue'},"deepak":{"phone":'redmi',"colour":'black'}}
print(dic)
print(dic.values())
for v in dic.values():
    print(v["phone"])
# WAYS OF RECALLING DICTIONARY
d1={"a":1,"b":2}
d2={"y":25,"z":26}
d={}

for i in (d1,d2):
    d.update(i)
print(d)
d3={**d1,**d2}
print(d3)                                             # UNPACKS DICTIONARY
print(*d1,*d2)                                        # UNPACKS VALUES

for a,b in d.items():                                 # RETURNS KEYS AND VALUES
    print(a,b)
for k in d.keys():                                    # RETURNS KEYS
    print(k)
for v in d:                                           # RETURNS KEYS
    print(v)
for v in d.values():                                  # RETURNS VALUE
    print(v)
#del(d)                                               # delete all
#dictionary.clear()
dic={"A":3,"B":2,"C":1}
print(max(list(dic.keys())))
print(dic[max(dic.keys(),key=(lambda k: dic[k]))])
#####

