from collections import deque

A = (deque(input()))
B = (deque(input()))
lcsmap = [[0 for _ in range(len(B)+1)] for _ in range(len(A)+1)]
lcs = 0

A.appendleft(0)
B.appendleft(0)

for i in range(1,len(A)):
    for j in range(1, len(B)):
        if A[i] == B[j]:
            lcsmap[i][j] = lcsmap[i-1][j-1]+1
        else:
            lcsmap[i][j] = max(lcsmap[i-1][j], lcsmap[i][j-1])
        

print(lcsmap[-1][-1])


