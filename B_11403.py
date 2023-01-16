#그래프 G에대해 모든 정점(i,j)에 대해서 
# i에서 j로 가는 경로가 있는지 없는지
N = int(input())
adj = []
check = [[0 for i in range(N)]for i in range(N)]
for _ in range(N):
    temp = list(map(int, input().split()))
    adj.append(temp)
    temp = []

for k in range(N):
    for i in range(len(adj)):
        for j in range(len(adj[i])):
            if adj[i][k] == 1 and adj[k][j]==1:
                adj[i][j] = 1
                    
            # if check[i][j] == 1:
            #     continue
            # else:
            #     if adj[i][j] == 0:
            #         if adj[i][k] == 1 and adj[k][j]:
            #             check[i][j] = 1
            #     else:
            #         check[i][j] = 1


for i in range(len(adj)):
    for j in range(len(adj[i])):
        print(adj[i][j],end=" ")
    print()
# for i in range(len(check)):
#     for j in range(len(check[i])):
#         print(check[i][j],end="")
#     print()



# BFS
from collections import deque
 
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]
visited = [[0]*n for _ in range(n)]
 
def bfs(x):
    queue = deque()
    queue.append(x)
    check = [0 for _ in range(n)]
 
    while queue:
        q = queue.popleft()
 
        for i in range(n):
            if check[i] == 0 and graph[q][i] == 1:
                queue.append(i)
                check[i] = 1
                visited[x][i] = 1
 
for i in range(0, n):
    bfs(i)
 
for i in visited:
    print(*i)