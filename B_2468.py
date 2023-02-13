from collections import deque
N = int(input())
visited = [[0 for i in range(N)]for i in range(N)]
Map = []
minHeight = 100
maxHeight = 0
result = 1
for i in range(N):
    temp = list(map(int, input().split(" ")))
    minHeight = min(temp) if minHeight > min(temp) else minHeight
    maxHeight = max(temp) if minHeight < max(temp) else maxHeight
    Map.append(temp)




def bfs(graph, Height):
    queue = deque()
    dx = [0, 0, 1, -1]
    dy = [1, -1, 0, 0]
    visited = [[0 for i in range(N)]for i in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(N):
            if graph[i][j] > Height and visited[i][j] == 0:
                queue.append([i,j])
                visited[i][j] = 1
                while queue:
                    xx, yy= queue.popleft()
                    for k in range(4):
                        if 0 <= xx+dx[k] < N and 0 <= yy+dy[k] < N and graph[xx+dx[k]][yy+dy[k]] > Height and visited[xx+dx[k]][yy+dy[k]] == 0:
                            queue.append([xx+dx[k],yy+dy[k]])
                            visited[xx+dx[k]][yy+dy[k]] = 1
                cnt += 1
    return cnt

for i in range(maxHeight, minHeight-1, -1):
    temp = bfs(Map, i)
    result = temp if result < temp else result
print(result)
