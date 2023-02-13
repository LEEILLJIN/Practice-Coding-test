import sys
input = sys.stdin.readline
#M:조작법은 M개의 버튼 조작
#N : 사용자가 누른 N개의 버튼
#K : 자판기에는 총 K개의 버튼
M, N, K = map(int, input().split())

secretNum = list(map(int,input().split()))
UserNum= list(map(int,input().split()))
temp = []

if N > M:
    for i in range(N):
        if int(UserNum[i]) == int(secretNum[0]):
            for j in range(i, i+M):
                temp.append(UserNum[j])
            if str(temp) == str(secretNum):
                print("secret")
                exit(0)
            else:
                temp = []
    print("normal")
else:
    print("normal")
#오답
#---------------------------------------------------------------------
#정답
import sys
input = sys.stdin.readline
#M:조작법은 M개의 버튼 조작
#N : 사용자가 누른 N개의 버튼
#K : 자판기에는 총 K개의 버튼
M, N, K = map(int, input().split())
# ''.join(list(sys.stdin.readline().rstrip().split()))
secretNum = ''.join(list(input().split()))
UserNum= ''.join(list(input().split()))
if secretNum in UserNum:
    print("secret")
else:
    print("normal")
