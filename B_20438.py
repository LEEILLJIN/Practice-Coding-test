#3번부터 N+2번까지
# 학생수 N, 졸고 있는 학생의 수 K, 
# 지환이가 출석 코드르 보낼 학생의 수 Q, 주어질 구간의 수 M

#3, 6, 9, 12
#5, 10
#7

#4, 7, 8, 11
import sys
input = sys.stdin.readline

n, k, q, m = map(int, input().split())
sleepStu = [0]*(n+3)
checkStu = [0]*(n+3)

for i in map(int, input().split()):
    sleepStu[i] = 1

for i in map(int, input().split()):
    if sleepStu[i] :
        continue
    for j in range(i, n+3, i):
        if sleepStu[j] == 0:
            checkStu[j] = 1


AccuSum = [checkStu[0]]

for i in range(1, n+3):
    AccuSum.append(AccuSum[-1] + checkStu[i])
    #각 번호까지 출석한 애들의 누적 합

for _ in range(m):
    start, end = map(int, input().split())
    print(end-start + 1 - (AccuSum[end] - AccuSum[start-1]))



