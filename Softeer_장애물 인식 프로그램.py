#50분 걸림...
import sys
from collections import deque

n = int(input())
Map = []
visited = [[0 for _ in range(n)]for _ in range(n)]
BlockCnt = 0
cntList = []
for i in range(n):
    temp = list(input())
    Map.append(temp)
    temp = []
def bfs(Map, index) :
    global n
    global visited
    dx = [0,0,-1,1]
    dy = [-1,1,0,0]
    cnt = 1
    queue = deque()
    queue.append(index)
    while queue:
        i,j = queue.popleft()
        for k in range(4):
            if (0 <= j + dy[k] < n) and (0 <= i + dx[k] < n) :
                if Map[i + dx[k]][j + dy[k]] == "1" and visited[i + dx[k]][j + dy[k]] == 0:
                    visited[i + dx[k]][j + dy[k]] = 1
                    cnt += 1
                    queue.append([i + dx[k], j + dy[k]])
                else :
                    continue
    return cnt

for i in range(len(Map)):            # 세로 크기
    for j in range(len(Map[i])):     # 가로 크기       
        if (Map[i][j] == "1") and (visited[i][j] == 0):
            visited[i][j] = 1
            cntList.append(bfs(Map, [i,j]))
        else:
            continue

cntList.sort()
print(len(cntList))
print(*cntList, sep='\n')