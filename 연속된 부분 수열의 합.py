#dp
def solution(sequence, k):
    answer = []
    dp = [[0 for _ in range(len(sequence)+1)] for _ in range(len(sequence)+1)]
    result = []
    for i in range(len(sequence)):
        for j in range(i,len(sequence)):
            dp[i][j] = dp[i][j-1] + sequence[j]
            if dp[i][j] == k:
                result.append([j-i,i,j])
                
    
    result.sort(key = lambda x : (x[0], x[1]))
    
    answer = result[0][-2:]
    return answer