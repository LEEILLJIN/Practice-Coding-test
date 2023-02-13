from itertools import permutations
n = input()
flag = False
result = 0
nlist = list(map(int,n))
templist = []
for i in permutations(nlist):
    item = int(''.join(map(str, i)))
    templist.append(item)

checklist = list(set(templist))
checklist.sort()
for i in range(1, len(checklist)):
    if int(checklist[i]) > int(n):
        result = checklist[i]
        flag = True
        break
if flag:
    print(result)
else:
    print(0)

