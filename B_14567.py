from collections import deque
from collections import defaultdict

import sys

# 한 학기에 들을 수 있는 과목 수에는 제한이 없다.
# 모든 과목은 매 학기 항상 개설된다.
input = sys.stdin.readline

N, M = map(int, input().split())
graph = defaultdict(list)
check = [0 for i in range(N+1)]
order = [0 for i in range(N+1)]#선수과목 목록에 아예 포함되지 않는 거도 있어서 초기값을 1로 주어야한다.

result = deque()

for i in range(M):
    key, value = map(int, input().split())
    graph[key].append(value)
    check[value] += 1

for i in range(1, N+1):
    if check[i] == 0:
        result.append((i,1))
        order[i] = 1

while result:
    n, cnt = result.popleft()
    for i in graph[n]:
        check[i] -= 1
        if check[i] == 0:
            result.append((i, cnt+1))
            order[i] = cnt + 1

for i in range(1,len(order)):
    print(order[i],end=" ")


