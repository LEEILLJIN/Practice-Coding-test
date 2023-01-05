from collections import deque

num = int(input())
stoneList = list(map(int,input().split()))
start, goal = map(int,input().split())

# graph = [[]]
temp= []
visited = [False]*num

# for index,value in enumerate(stoneList):
#     temp.append(index)
#     for t_index,t_value in enumerate(stoneList):
#         if (abs(index - t_index))% value == 0:
#             if t_index not in temp:
#                 temp.append(t_index)
#     graph.append(temp)
#     temp = []
# print(graph)
def Bfs(stoneList, node, visited):
    cnt = 0
    queue = deque()
    queue.append((node,cnt))
    global goal
    visited[node] = True
    if len(stoneList) == 1:
        print(0)
        return
    while queue:
        v,cnt = queue.popleft()
        if v == goal-1:
            break
        jump = stoneList[v]
        m = 1
        while v-jump*m >=0 or v+jump*m < num :
            if v+jump*m < num and visited[v+jump*m] == False:
                visited[v+jump*m] = True
                queue.append((v+jump*m,cnt+1))
            if v-jump*m >=0 and visited[v - jump*m] == False:
                visited[v-jump*m] = True
                queue.append((v-jump*m,cnt+1))
            m+=1

        # for i in graph[v]:
        #     if not(visited[i]):
        #         queue.append(i,cnt+1)
        #         visited[i] = True
                # print(queue)

    if visited[goal-1] == False:
        print(-1)
    else:
        print(cnt)
Bfs(stoneList, start-1, visited)
