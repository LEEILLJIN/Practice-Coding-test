n,m = map(int, input().split())
cMap = []
for i in range(n):
    cMap.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        print(cMap[i][j],end = " ")
    print()

def bfs():
