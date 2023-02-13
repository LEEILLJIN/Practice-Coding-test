from collections import deque
def solution(numbers):
    answer = [0 for i in range(len(numbers))]
    resultlist = []
    qu = deque()
    for index, i in enumerate(numbers):
        if len(qu) == 0:
            qu.append([index,i])
        else:
            while len(qu) > 0 and i > qu[-1][1]:
                temp = qu.pop()
                temp[1] = i
                resultlist.append(temp)
                temp = []
            qu.append([index,i])
    while qu:
        temp = qu.pop()
        temp[1] = -1
        resultlist.append(temp)
        temp = []
    resultlist.sort(key=lambda x : x[0])
    for i in range(len(numbers)):
        answer[i] = resultlist[i][1]
    return answer
#    for i in range(len(numbers)-1):
#        temp = 0
#        for j in range(i, len(numbers)):
#            temp = j
#            if numbers[i] < numbers[j]:
#                answer.append(numbers[j])
#                break
#        if (temp == len(numbers)-1) and len(answer) != i+1:
#            answer.append(-1)
#    answer.append(-1)
    return answer

solution([2, 3, 3, 5])
solution([9, 1, 5, 3, 6, 2])