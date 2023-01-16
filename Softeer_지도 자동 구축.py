import sys

N = int(sys.stdin.readline())
dp = [0] * 16 
dp[0] = 2 

for i in range(1,N+1):
    dp[i] = dp[i-1] + (dp[i-1] -1) 

print(dp[N]**2) 