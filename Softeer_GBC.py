#0m ~ 100m 엘리비이터 속도검사
#N개의 구간으로 나뉘며 해당 구간의 제한속도가 주어짐
#M개의 줄은 광우가 테스트하는 구간의 길이와 속도
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

limit = [0 for i in range(101)]
check = [0 for i in range(101)]
temp1 = 0
for i in range(N):
    dis, speed = map(int, input().split())
    for j in range(temp1, temp1+dis+1):
        limit[j] = speed
    temp1 += dis
temp2 = 0
for i in range(M):
    dis, speed = map(int, input().split())
    for j in range(temp2, temp2+dis+1):
        check[j] = speed
    temp2 += dis

maxgap = 0
for i in range(101):
    maxgap = max(maxgap, check[i] - limit[i])

print(maxgap)