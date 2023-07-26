N = int(input())
score = [0]
dp = [0 for _ in range(N+1)]
for i in range(N):
    score.append(int(input()))

dp[1] = score[1]
if N <= 2:
    if N == 2:
        dp[2] = dp[1]+score[2]
    print(dp[N])
else:
    for i in range(2, N+1):
        dp[i] = max(dp[i-2], dp[i-3]+score[i-1]) + score[i]
    print(dp[N])

