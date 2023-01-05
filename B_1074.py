#0,0 - 0,1 - 1,0 - 1,1
#N - 2차원 배열 크기, r - 0행~, c - 0열~
import sys
sys.setrecursionlimit(10**6)
N,r,c = map(int,input().split())
order = 0
array  = [[0]*(2**N)]*(2**N)
standard = [[0,0], [0,1], [1,0], [1,1]]
goal = [r,c]

def search(size, x,y):
    global order
    # if x == r and y == c:
    #     #0,0부터 시작해서 r,c로 왔으니 종료
    print("size",size, [x,y],order)
    if size >2:   
        if (x < size//2) and (y < size//2) :
            order += 0
            search(size//2,0,0)
        elif (x < size//2) and (y >= size//2) :
            order += 4*(2**N-1)
            search(size//2,0,size//2)
        elif (x >= size//2) and (y < size//2) :
            order += 4*(2**N-1) * 2
            search(size//2,size//2,0)
        elif (x >= size//2) and (y >= size//2) :
            order += 4*((size//2))* 3
            search(size//2,size//2,size//2)
    else:
        for i in range(len(standard)):
            print([x,y])
            if [x,y] == standard[i]:
                order += i
        print(order)


search(2**N, 7, 7)

# if N == 1:
#     for i in range(len(standard)):
#         if goal == standard[i]:
#             order = i
# else:
#     while True:
#             if r => 2**(N-1):






N,r,c = map(int,input().split())
N = 2**N
ans = 0
def devide(x,y,N):
    global ans
    if x == c and y == r:
        print(ans)
        exit(0)
    elif N==1:
        ans += 1
        return
    if not (x <= c <x + N and y <= r < y+N):
        ans += N*N
        return
    nn = N//2
    devide(x,y,nn)
    devide(x+nn,y,nn)
    devide(x,y+nn,nn)
    devide(x+nn,y+nn,nn)
    return
ans = devide(0,0,N)