from collections import defaultdict

N,M,X = map(int,input().split())
#N명의 학생, 총 M개의 단방향 도로, X번 마을에서 파티
graph = defaultdict(list)
table = [[int(1e9) for _ in range(N+1)]for _ in range(N+1)]

for i in range(M):
    start, end, value = map(int,input().split())
    graph[start].append([end, value])
    table[start][start] = 0
    table[start][end] = value

def get_smallest_node(distance, visted):
    min_value=int(1e9)
    index = 0
    
    for i in range(1, N+1):
        if distance[i] < min_value and not visted[i]:
            min_value = distance[i]
            index = i
    return index

def Daijkstra(start,visted):
    visted[start] = True
    for i in range(N-1):
        now = get_smallest_node(table[start], visted)
        visited[now] = True
        for j in graph[now]:
            cost = table[start][now] + j[1]
            if cost < table[start][j[0]]:
                table[start][j[0]] = cost

for i in range(N):
    visited = [False]*(N+1)
    Daijkstra(i+1, visited)

result = []
for i in range(N):
    result.append(table[i+1][X] + table[X][i+1])

print(max(result))