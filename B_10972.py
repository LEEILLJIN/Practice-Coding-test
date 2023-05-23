N = int(input())

standard = list(map(int, input().split()))
flag = True
x=0
y=0
for i in range(N-1, 0 ,-1):
    if standard[i] > standard[i-1]:
        x = i-1
        y = i
        for j in range(N-1, 0 ,-1):
            print(i,j)
            if standard[j] > standard[x]:
                print(standard[x],standard[j])
                standard[j], standard[x] = standard[x], standard[j]
                flag = False
                break
    if flag == False:
        print(x,y)
        standard = standard[:y] + sorted(standard[y:])
        print(*standard)
        break

if flag == True:
    print(-1)

