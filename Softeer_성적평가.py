#각 대회 별 등수 및 최종 등수를 매기고 싶다.
import sys
from collections import defaultdict
input = sys.stdin.readline

N = int(input())#참가자의 수
contest = defaultdict(list)


for i in range(3):
    grade = list(map(int, input().split()))
    for j in range(N):
        contest[j].append(grade[j])

gradelist = []
for i in range(N):
    contest[i].append(sum(contest[i]))
for i in range(3):
    #대회 3개니까
    for j in range(N):
        gradelist.append([j,contest[j][i]])
    gradelist.sort(key = lambda x : x[1], reverse = True)
   
    gradelist[0].append(1)
    cnt = 0
    for j in range(1, N):
        if gradelist[j-1][1] == gradelist[j][1]:
            gradelist[j].append(gradelist[j-1][2])
            cnt += 1
        else:
            gradelist[j].append(gradelist[j-1][2]+1 + cnt)
            cnt = 0

    gradelist.sort(key = lambda x : x[0])
    for j in range(N):
        print(gradelist[j][2],end = " ")
    print()
    gradelist = []
# 마지막 최종 점수 
for i in range(N):
    gradelist.append([i,contest[i][-1]])
gradelist.sort(key = lambda x : x[1], reverse = True)

gradelist[0].append(1)
cnt = 0
for j in range(1, N):
    if gradelist[j-1][1] == gradelist[j][1]:
        gradelist[j].append(gradelist[j-1][2])
        cnt += 1
    else:
        gradelist[j].append(gradelist[j-1][2]+1 + cnt)
        cnt = 0

gradelist.sort(key = lambda x : x[0])
for j in range(N):
    print(gradelist[j][2],end = " ")
print()