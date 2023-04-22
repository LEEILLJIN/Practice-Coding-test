from collections import deque
n,m = map(int, input().split())
cMap = []

for i in range(n):
    cMap.append(list(map(int, input().split())))

def bfs(cMap, x,y):
    qu = deque()
    visited = [[0 for i in range(m)] for i in range(n)]
    dx = [-1,1,0,0]
    dy = [0,0,-1,1]
    qu.append([x,y])
    visited[x][y] = 1
    cnt = 0
    switchZero = []
    while qu:
        tempx,tempy = qu.popleft()
        for i in range(4):
            ddx = tempx + dx[i]
            ddy = tempy + dy[i]
            if 0 <= ddx < len(cMap) and 0 <= ddy < len(cMap[0]) and cMap[ddx][ddy] == 0 and visited[ddx][ddy] == 0:
                visited[ddx][ddy] = 1
                qu.append([ddx, ddy])
            elif 0 <= ddx < len(cMap) and 0 <= ddy < len(cMap[0]) and cMap[ddx][ddy] == 1 and visited[ddx][ddy] == 0:
                cMap[ddx][ddy] = 'c'
                switchZero.append([ddx, ddy])
                cnt += 1

    for i in switchZero:
        cMap[i[0]][i[1]] = 0
    return cnt


cnt = []
while True:
    temp = bfs(cMap, 0 , 0)
    if temp == 0:
        break
    else:
        cnt.append(temp)

print(len(cnt), cnt[-1], sep='\n')