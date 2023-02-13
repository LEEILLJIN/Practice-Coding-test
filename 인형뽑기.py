# 행과 열을 반대로 접근하면 되지 않을까?

basket = []

def solution(board, moves):
    answer = 0
    for i in moves:
        for j in range(len(board)):

            if board[j][i-1] != 0:
                answer += checkcnt(board[j][i-1])
                board[j][i-1] = 0
                break
            #4, (3, (1, 1) ,3), 2, 4
    return answer

def checkcnt(now):
    global basket
    cnt = 0
    if basket:
        if basket[-1] == now:
            basket.pop()
            cnt += 2
        else:
            basket.append(now)
            return cnt
    else :
        basket.append(now)
    return cnt
            
     
print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]], [1,5,3,5,1,2,1,4]))