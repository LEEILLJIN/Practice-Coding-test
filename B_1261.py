import heapq # heapq : 우선순위 큐 구현

C,R = map(int, input().split())
Maze = []
INF = int(1e9)
graph = []
dx = [-1,0,1,0]
dy = [0,1,0,-1]
visited = [[0 for _ in range(C)]for _ in range(R)]

for _ in range(R):
    temp = list(input())
    Maze.append(temp)


for i in range(len(Maze)):            # 세로 크기
    for j in range(len(Maze[i])):     # 가로 크기
        content = [Maze[i][j], i,j]
        graph.append(tuple(content))

print(graph)

# def dijkstra(graph, start) :



