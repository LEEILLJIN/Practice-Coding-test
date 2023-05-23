from collections import defaultdict

n = int(input())
alphaNum = defaultdict(int)
alphalist = list()
numlist = list()

for i in range(n):
    alphalist.append(list(input()))

for i in alphalist:
    for j in range(len(i)):
        alphaNum[i[j]] += 10**(len(i)-(j+1))

sortedalphaNum = sorted(alphaNum.items(), key=lambda x: x[1], reverse=True)
num = 9

for i in sortedalphaNum:
    alphaNum[i[0]] = str(num)
    num -= 1

for i in alphalist:
    temp = ""
    for j in range(len(i)):
        if i[j] != 0:
            temp += alphaNum[i[j]]
    numlist.append(int(temp))

print(sum(numlist))
