#N이 3의 거듭제곱이다. 크기 = NxN
#N이 3보다 클 경우, 크기 N의 패턴은 공백으로 채워진
#가운데의 (N/3)×(N/3) 정사각형을 크기 N/3의 패턴으로 
#둘러싼 형태이다. 

N = int(input())
starList = [["*" for i in range(N)]for i in range(N)]
def star(num,x,y):
    global starList
    if x == N and y == N:
        return

    for i in range(x+num//3, x+(num//3)*2):
        for j in range(y+num//3, y+(num//3)*2):
            starList[i][j] = " "

    if num == 1:
        return
    star(num//3, x, y)
    star(num//3, x+num//3, y)
    star(num//3, x, y+num//3)
    star(num//3, x+num//3, y+num//3)
    star(num//3, x+(num//3)*2, y)
    star(num//3, x, y+(num//3)*2)
    star(num//3, x+(num//3)*2, y+(num//3)*2)
    star(num//3, x+(num//3), y+(num//3)*2)
    star(num//3, x+(num//3)*2, y+(num//3))
    
star(N,0,0)
for i in range(len(starList)):            # 세로 크기
    for j in range(len(starList[i])):     # 가로 크기
        print(starList[i][j], end='')
    print()
