#(1,2) (2,1) = 2  (4,1) (2,1) = 2
#한 집에서 최소 거리인 치킨 집의 카운트를 올리고 가장 적은거부터 삭제 카운트와 거리도 있어야 되나?
#각 집에서 최소 거리인 치킨 집을 어떻게 구하지
from itertools import combinations
N, M = map(int, input().split())
city = []
for i in range(N):
    city.append(list(input().split(" ")))
homelist = []
chickenlist = []
result = 1000000
for i in range(N):
    for j in range(N):
        if city[i][j] == "1":
            homelist.append([i+1,j+1])
        elif city[i][j] == "2":
            chickenlist.append([i+1, j+1])

resultchicken = combinations(chickenlist,M)

for chicken in resultchicken:
    temp = 0
    for home in homelist:
        chickenDis = 9999
        for j in range(M):
            chickenDis = min(chickenDis, abs(home[0]-chicken[j][0]) + abs(home[1] - chicken[j][1]))
        temp += chickenDis
    result = min(temp, result)


print(result)
