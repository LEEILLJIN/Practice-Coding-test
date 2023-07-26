# import sys

# N = int(input())
# tempo = []
# pay = []
# dp = [0 for _ in range(N+1)]

# for i in range(N):
#     t,p = map(int, sys.stdin.readline().split())
#     tempo.append(t)
#     pay.append(p)

# for i in range(N):
#     for j in range(i+tempo[i], N+1):
#         if dp[j] < dp[i] + pay[i]:
#             dp[j] = dp[i] + pay[i]

# print(dp[N])
            
notworking = "https://interviewbank.s3.us-west-2.amazonaws.com/BasicProfilePhoto.png"
working = "https://interviewbank.s3.us-west-2.amazonaws.com/BasicProfilePhoto.png"

if notworking == working:
    print("둘이 똑같은데 왜 안나와 사진이")
else:
    print("사실 둘이 주소 다름ㅋㅋ")