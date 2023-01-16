import sys
input = sys.stdin.readline
from collections import deque
#전광판은 최대 다섯 자리의 자연수만 육각형 전구 7x5=35

T = int(input().rstrip())
Num = {
    '0' : [0,1,2,4,5,6],
    '1' : [2,6],
    '2' : [1,2,3,4,5],
    '3' : [1,2,3,5,6],
    '4' : [0,2,3,6],
    '5' : [0,1,3,5,6],
    '6' : [0,1,3,4,5,6],
    '7' : [0,1,2,6],
    '8' : [0,1,2,3,4,5,6],
    '9' : [0,1,2,3,5,6]
}
for i in range(T):
    answer = 0
    start, end = map(str, input().split())
    start = deque(start)
    end = deque(end)
 
    if len(start) < len(end):
        gap = len(end) - len(start)
        for i in range(len(end) - len(start)-1, -1 ,-1):
            answer += len(Num[end[i]])
            start.appendleft(end[i])
        for i in range(gap, len(end)):
            cnt = 0
            for j in Num[end[i]]:
                if j in Num[start[i]]:
                    cnt += 1
            answer += len(Num[end[i]]) + len(Num[start[i]]) - cnt*2

    elif len(start) > len(end):
        gap = len(start) - len(end)
        for i in range(gap):
            answer += len(Num[start[i]])
        for _ in range(gap):
            start.popleft()
        for i in range(len(end)):
            cnt = 0
            for j in Num[end[i]]:
                if j in Num[start[i]]:
                    cnt += 1
            answer +=  len(Num[start[i]]) + len(Num[end[i]]) - cnt*2
    else:
        for i in range(len(end)):
            cnt = 0
            for j in Num[end[i]]:
                if j in Num[start[i]]:
                    cnt += 1
            answer +=  len(Num[start[i]]) + len(Num[end[i]]) - cnt*2

    print(answer)