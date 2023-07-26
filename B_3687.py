#1 : 2, 
#2 : 5, 
#3 : 5, 
#4 : 4, 
#5 : 5, 
#6 : 6, 
#7 : 3,
#8 : 7,
#9 : 6,
#0 : 6
# 8 0 6 9 2 3 5 4 7 1 
# 7 6 6 6 5 5 5 4 3 2


# 1 7 4 2 3 5 0 6 9 8
# 2 3 4 5 5 5 6 6 6 7
# dp 배열의 인덱스는 성냥개비의 개수를 나타내고 값은 [최소값, 최대값] 이다.


#dp[2] = [1,1]
#dp[3] = [7,7]
#dp[4] = [4,11]
#dp[5] = [2,71]
#dp[6] = [6,111]
#dp[7] = [8,711]

#dp[8] = [10(2,6),1111]
#dp[9] = [18(2,7),7111]
#dp[10] = [22(5,5), 11111]
#dp[11] = [20(5,6) , 71111]
#dp[12] = [28(5,7) , 111111]
#dp[13] = [68(6,7) , 711111]
#dp[14] = [88(7,7) , 1111111]

# 15
# 108 7111111
# 16
# 188 11111111
# 17
# 200 71111111
# 18
# 208 111111111
# 19
# 288 711111111
# 20
# 688 1111111111
# 21
# 888 7111111111
# 22
# 1088 11111111111

T = int(input())
check = {1 : 2, 2 : 5, 3 : 5, 4 : 4, 5 : 5, 0 : 6, 6 : 6, 7 : 3, 8 : 7, 9 : 7}
dp = [0 for _ in range(103)]

dp[2] = 1
dp[3] = 7
dp[4] = 4
dp[5] = 2
dp[6] = 6
dp[7] = 8
dp[8] = 10
dp[9] = 18
dp[10] = 22

for i in range(T):
    matchstick = int(input())
    maxvalue = ""
    if matchstick % 2 == 0:
        for i in range(matchstick//2):
            maxvalue += "1"
    else:
        maxvalue += "7"
        for i in range(matchstick//2 - 1):
            maxvalue += "1"

    result = ""
    if matchstick < 11:
        print(dp[matchstick],end=" ")
        print(maxvalue)
    else :
        for j in range(8, matchstick+1):
            dp[j] = int(str(dp[j-7]) + "8")
        
        print(dp[matchstick],end=" ")
        print(maxvalue)
