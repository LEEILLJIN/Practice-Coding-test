from collections import deque
#(2,2) (2,3) (2,4) (3,4) (4,4) (5,4) (5,3) (5,2) (4,2) (3,2) (2,2)

def solution(rows, columns, queries):
    answer = []
    rotate = deque()
    route = []
    mincheck = []
    matrix = [[0 for i in range(columns)] for i in range(rows)]
    value = 1
    for i in range(rows):
        for j in range(columns):
            matrix[i][j] = value
            value += 1
    #(2,2) (2,3) (2,4) (3,4) (4,4) (5,4) (5,3) (5,2) (4,2) (3,2) (2,2)
    for i in range(len(queries)):
        startx, starty, endx, endy = queries[i]
        for j in range(starty, endy+1):
            route.append([startx,j])
        for k in range(startx+1, endx+1):
            route.append([k,endy])
        for l in range(endy-1, starty-1, -1):
            route.append([endx, l])
        for m in range(endx-1, startx-1, -1):
            route.append([m, starty])
        
        for n in range(len(route)):
            print(route[n])
            mincheck.append(matrix[route[n][0]-1][route[n][1]-1])
            rotate.append(matrix[route[n][0]-1][route[n][1]-1])
            if n>0:
                matrix[route[n][0]-1][route[n][1]-1] = rotate.popleft()
            print(rotate, matrix[route[n][0]-1][route[n][1]-1])
            print(route[n][0], route[n][1])

        print(mincheck)
        answer.append(min(mincheck))
        mincheck.clear()
        route.clear()
        rotate.clear()

    return answer
print(solution(6,6,[[2,2,5,4],[3,3,6,6],[5,1,6,3]]))