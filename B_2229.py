#조별 수업의 목적은 잘 하는 학생들과 덜 잘 하는 학생들을 같은 조로 묶어서 서로 자극을 받으며 공부하도록 만들기 위함이다. 
#따라서 가급적이면 실력 차이가 많이 나도록 조를 편성하는 것이 유리하다.
#하지만 조를 편성할 때 같은 조에 속하게 된 학생들의 나이 차이가 많이 날 경우에는 오히려 부정적인 효과가 나타날 수도 있다.
#따라서 선생님들은 우선 학생들을 나이 순서대로 정렬한 다음에, 
#적당히 학생들을 나누는 방식으로 조를 짜기로 하였다. 조의 개수는 상관이 없다.

n = int(input())
score = list(map(int, input().split()))
dp = [0 for i in range(1001)]

for i in range(n+1):
    for j in range(i,0,-1):
        maxval = max(score[i-1],score[j-1])
        minval = min(score[i-1],score[j-1])
        dp[i] = max(dp[i], dp[j-1]+maxval-minval)

print(dp[n]) 

