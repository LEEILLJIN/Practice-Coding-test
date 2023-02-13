
while True:
    try:
        n = int(input())

        onlyone = 1
        onlyoneLen = 0
        cnt = 1
        while True:
            if int(onlyone) % n == 0:
                onlyoneLen = len(str(onlyone))
                break
            onlyone += 10**cnt
            cnt += 1
        print(cnt)
    except:
        break

