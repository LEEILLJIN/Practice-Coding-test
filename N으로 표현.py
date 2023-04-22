# from collections import defaultdict
# import copy
# from itertools import combinations
# infodict = defaultdict(list)
# info = 'java backend junior pizza 100'
# num = [0,1,2,3]
# numlist = list(combinations(num,4))
# print(numlist)
# temp = info.split(" ")
# infodict["".join(temp[:4])].append(int(temp[4]))


# for i in range(1,5):
#     numlist = list(combinations(num,i))
#     print(numlist)
#     # temp2 = copy.deepcopy(temp)
#     # temp2[i] = '-'
#     # print(temp)
#     # print(temp2)
#     # infodict["".join(temp2[:4])].append(int(temp2[4]))
# print(infodict)
# s = "aabbaab"
# check = []
# check.append("1")
# check.append("2")
# check.append("3")
# print(check)
# print(check[-1], check[-2])
# check.clear()
# print(check)
# for i in range(1, len(s)+1):
#     print("i",i)
#     for j in range(0, len(s), i):
#         print(j)
#         check.append(s[j:j+i])
# print(s[6:12])
# print(check)

#abcabcabc
#3abc
def solution(s):
    answer = 0
    result = []
    check = []
    result.append(len(s))
    #len(s)는 len(s)개단위로 압축한 것
    for i in range(1, len(s)):
        eachlen = len(s)
        cnt = 1
        for j in range(0, len(s), i):
            check.append(s[j:j+i])
            print(check)
            if len(check) > 1:
                flag = isright(check,i)
                print(flag)
                if flag:
                    cnt += 1
                else:
                    print("else", check)
                    if cnt > 1:
                        print(cnt, check[-1])
                        eachlen -= (cnt*len(check[-2]))
                        eachlen += (len(str(cnt))+len(check[-2])) 
                        print("eachlen", eachlen)
                    temp = check[-1]
                    check.clear()
                    check.append(temp)
                    cnt = 1

        if flag:
            if cnt > 1:
                eachlen -= (cnt*len(check[-2]))
                eachlen += (len(str(cnt))+len(check[-2])) 
        print("#####################")
        print(i, eachlen)
        print("#####################")

        result.append(eachlen)
        check.clear()
    answer = min(result)
    return answer

def isright(check, i):
    if check[-2] == check[-1]:
        return True
    else:
        return False

solution("aabbaccc")
