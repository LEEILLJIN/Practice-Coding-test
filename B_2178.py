from collections import deque
dx = [-1,0,1,0]
dy = [0,1,0,-1]

N,M = map(int, input().split())
visited = [[0 for i in range(M)]for i in range(N)]
Maze = []
for i in range(N):
    Maze.append(list(input()))

def bfs(graph, visited, x, y):
    queue = deque()
    queue.append([x,y,1])
    dis = 1
    coor = [x,y]
    visited[x][y] = 1
    dx = [-1,0,1,0]
    dy = [0,1,0,-1]
    while queue:
        temp = queue.popleft()

        if temp[0] == N-1 and temp[1] == M-1:
            print(temp[2])
            break
        for i in range(4):
            xx = temp[0] + dx[i]
            yy = temp[1] + dy[i]
            if 0 <= xx < N and 0 <= yy < M:
                if graph[xx][yy] == '1' and visited[xx][yy] == 0:
                    visited[xx][yy] = 1
                    queue.append([xx,yy,temp[2]+1])
                    #카운트를 개수마다하면 안됨 위에 처럼 해야 거리를 잴 수 있음
bfs(Maze, visited, 0, 0)

