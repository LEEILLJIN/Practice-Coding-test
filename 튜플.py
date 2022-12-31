from collections import defaultdict


def solution(s):
    answer = []
    numList = []
    maxlenList = []
    temp = []
    numdict = defaultdict(int)
    sstr = ""

    num = s[1:len(s)-1]
    for i in range(len(num)):
        if num[i] == "{":
            continue
        elif num[i] == "}":
            temp = sstr.split(",")
            numList.append(temp)
            maxlenList = maxlenList if len(maxlenList) > len(temp) else temp
            sstr = ""
            temp = []
            continue
        elif num[i] == "," and num[i-1] == "}":
            continue
        elif num[i].isdigit() or num[i] == ",":
            sstr += num[i]
    
    for i in numList:
        for j in maxlenList:
            if j in i:
                numdict[j] += 1

    answer = list(map(int, sorted(numdict, key=lambda x:numdict[x], reverse=True)))
            
    return answer


print(solution("{{4,2,3},{3},{2,3,4,1},{2,3}}"))
# print(solution("{{123}}"))
print(solution("{{20,111},{111}}"))