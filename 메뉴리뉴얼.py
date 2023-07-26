from itertools import combinations 
from collections import defaultdict

def solution(orders, course):
    answer = []
    alphabet = defaultdict(int)
    for order in orders:
        temp = list(order)
        for j in range(1, len(temp)+1):
            comb = combinations(temp, j)
            for c in comb:
                key = ''.join(sorted(list(c)))
                alphabet[key] += 1
    alphabetlist = sorted(alphabet.items(), key = lambda x:len(x[0]))
    print(alphabetlist)
    for i in course:
        temp = []
        for j in range(len(alphabetlist)):
            if len(alphabetlist[j][0]) == i:
                temp.append(list(alphabetlist[j]))
            elif len(alphabetlist[j][0]) < i:
                continue
            elif len(alphabetlist[j][0]) > i:
                break
        temp = sorted(temp, key = lambda x:-x[1])
        maxNum = temp[0][1]
        for k in temp:
            if k[1] == maxNum:
                answer.append(k[0])
            else:
                break
    answer.sort()
    print(answer)
    return answer
solution(["ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE", "ABCDE"], [2,3,5])
# ->['AB', 'ABC', 'ABCDE', 'ABD', 'ABE', 'AC', 'ACD', 'ACE', 'AD', 'ADE', 'AE', 'BC', 'BCD', 'BCE', 'BD', 'BDE', 'BE', 'CD', 'CDE', 'CE', 'DE']
