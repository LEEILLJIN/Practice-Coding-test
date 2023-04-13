# from collections import defaultdict
# from collections import deque

# def solution(gems):
#     answer = []
#     gemsSetList = list(set(gems))
#     gemcheck = defaultdict(int) 
#     check = deque()
#     result = []
#     for i in range(len(gems)):
#         gemcheck[gems[i]] += 1
#         check.append(i)
#         if i >= len(gemsSetList)-1:
#             while check:
#                 cnt = 0
#                 for k in gemsSetList:
#                     if gemcheck[k] < 1:
#                         break
#                     else:
#                         cnt += 1
#                 if cnt == len(gemsSetList):
#                     start = check.popleft()+1
#                     gemcheck[gems[start-1]] -= 1
#                     result.append([i+1-start,start,i+1])
#                 else:
#                     break   
#     result.sort()
#     answer = result[0][1:]
#     return answer
from collections import defaultdict
from collections import deque

def solution(gems):
    answer = []
    gemsSetList = list(set(gems))
    gemcheck = defaultdict(int) 
    check = deque()
    result = []
    start = 0
    end = 0
    for i in range(len(gems)):
        gemcheck[gems[i]] += 1
        print(gemcheck, len(gemcheck))
        if len(gemcheck) == len(gemsSetList):
            result.append([(end+1)-(start+1), start+1, end+1])
            gemcheck[gems[start]] -= 1
            if gemcheck[gems[start]] == 0:
                del gemcheck[gems[start]] 
            start += 1
        else :
            end += 1
            break
    result.sort()
    print(result)
    answer = result[0][1:]
    return answer
gems = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(gems)) 