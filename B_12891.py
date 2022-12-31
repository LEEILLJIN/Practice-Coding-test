# DNA 문자열의 길이 S, 비밀번호로 사용할 부분 문자열의 길이 P
# 임의의 DNA 문자열
# A C G T 각각에 최소 개수
S,P = map(int,input().split())
DNA = input()
A, C, G, T = map(int,input().split())
tempA, tempC, tempG, tempT = A, C, G, T
# 딕셔너리로 받고 싶은데?
start = 0
end = start + P
cnt = 0
rigthPassword = 0
print("temps", tempA, tempC, tempG, tempT)

# while end <= S:
#     for i in range(start, end):
#         print(start, end)
#         print("DNA[i]",DNA[i])
#         if DNA[i] == "A":
#             tempA -= 1
#         elif DNA[i] == "C":
#             tempC -= 1
#         elif DNA[i] == "G":
#             tempG -= 1
#         elif DNA[i] == "T":
#             tempT -= 1
#         if i
#         if i == end-1:
#             print(i)
#             print("temps", tempA, tempC, tempG, tempT)

#             if (tempA <= 0) and (tempC <= 0) and (tempG <= 0) and (tempT <= 0):
#                 rigthPassword += 1
            
#             tempA, tempC, tempG, tempT = A, C, G, T
#             print(start, end)
#             start += 1
#             end += 1
#             print("+된 start, end",start, end)
#             break

for i in range(S):
        print(start, end)
        print("DNA[i]",DNA[i])
        if DNA[i] == "A":
            tempA -= 1
        elif DNA[i] == "C":
            tempC -= 1
        elif DNA[i] == "G":
            tempG -= 1
        elif DNA[i] == "T":
            tempT -= 1
        if i >= P-1:
            if (tempA <= 0) and (tempC <= 0) and (tempG <= 0) and (tempT <= 0):
                rigthPassword += 1
            if DNA[start] == "A":
                tempA += 1
            elif DNA[start] == "C":
                tempC += 1
            elif DNA[start] == "G":
                tempG += 1
            elif DNA[start] == "T":
                tempT += 1

            start += 1

print(rigthPassword)
