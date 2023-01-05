# #N은 홀수
# # 산술평균 : N개의 수들의 합을 N으로 나눈 값
# # 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
# # 최빈값 : N개의 수들 중 가장 많이 나타나는 값
# # 범위 : N개의 수들 중 최댓값과 최솟값의 차이

# #input : 수의 개수
# #        수의 개수만큼의 수

# #12시 50분 시작 1시 7분
# from collections import defaultdict
# from sys import stdin
# input = stdin.readline

# Num = float(input())
# NumList = []
# answerList = []
# freNumList = defaultdict(int)

# for _ in range(int(Num)):
#     NumList.append(int(input()))
# NumList.sort()

# temp = []
# answerList.append(round(sum(NumList)/Num))
# answerList.append(NumList[int(Num)//2])

# for i in NumList:
#     if freNumList[i] == 0:
#         freNumList[i] = 1
#     else:
#         freNumList[i] += 1

# for i in freNumList.keys():
#     if freNumList[i] >1:
#         temp.append(i)

# if len(temp) == 1:
#     answerList.append(temp[0])
# elif len(temp) == 0:
#     if len(list(freNumList.keys())) >1:
#         answerList.append(list(freNumList.keys())[1])
#     else:
#         answerList.append(list(freNumList.keys())[0])

# elif len(temp) >1:
#     answerList.append(temp[1])

# answerList.append(max(NumList) - min(NumList))


# print(*answerList, sep="\n")
n = int(input())

nums = []
for _ in range(n) :
	nums.append(int(input()))

# 산술평균
print(round(sum(nums)/n))

# 중앙값
nums.sort()
print(nums[int((n-1)/2)])

# 최빈값
counts = dict()
for i in range(1,n+1) :
	counts[i] = []

maxCount = 1
count = 1
for j in range(1,n) :
	if nums[j] == nums[j-1] :
		count += 1
	else :
		counts[count].append(nums[j-1])
		if maxCount < count : maxCount = count
		count = 1
	if j == n-1 : 
		counts[count].append(nums[j])
		if maxCount < count : maxCount = count

if n == 1 :
	counts[1].append(nums[0])

counts[maxCount].sort()
if len(counts[maxCount]) == 1 :
	print(counts[maxCount][0])
else :
	print(counts[maxCount][1])

# 범위
print(nums[-1]-nums[0])