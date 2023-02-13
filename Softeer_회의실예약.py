import sys
input = sys.stdin.readline
#N : 회의실 수, M : 예약된 회의의 수
# 총 10개
N,M = map(int,input().split())
RoomName = {}
for i in range(N):
    RoomName[input().rstrip()] = [1 for i in range(10)]

for i in range(M):
    r,s,t = input().split()
    temp = RoomName[r]
    for j in range(int(s)-9, int(t)-10+1):
        RoomName[r][j] = 0


for i in sorted(list(RoomName.keys())):
    print(f"Room {i}:")
    cnt = 0
    timelist = []
    outputlist = []
    for j in range(len(RoomName[i])):
        if RoomName[i][j] == 1:
            if len(timelist)>0 and j - timelist[-1] > 1:
                cnt += 1
                if timelist[0]+9 == 9:
                    outputlist.append(f"09-{timelist[-1]+10}")
                else:
                    outputlist.append(f"{timelist[0]+9}-{timelist[-1]+10}")
                timelist = []
                timelist.append(j)
            else:
                timelist.append(j)
    if len(timelist) > 1:
        cnt += 1
        if timelist[0]+9 == 9:
            outputlist.append(f"09-{timelist[-1]+9}")
        else:
            outputlist.append(f"{timelist[0]+9}-{timelist[-1]+9}")
    if cnt == 0:
        print("Not available")
    else:
        print(cnt, "available:")
        print(*outputlist, sep="\n")
    if i != sorted(list(RoomName.keys()))[-1]:
        print("-----")