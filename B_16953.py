a, b = map(str, input().split(" "))

cnt = 0
while True:
    if a==b:
        print(cnt+1)
        break
    elif (int(b)%2 !=0 and b[-1] != '1') or (int(b) < int(a) ):
        print(-1)
        break
    else:
        if b[-1] == '1':
            b = b[:-1]
            cnt += 1
        else:
            if int(b) % 2 == 0:
                b = str(int(b)//2)
                cnt += 1

   