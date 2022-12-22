#랜선자르기
#input : 가지고 있는 랜선의 개수 K 필요한 랜선의 개수 N
         #k줄에 걸쳐 가지고 있는 랜선의 길이(정수)

N, K = map(int,input().split())

Lan  = []
count = [0  for i in range(N)]
answer = 0

for i in range(N):
    Lan.append(int(input()))

MaxLan = max(Lan)
start = 0
end = MaxLan
mid = int((start+end)//2)

while True:
    if start > end:
        answer = (start + end) // 2
        break
    if mid == 0:
        mid = 1
    for i in range(N):
        count[i] = (int(Lan[i]//mid))

    if (sum(count)) >= K:
        start = mid+1
    else:
        end = mid-1

    mid = int((start+end)//2) 
    
print(answer)

    