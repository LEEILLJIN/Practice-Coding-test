# from collections import defaultdict
N, D = map(int, input().split())
graph = [[] for _ in range(10001)]
for i in range(N):
    start, end, value = map(int, input().split())
    if start < D:
        graph[start].append([end, value])
distance = [i for i in range(D+1)]
#기존 값 거리 테이블

for i in range(D+1):
    if i != 0:
        distance[i] = min(distance[i], distance[i-1]+1)
        #만약 0 50 10이 지름길로 입력되어 distance[50]이 10이라면
        #0부터 51까지 가는 거리는 51이 아닌 11이 된다.
        #따라서 distsance[51]을 distance[51] = 51과 distance[49] + 1 = 11중에 작은 값으로 갱신해주어야한다.
    for e, v in graph[i]:
        if e <= D and distance[e] > v + distance[i]:
            distance[e] = v + distance[i]

print(distance[D])
